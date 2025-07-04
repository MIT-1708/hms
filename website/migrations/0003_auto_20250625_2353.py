# Generated by Django 5.2 on 2025-06-25 18:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('website', '0002_appointmentinquiry_is_notification_sent_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactInquiry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=20)),
                ('subject', models.CharField(max_length=200)),
                ('message', models.TextField()),
                ('status', models.CharField(choices=[('PENDING', 'Pending'), ('READ', 'Read'), ('REPLIED', 'Replied'), ('CLOSED', 'Closed')], default='PENDING', max_length=20)),
                ('admin_notes', models.TextField(blank=True, help_text='Internal notes for staff', null=True)),
                ('reply_message', models.TextField(blank=True, help_text='Reply message sent to customer', null=True)),
                ('is_notification_sent', models.BooleanField(default=False)),
                ('notification_seen', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('replied_at', models.DateTimeField(blank=True, null=True)),
                ('assigned_to', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='assigned_contact_inquiries', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Contact Inquiries',
                'ordering': ['-created_at'],
            },
        ),
    ]
