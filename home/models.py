from django.db import models

from django.conf import settings

# Create your models here.


class survey_answers(models.Model):
    user_id = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    supports_fairtrade = models.BooleanField()
    supports_nochildlabor = models.BooleanField() 
    supports_lowcarbonemissions = models.BooleanField()
    supports_noanimaltesting = models.BooleanField()
    placeholder = models.BooleanField()
      

class company(models.Model):
    name = models.CharField(max_length=40, unique=True) #company name is the unique identifer in table 
    fairtrade = models.BooleanField()
    nochildlabor = models.BooleanField()
    bcorp = models.BooleanField()
    peta = models.BooleanField()
    point1 = models.CharField(max_length=1000)
    source1 = models.CharField(max_length=200)
    point2 = models.CharField(max_length=1000, blank=True)
    source2 = models.CharField(max_length=200, blank=True)    
    point3 = models.CharField(max_length=1000, blank=True)
    source3 = models.CharField(max_length=200, blank=True)
    point4 = models.CharField(max_length=1000, blank=True) 
    source4 = models.CharField(max_length=200, blank=True)
    point5 = models.CharField(max_length=1000, blank=True)
    source5 = models.CharField(max_length=200, blank=True)
    point6 = models.CharField(max_length=1000, blank=True)
    source6 = models.CharField(max_length=200, blank=True) #so max of 6 points of information about a company
    rating = models.IntegerField()
    stat1 = models.CharField(max_length=200, blank=True)
    stat2 = models.CharField(max_length=200, blank=True) 
    stat3 = models.CharField(max_length=200, blank=True) 
    stat4 = models.CharField(max_length=200, blank=True)
    news1 = models.CharField(max_length=200, blank=True)
    news2 = models.CharField(max_length=200, blank=True) 
    news3 = models.CharField(max_length=200, blank=True) 
    news4 = models.CharField(max_length=200, blank=True)
    stat1source = models.CharField(max_length=200, blank=True)
    stat2source = models.CharField(max_length=200, blank=True) 
    stat3source = models.CharField(max_length=200, blank=True) 
    stat4source = models.CharField(max_length=200, blank=True)
    news1source = models.CharField(max_length=200, blank=True)
    news2source = models.CharField(max_length=200, blank=True) 
    news3source = models.CharField(max_length=200, blank=True) 
    news4source = models.CharField(max_length=200, blank=True)
    products = models.CharField(max_length= 1000, blank=True) #write products comma separated
    comp_type = models.CharField(max_length=50,blank=True) # this is energy, tech, food, fashion, transport only!
     

class comments(models.Model):
    username = models.CharField(max_length=150)
    companyname = models.CharField(max_length=40)
    body = models.CharField(max_length = 400)
    upvotes = models.IntegerField()
    downvotes = models.IntegerField()
    date = models.CharField(max_length=30)
