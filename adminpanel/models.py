from django.db import models
from django.utils import timezone

class GlobalSettings(models.Model):
    SiteName = models.CharField(max_length=100,null =True)
    name_nepali = models.CharField(max_length=100,null =True)
    SiteContact = models.CharField(max_length=100,null =True)
    SiteEmail = models.EmailField()
    SiteAddress = models.CharField(max_length=500,null =True)
    Sitedescription = models.CharField(max_length=500,null =True)
    Sitetwitterlink = models.CharField(max_length=300,null =True)
    Sitefacebooklink = models.CharField(max_length=300,null =True)
    Siteyoutubelink = models.CharField(max_length=300,null =True)
    Sitefax = models.CharField(max_length=300,null=True)
    logo = models.ImageField(upload_to="Global/",max_length=200, null=True,default=None)
    flag_logo = models.ImageField(upload_to="logo/",null=True,default=None)
    back_image = models.ImageField(upload_to="Global/",null=True)

    def __str__(self):
        return self.SiteName

class ContactUS(models.Model):
    name = models.CharField(max_length=50)
    mobile = models.CharField(max_length=50,null=True)
    email = models.CharField(max_length=50)
    message = models.TextField(null=True)
    
    def __str__(self):
        return self.name
    
class Comment(models.Model):
    name = models.CharField(max_length=50)
    mobileno = models.CharField(max_length=50,null=True)
    email = models.CharField(max_length=50)
    message = models.TextField(null=True)
    
    def __str__(self):
        return self.name
    
    

class Navigation(models.Model):
    PAGE_TYPE = (
        ('Home', 'Home'),('Home/Banner','Home/Banner'),('Notice','Notice'),('Major Activities','Major Activities'),('About/introduction','About/introduction'),
        ('Associate Organization','Associate Organization'),('Board of Directors','Board of Directors'),('Chairman Message','Chairman Message'),
        ('Secretary Message','Secretary Message'),('Bidhans','Bidhans'),('News/Events','News/Events'),('Issue/Campaigns','Issue/Campaigns'),('Publications','Publications'),
        ('Membership Form','Membership Form'),('Image_Gallery', 'Image_Gallery'),('Video_Gallery', 'Video_Gallery'),('Download','Download'),('Press release','Press release'),
        ('Contact', 'Contact')
        
    )

    STATUS = (
        ('Publish', 'Publish'),
        ('Draft', 'Draft')
    )
    name = models.CharField(max_length=100, null=False)
    caption = models.CharField(max_length=100,null=True)
    status = models.CharField(choices=STATUS, max_length=50)
    position = models.IntegerField()
    page_type = models.CharField(choices=PAGE_TYPE, null=True, blank=True, max_length=50)
    title = models.CharField(max_length=200)
    short_desc = models.TextField(null=True)
    desc = models.TextField(null=True)
    bannerimage = models.ImageField(upload_to="about/",null=True)
    meta_title = models.CharField(max_length=100, null=True)
    meta_keyword = models.CharField(max_length=100, null=True)
    icon_image = models.TextField(null=True)
    slider_image = models.ImageField(upload_to="about/", null=True)
    Parent = models.ForeignKey('self', related_name="childs", on_delete=models.CASCADE, null=True, blank=True)
    brochure = models.FileField(upload_to="brochure/",null=True)
    date = models.DateField(null=True, blank=True)
    image = models.ImageField(upload_to="about/",null=True)
    video = models.FileField(upload_to="video/%y", null=True)

    def __str__(self):
        return self.name
    
    
    
class Membership(models.Model):
    name = models.CharField(max_length=100)
    mobile = models.CharField(max_length=100)
    Gender = models.CharField(max_length=100)
    date = models.CharField(max_length=100)
    citizenship = models.CharField(max_length=100)
    issued_district = models.CharField(max_length=50)
    province = models.CharField(max_length=100)
    district = models.CharField(max_length=100)
    muncipality = models.CharField(max_length=100)
    ward = models.CharField(max_length=50)
    fathers_name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
    
    
    
    


