# Generated by Django 4.1.4 on 2023-12-26 10:24

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('adminpanel', '0024_alter_navigation_page_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='navigation',
            name='date',
            field=models.DateField(blank=True, default=django.utils.timezone.now, null=True),
        ),
    ]
