from django.db import models

# Create your models here.

class User(models.Model):
    pass

class Category(models.Model):
    name = models.CharField(max_length=32, verbose_name="Категория")


class Planet(models.Model):
    name = models.CharField(max_length=32, verbose_name="Планета")
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null = True, blank = True) # on_delete=models.CASCADE
                                                # related_name="name" 
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null = True, blank = True)


User.login = models.CharField(max_length=32, null=False, unique=True)
User.name = models.CharField(max_length=32)
User.notes = models.ManyToManyField(Planet)

# planet = Planet()
# planet.name = "Earth"
# planet.save()

# categoryes = Category.objects.all()
# categoryes.fist().name = "newName"
# ...save