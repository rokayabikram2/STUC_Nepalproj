# Generated by Django 4.1.4 on 2023-12-24 07:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminpanel', '0002_alter_globalsettings_sitelinkdinlink'),
    ]

    operations = [
        migrations.AddField(
            model_name='globalsettings',
            name='flag_logo',
            field=models.ImageField(default=None, null=True, upload_to='logo'),
        ),
    ]
