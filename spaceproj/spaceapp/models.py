from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    notes = models.ManyToManyField('Planet')

class Category(models.Model):
    name = models.CharField(max_length=32, verbose_name="Категория")
    def __str__(self):
        return f"{self.name}"

class Atmosphere(models.Model):
    h2 = models.FloatField(default=0.0, verbose_name="водород")
    he = models.FloatField(default=0.0, verbose_name="гелий")
    h2O = models.FloatField(default=0.0, verbose_name="вода")
    co2 = models.FloatField(default=0.0, verbose_name="углекислый газ")
    n = models.FloatField(default=0.0, verbose_name="азот")
    o2 = models.FloatField(default=0.0, verbose_name="кислород")
    ar = models.FloatField(default=0.0, verbose_name="аргон")
    other = models.FloatField(default=0.0, verbose_name="другое")


class StarSystem(models.Model):
    name = models.CharField(max_length=32, verbose_name="Звёздная система")
    def __str__(self):
        return f"{self.name}"

class Planet(models.Model):
    name = models.CharField(max_length=32, unique=True, verbose_name="Планета")
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null = True, blank = True) # on_delete=models.CASCADE
                                                # related_name="name" 
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null = True, blank = True)
    
    starSystem = models.ForeignKey(StarSystem, on_delete=models.SET_NULL, null = True, blank = True)

    orbit = models.IntegerField(default = 1)
    atmosphere = models.OneToOneField(Atmosphere, null=True, blank=True, on_delete=models.SET_NULL)
    def __str__(self):
        return f"{self.name}"

# User.login = models.CharField(max_length=32, null=False, unique=True)
# User.name = models.CharField(max_length=32)

# planet = Planet()
# planet.name = "Earth"
# planet.save()

# categoryes = Category.objects.all()
# categoryes.fist().name = "newName"
# ...save