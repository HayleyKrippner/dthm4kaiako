from django.urls import reverse, resolve
from http import HTTPStatus
from tests.BaseTestWithDB import BaseTestWithDB
from users.models import User
from django.contrib.gis.geos import Point
import datetime
from events.models import (
    Location,
    Event,
)
from django.test.utils import override_settings


class RegistrationsURLTest(BaseTestWithDB):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def test_valid_registrations_url(self):
        url = reverse("events:event_registrations")
        self.assertEqual(url, "/events/registrations/")

    def test_registrations_resolve_provides_correct_view_name(self):
        self.assertEqual(resolve("/events/registrations/").view_name, "events:event_registrations")

    @override_settings(GOOGLE_MAPS_API_KEY="mocked")
    def test_registrations_gives_200_status_code(self):

        user_kate = User.objects.create_user(
            id=1,
            username='kate',
            first_name='Kate',
            last_name='Bush',
            email='kate@uclive.ac.nz',
            password='potato',
        )
        user_kate.save()

        location_1 = Location.objects.create(
            id=1,
            room='Room 123',
            name='Middleton Grange School',
            street_address='12 High Street',
            suburb='Riccarton',
            city='Chrirstchurch',
            region=14,
            coords=Point(-43, 172)
        )
        location_1.save()

        event_physical_register_1 = Event.objects.create(
            id=1,
            name="DTHM for Kaiako Conference 2023",
            description="description",
            registration_type=1,
            start=datetime.date(2023, 6, 24),
            end=datetime.date(2023, 6, 26),
            accessible_online=False,
            published=True
        )
        event_physical_register_1.locations.set([location_1])
        event_physical_register_1.save()

        event = Event.objects.get(pk=event_physical_register_1.pk)
        event.event_staff.set([user_kate])
        event.save()
        self.client.force_login(user_kate)
        url = reverse("events:event_registrations")
        response = self.client.get(url)
        self.assertEqual(HTTPStatus.OK, response.status_code)