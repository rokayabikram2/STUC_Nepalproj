# Generated by Django 4.1.4 on 2023-12-21 09:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminpanel', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='globalsettings',
            name='Sitelinkdinlink',
            field=models.CharField(max_length=300, null=True),
        ),
    ]
