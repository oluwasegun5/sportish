from django.db import models
from auth_app.models import User


# Create your models here.

class Player(models.Model):
    ROLE_CHOICES = [
        ("COA", "Coach"),
        ("GK", "Goal-Keeper"),
        ("DF", "Defender"),
        ("MF", "Midfielder"),
        ("FWD", "Forward")
    ]
    FOOT_CHOICES = [
        ("RGT", "Right"),
        ("LFT", "Left"),
        ("BTH", "Both")
    ]
    team = models.ForeignKey('Team', on_delete=models.SET_NULL, null=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=11, choices=ROLE_CHOICES)
    strong_foot = models.CharField(max_length=5, null=True, choices=FOOT_CHOICES)
    country = models.CharField(max_length=255, default="Nigeria")
    organization = models.CharField(max_length=255, null=True)
    picture = models.ImageField(upload_to='sport_app/images')
    height = models.DecimalField(max_digits=3, decimal_places=1)


class Competition(models.Model):
    host = models.ForeignKey('Host', on_delete=models.SET_NULL, null=True)
    competition_name = models.CharField(max_length=255)
    minutes = models.SmallIntegerField()
    venue = models.CharField(max_length=255)
    competition_info = models.TextField()
    competition_logo = models.ImageField(upload_to='sport_app/images')
    date_created = models.DateField(auto_now=True)
    organization = models.CharField(max_length=255, null=True)

    def __str__(self):
        return self.name


class Manager(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    organization = models.CharField(max_length=255, null=True)
    profile_picture = models.ImageField(upload_to='sport_app/images')

    def __str__(self):
        return str(self.user.username)


class Team(models.Model):
    date_created = models.DateField(auto_now=True)
    manager = models.OneToOneField(Manager, on_delete=models.SET_NULL, null=True)
    competition = models.ForeignKey(Competition, on_delete=models.SET_NULL, null=True)
    teamName = models.CharField(max_length=255)
    teamLogo = models.ImageField(upload_to='sport_app/images')
    organization = models.CharField(max_length=255, null=True)

    def __str__(self):
        return self.teamName


class Host(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    organization = models.CharField(max_length=255, null=True)
    phone = models.CharField(max_length=15)
    profile_picture = models.ImageField(upload_to='sport_app/images')

    def __str__(self):
        return str(self.user)
