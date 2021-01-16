from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    pass


class Lead(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    age = models.IntegerField(default=0)
    # in my case I follow the tutorial but I think that use set_null is better
    #agent = models.ForeignKey("Agent", on_delete=SET_NULL, null=True)
    agent = models.ForeignKey("Agent", on_delete=models.CASCADE)

class Agent(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)




    # SOURCE_CHOICES = (
    #     ('YouTube','Youtube'),
    #     ('Google','Google'),
    #     ('Newletter','Newletter')
    # )



    # phoned = models.BooleanField(default=False)
    # source = models.CharField(choices=SOURCE_CHOICES, max_length=100)

    # profile_images = models.ImageField(blank=True, null=True)
    # special_files = models.FileField(blank=True, null=True)