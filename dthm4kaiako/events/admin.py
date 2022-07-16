"""Module for admin configuration for the events application."""
import logging
from django.contrib import admin
from django.utils.timezone import now
from django.contrib.gis.db import models as geomodels
from django.utils.translation import gettext_lazy as _
from events.models import (
    Event,
    Session,
    Location,
    Series,
    EventApplication,
    RegistrationForm,
    ApplicantType,
)
from mapwidgets.widgets import GooglePointFieldWidget
from modelclone import ClonableModelAdmin
from users.models import User
from django.utils.html import format_html_join

import datetime

datetime_str = '2016-05-18T15:37:36.993048Z'
old_format = '%Y-%m-%dT%H:%M:%S.%fZ'
new_format = '%d-%m-%Y %H:%M:%S'

logger = logging.getLogger(__name__)


class LocationAdmin(admin.ModelAdmin):
    """Inline view for event locations."""

    formfield_overrides = {
        geomodels.PointField: {"widget": GooglePointFieldWidget}
    }
    list_display = (
        'name',
        'room',
        'street_address',
        'suburb',
        'city',
        'region',
    )
    list_filter = ('region', )
    search_fields = (
        'name',
        'room',
        'street_address',
        'suburb',
        'city',
        'region',
    )


class SessionInline(admin.StackedInline):
    """Inline view for event sessions."""

    model = Session
    fk_name = 'event'
    extra = 3
    min_num = 1
    ordering = ('start', 'end', 'name')
    autocomplete_fields = ('locations', )


class RegistrationFormInline(admin.StackedInline):
    """Inline view for event registration form."""

    model = RegistrationForm
    fk_name = 'event'
    extra = 0
    min_num = 1


class EventUpcomingListFilter(admin.SimpleListFilter):
    """Custom filter for events admin."""

    title = _('time')

    # Parameter for the filter that will be used in the URL query.
    parameter_name = 'time'

    def lookups(self, request, model_admin):
        """Return a list of tuples.

        The first element in each tuple is the coded value for
        the option that will appear in the URL query.
        The second element is the human-readable name for
        the option that will appear in the right sidebar.
        """
        return (
            ('upcoming', _('Upcoming events')),
            ('past', _('Past events')),
            ('all', _('All events')),
        )

    def queryset(self, request, queryset):
        """Return filtered queryset.

        The filtered queryset is based on the value
        provided in the query string and retrievable via
        `self.value()`.
        """
        if self.value() is None:
            self.used_parameters[self.parameter_name] = 'upcoming'
        if self.value() == 'upcoming':
            return queryset.filter(end__gte=now())
        elif self.value() == 'past':
            return queryset.filter(end__lt=now())
        else:
            return queryset

    def choices(self, changelist):
        """Override default method to remove 'All' option."""
        for lookup, title in self.lookup_choices:
            yield {
                'selected': self.value() == str(lookup),
                'query_string': changelist.get_query_string({self.parameter_name: lookup}),
                'display': title,
            }


class EventAdmin(ClonableModelAdmin):
    """Admin view for an event."""

    model = Event
    inlines = [SessionInline, RegistrationFormInline]
    fieldsets = (
        (
            None,
            {
                'fields': (
                    'name',
                    'description',
                    'series',
                    'organisers',
                    'sponsors',
                    'is_free',
                    'is_catered',
                )
            }
        ),
        ('Location', {
            'fields': ('accessible_online', 'locations'),
        }),
        ('Registration', {
            'description': 'Currently only registration via URL is available.',
            'fields': (
                'registration_link',
                'registration_type',
            ),
        }),
        ('Visibility', {
            'fields': (
                'published',
                'featured',
                'show_schedule',
            ),
        }),
    )
    filter_horizontal = (
        'organisers',
        'sponsors',
    )
    list_display = ('name', 'location_summary', 'series', 'start', 'end', 'published', 'featured')
    list_filter = (EventUpcomingListFilter, 'organisers', )
    ordering = ('start', 'end', 'name')
    autocomplete_fields = ('locations', )
    save_on_top = True

    def save_related(self, request, form, formsets, change):
        """Trigger update of event datetimes after sessions are saved."""
        super().save_related(request, form, formsets, change)
        # Update datetimes on event after saving sessions
        form.instance.update_datetimes()

    class Media:
        """Custom media file overrides."""

        css = {
            'all': ('css/admin-overrides.css', )
        }



class EventApplicationAdmin(admin.ModelAdmin):
    """Admin view for an event application."""

    model = EventApplication
    readonly_fields = [
        'user',
        'user_education_entities',
        'user_region',
        'mobile_phone_number',
        'medical_notes',
        'user_dietary_requirements',
        'event',
        'event_start_end',
        'event_location',
        'submitted',
        'updated',
        'billing_physical_address',
        'billing_email_address',
        'participant_email_address',
        'emergency_contact_first_name',
        'emergency_contact_last_name',
        'emergency_contact_relationship',
        'emergency_contact_phone_number',
    ]
    fieldsets = (
        (
            'User',
            {
                'fields': (
                    'user',
                    'user_education_entities',
                    'user_region',
                    'mobile_phone_number',
                    'user_dietary_requirements',
                )
            },
        ),
        (
            'Event',
            {
                'fields': (
                    'event',
                    'event_start_end',
                    'event_location',
                )
            },
        ),
        (
            'Application',
            {
                'fields': (
                    'submitted',
                    'updated',
                    'status',
                    'applicant_type',
                    'participant_email_address',
                    'medical_notes',
                    'staff_comments',
                    'emergency_contact_first_name',
                    'emergency_contact_last_name',
                    'emergency_contact_relationship',
                    'emergency_contact_phone_number',
                )
            },
        ),
        (
            'Billing',
            {
                'fields': (
                    'paid',
                    'billing_physical_address',
                    'billing_email_address',
                )
            },
        ),
    )

    @admin.display(description="Educational entities participant belongs to")
    def user_education_entities(self, application):
        return format_html_join(
            '\n',
            '<li>{}</li>',
            application.user.educational_entities.values_list('name'),
        )

    @admin.display(description="User's region")
    def user_region(self, application):
        return application.user.region

    @admin.display(description="User's dietary requirements")
    def user_dietary_requirements(self, application):
        return format_html_join(
            '\n',
            '<li>{}</li>',
            application.user.dietary_requirements.values_list('name'),
        )

    @admin.display
    def event_start_end(self, application):
        # formatted_start = datetime.datetime.strptime(str(application.event.start), old_format).strftime(new_format)
        # formatted_end = datetime.datetime.strptime(str(application.event.end), old_format).strftime(new_format)
        # return f'{formatted_start} to {formatted_end}'

        return f'{application.event.start} to {application.event.end}'

    @admin.display
    def event_location(self, application):
        return application.event.location_summary()

    # TODO: remove this and replace with applicant type attendance fee
    # @admin.display
    # def event_price(self, application):
    #     return f'${application.event.price:.2f}'

    @admin.display
    def mobile_phone_number(self, application):
        return application.user.mobile_phone_number

    @admin.display
    def medical_notes(self, application):
        return application.user.medical_notes

    @admin.display
    def participant_email_address(self, application):
        return application.event_application.participant_email_address

    @admin.display
    def emergency_contact_first_name(self, application):
        return application.event_application.emergency_contact_first_name

    @admin.display
    def emergency_contact_last_name(self, application):
        return application.event_application.emergency_contact_last_name

    @admin.display
    def emergency_contact_relationship(self, application):
        return application.event_application.emergency_contact_relationship

    @admin.display
    def emergency_contact_phone_number(self, application):
        return application.event_application.emergency_contact_phone_number


admin.site.register(Event, EventAdmin)
admin.site.register(Location, LocationAdmin),
admin.site.register(Series),
admin.site.register(Session),
admin.site.register(EventApplication, EventApplicationAdmin),
admin.site.register(RegistrationForm),
admin.site.register(ApplicantType),
