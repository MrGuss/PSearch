from django.db import models

# Create your models here.
class Para(models.Model):
    Id = models.BigAutoField(auto_created=True, primary_key=True, serialize=False)
    date = models.IntegerField()
    period = models.IntegerField()
    nameC = models.CharField(max_length=500)
    categ = models.CharField(max_length=100)
    nameT = models.CharField(max_length=50)
    place = models.CharField(max_length=500)

class Teacher(models.Model):
    def __str__(self):
        return self.nameT 

    Id = models.BigAutoField(auto_created=True, primary_key=True, serialize=False)
    nameT = models.CharField(max_length=30)