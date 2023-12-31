# Generated by Django 4.1.4 on 2023-12-21 08:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('mobileno', models.CharField(max_length=50, null=True)),
                ('email', models.CharField(max_length=50)),
                ('message', models.TextField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ContactUS',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('mobileno', models.CharField(max_length=50, null=True)),
                ('email', models.CharField(max_length=50)),
                ('subject', models.CharField(max_length=50)),
                ('message', models.TextField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='GlobalSettings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('SiteName', models.CharField(max_length=100)),
                ('SiteContact', models.CharField(max_length=100)),
                ('SiteEmail', models.EmailField(max_length=254)),
                ('SiteAddress', models.CharField(max_length=500)),
                ('Sitedescription', models.CharField(max_length=500)),
                ('Sitelicence', models.CharField(max_length=300)),
                ('Sitetwitterlink', models.CharField(max_length=300)),
                ('Sitefacebooklink', models.CharField(max_length=300)),
                ('Sitelinkdinlink', models.CharField(max_length=300)),
                ('Siteinstagram', models.CharField(max_length=300)),
                ('Siteyoutubelink', models.CharField(max_length=300)),
                ('Sitefax', models.CharField(max_length=300, null=True)),
                ('SiteBox', models.CharField(max_length=300, null=True)),
                ('logo', models.ImageField(default=None, max_length=200, null=True, upload_to='Global/')),
                ('back_image', models.ImageField(null=True, upload_to='Global/')),
                ('brochure', models.FileField(null=True, upload_to='brochure/')),
                ('brochure_name', models.CharField(max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Navigation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('caption', models.CharField(max_length=100)),
                ('status', models.CharField(choices=[('Publish', 'Publish'), ('Draft', 'Draft')], max_length=50)),
                ('position', models.IntegerField()),
                ('page_type', models.CharField(blank=True, choices=[('Home', 'Home'), ('Slider', 'Slider'), ('Home/About', 'Home/About'), ('Features', 'Features'), ('Features_1', 'Features_1'), ('Home/Video', 'Home/Video'), ('Aboutus', 'Aboutus'), ('Aboutus_1', 'Aboutus_1'), ('Achievements', 'Achievements'), ('Achievements_1', 'Achievements_1'), ('Testimonials', 'Testimonials'), ('Blog', 'Blog'), ('Services', 'Services'), ('Vision', 'Vision'), ('Mission', 'Mission'), ('Objectives', 'Objectives'), ('Our Strength', 'Our Strength'), ('Research & Development', 'Research & Development'), ('Video_Gallery', 'Video_Gallery'), ('Gallery', 'Gallery'), ('Image_Gallery', 'Image_Gallery'), ('Contact', 'Contact'), ('Group', 'Group'), ('Video', 'Video'), ('Blog_1', 'Blog_1'), ('Services_1', 'Services_1'), ('Client', 'Client'), ('Client/Title', 'Client/Title'), ('Our Team', 'Our Team'), ('OurTeam/Slider', 'OurTeam/Slider')], max_length=50, null=True)),
                ('title', models.CharField(max_length=200)),
                ('short_desc', models.TextField(null=True)),
                ('desc', models.TextField(null=True)),
                ('bannerimage', models.ImageField(null=True, upload_to='about/')),
                ('meta_title', models.CharField(max_length=100, null=True)),
                ('meta_keyword', models.CharField(max_length=100, null=True)),
                ('icon_image', models.TextField(null=True)),
                ('slider_image', models.ImageField(null=True, upload_to='about/')),
                ('brochure', models.FileField(null=True, upload_to='brochure/')),
                ('date', models.DateField(auto_now_add=True, null=True)),
                ('image', models.ImageField(null=True, upload_to='about/')),
                ('video', models.FileField(null=True, upload_to='video/%y')),
                ('Parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='childs', to='adminpanel.navigation')),
            ],
        ),
    ]
