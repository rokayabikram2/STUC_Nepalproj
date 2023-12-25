# Generated by Django 4.1.4 on 2023-12-25 05:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminpanel', '0007_rename_brochure_name_globalsettings_name_nepali_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='navigation',
            name='page_type',
            field=models.CharField(blank=True, choices=[('Home', 'Home'), ('Banner', 'Banner'), ('Home/About', 'Home/About'), ('Features', 'Features'), ('Features_1', 'Features_1'), ('Home/Video', 'Home/Video'), ('Aboutus', 'Aboutus'), ('Aboutus_1', 'Aboutus_1'), ('Achievements', 'Achievements'), ('Achievements_1', 'Achievements_1'), ('Testimonials', 'Testimonials'), ('Blog', 'Blog'), ('Services', 'Services'), ('Vision', 'Vision'), ('Mission', 'Mission'), ('Objectives', 'Objectives'), ('Our Strength', 'Our Strength'), ('Research & Development', 'Research & Development'), ('Video_Gallery', 'Video_Gallery'), ('Gallery', 'Gallery'), ('Image_Gallery', 'Image_Gallery'), ('Contact', 'Contact'), ('Group', 'Group'), ('Video', 'Video'), ('Blog_1', 'Blog_1'), ('Services_1', 'Services_1'), ('Client', 'Client'), ('Client/Title', 'Client/Title'), ('Our Team', 'Our Team'), ('OurTeam/Slider', 'OurTeam/Slider')], max_length=50, null=True),
        ),
    ]