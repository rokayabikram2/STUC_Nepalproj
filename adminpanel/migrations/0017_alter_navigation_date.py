# Generated by Django 4.1.4 on 2023-12-26 07:49

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('adminpanel', '0016_alter_navigation_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='navigation',
            name='date',
            field=models.DateField(default=django.utils.timezone.now, null=True),
        ),
    ]
