# Generated by Django 4.1.4 on 2023-12-26 07:52

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminpanel', '0017_alter_navigation_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='navigation',
            name='date',
            field=models.DateField(default=datetime.date.today, null=True),
        ),
    ]