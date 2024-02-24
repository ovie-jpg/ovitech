from django.db import models
from django.urls import reverse

# Create your models here.

class Profile(models.Model):
    img= models.ImageField(upload_to= 'media', default='\img\gallery\project-2.jpg')
    first_name= models.CharField(max_length= 25)
    last_name= models.CharField(max_length= 25)
    bio= models.TextField(default="none")
    qualifications= models.TextField(default="None")
    email= models.EmailField()
    twitter= models.URLField(blank= True, null= True)
    instagram= models.URLField(blank= True, null= True)
    facebook= models.URLField(blank= True, null= True)
    linkedin= models.URLField(blank= True, null= True)

    def get_absolute_url(self):
        return reverse('home')

class Projects(models.Model):
    img= models.ImageField(upload_to= 'media', default='\img\gallery\project-2.jpg')
    title= models.CharField(max_length=25)
    name= models.CharField(max_length=25)
    bio= models.TextField()
    link= models.URLField()

    def get_absolute_url(self):
        return reverse('home')

class Blog(models.Model):
    title= models.CharField(max_length=25)
    link= models.URLField(blank= True, null= True)
    description= models.TextField()
    pub_date= models.DateTimeField(auto_now_add= True)

    def get_absolute_url(self):
        return reverse('home')