# Generated by Django 3.2.15 on 2022-09-20 22:38

import ckeditor_uploader.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('users', '0030_alter_user_user_region'),
        ('events', '0104_auto_20220921_1025'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='accessible_online',
            field=models.BooleanField(default=False, help_text='Select if this participants will be attending this online e.g. Zoom'),
        ),
        migrations.AlterField(
            model_name='event',
            name='contact_email_address',
            field=models.EmailField(default='', help_text='The email which event participants can contact you via.', max_length=150),
        ),
        migrations.AlterField(
            model_name='event',
            name='description',
            field=ckeditor_uploader.fields.RichTextUploadingField(help_text="This is the description that will appear on this event's page that participants will view."),
        ),
        migrations.AlterField(
            model_name='event',
            name='event_staff',
            field=models.ManyToManyField(blank=True, help_text='To select multiple event staff members, hold CONTROL and click to select the individuals.', related_name='events', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='event',
            name='featured',
            field=models.BooleanField(default=False, help_text='Select if this event is a featured event.'),
        ),
        migrations.AlterField(
            model_name='event',
            name='is_catered',
            field=models.BooleanField(default=False, help_text='Select if food will be provided at this event. Participants will be ask for their dietary requirements when registering/applying'),
        ),
        migrations.AlterField(
            model_name='event',
            name='locations',
            field=models.ManyToManyField(blank=True, help_text='To select multiple event locations, hold CONTROL and click to select the locations.', related_name='events', to='events.Location'),
        ),
        migrations.AlterField(
            model_name='event',
            name='organisers',
            field=models.ManyToManyField(blank=True, help_text='To select multiple event organisers, hold CONTROL and click to select the sponsors.', related_name='events', to='users.Entity'),
        ),
        migrations.AlterField(
            model_name='event',
            name='registration_link',
            field=models.URLField(blank=True, help_text="Only required when the event registration type is 'external'. This is a link to an external location that will gather event applications' information e.g. Google Form", null=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='registration_type',
            field=models.PositiveSmallIntegerField(choices=[(1, 'Register to attend event'), (2, 'Apply to attend event'), (3, 'Visit event website'), (4, 'This event is invite only')], default=1, help_text='Register type events will not require you to approve or reject event reigstration forms.\nApply type events require you to approve event applications in order for a participant to be attending this event.'),
        ),
        migrations.AlterField(
            model_name='event',
            name='series',
            field=models.ForeignKey(blank=True, help_text='Optional. Select the series the event is a part of if it applies.', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='events', to='events.series'),
        ),
        migrations.AlterField(
            model_name='event',
            name='show_schedule',
            field=models.BooleanField(default=False, help_text="Select if you would like to show this event's schedule to prospective event participants."),
        ),
        migrations.AlterField(
            model_name='event',
            name='sponsors',
            field=models.ManyToManyField(blank=True, help_text='To select multiple event sponsors, hold CONTROL and click to select the sponsors.', related_name='sponsored_events', to='users.Entity'),
        ),
        migrations.AlterField(
            model_name='event',
            name='ticket_types',
            field=models.ManyToManyField(blank=True, help_text='The ticket types that will be available for event participants to choose from.', related_name='events', to='events.Ticket'),
        ),
        migrations.AlterField(
            model_name='registrationform',
            name='close_datetime',
            field=models.DateTimeField(blank=True, help_text='This is the date and time that participants registerations/applications close for this event.\nDesired format is YYYY-MM-DD hh:mm:ss, e.g. 2022-06-09 11:30:00 (9th May 2022 at 11.30am)', null=True),
        ),
        migrations.AlterField(
            model_name='registrationform',
            name='open_datetime',
            field=models.DateTimeField(blank=True, help_text='This is the date and time that participants can register/apply for this event.\nDesired format is YYYY-MM-DD hh:mm:ss, e.g. 2022-06-09 11:30:00 (9th May 2022 at 11.30am)', null=True),
        ),
        migrations.AlterField(
            model_name='registrationform',
            name='terms_and_conditions',
            field=ckeditor_uploader.fields.RichTextUploadingField(default='<p>Expenses for travel and accommodation are not covered by the event organisers, and are to be organised by the attendees themselves. Event organisers may provide details of available funding options that attendees&rsquo; may apply for.</p> <p>Should you need to cancel your application/registration, please let us know as soon as possible and we&#39;ll remove it. If you do not show to the event without informing us, you may be liable for a &lsquo;did not show&rsquo; fee. We understand life happens.</p> <p>In the event of cancellation of the event, we will notify you as soon as possible. It is your responsibility to understand any cancellation clauses for your flights and accommodation. While we are sorry if this causes inconvenience, the organisers will not be liable for any loss, damages, or sadness arising from such changes.</p> <p>Please be aware the event organisers and attendees may be taking photographs, video, and/or audio to record events. These may be displayed on websites or social media for education and/or promotional purposes. By attending the event you understand that these images and recordings may be used by the event organisers for related marketing and promotions. You understand that if you do not wish to have your image or voice recorded you must inform any media person taking your photo, videoing you, or recording your voice at the workshop. It is your responsibility to remove yourself from the photo, video, or voice recording situations. Photographers will do their best to take group images that do not identify people and will seek permission in particular instances where close ups are taken. Attendees posting on social media will be asked to check with you first, before posting. The event organisers does not accept responsibility for media posted by attendees.</p> <p>By registering for this event, you agree to us storing your information for organising and running the event. You are required to follow all health and safety instructions from event organisers while attending the event.</p> <p>Finally, you agree to and understand with the terms and conditions regarding the Code of Conduct. Read our Code of Conduct here: https://gist.github.com/uccser-admin/56de956a32ccf68e253be8632957c014</p>', help_text='Event participants must agree to this to register/apply for this event.'),
        ),
    ]
