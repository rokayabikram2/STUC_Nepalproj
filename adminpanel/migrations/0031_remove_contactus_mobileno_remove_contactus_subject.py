# Generated by Django 4.1.4 on 2023-12-27 07:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('adminpanel', '0030_rename_mobilenum_contactus_mobile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contactus',
            name='mobileno',
        ),
        migrations.RemoveField(
            model_name='contactus',
            name='subject',
        ),
    ]