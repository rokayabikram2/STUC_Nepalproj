# Generated by Django 4.1.4 on 2023-12-27 07:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('adminpanel', '0029_contactus_mobileno'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contactus',
            old_name='mobilenum',
            new_name='mobile',
        ),
    ]
