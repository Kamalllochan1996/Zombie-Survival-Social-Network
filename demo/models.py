from django.db import models



class Locations(models.Model):
    latitude = models.CharField(max_length=100, null=True, blank=True)
    longitude = models.CharField(max_length=100, null=True, blank=True)

    # def __str__(self):
    #     return str(self.latitude)+ ' ' + str(self.longitude)

# Create your models here.
class Survivors(models.Model):
 name = models.CharField(max_length=50)
 age = models.IntegerField()
#  gender = models.BooleanField('Male')
 gender = models.CharField(max_length=6,
            choices=[('Male','Male'),('Female','Female')],default='Male'
            )
 def __str__(self):
    return self.name
 location = models.ManyToManyField(Locations)
 

class Reports(models.Model):
    infected = models.IntegerField()
    non_infected = models.IntegerField()


# class Locations(models.Model):
#     latitude = models.CharField(max_length=100, null=True, blank=True)
#     longitude = models.CharField(max_length=100, null=True, blank=True)

#     def __str__(self):
#         return str(self.latitude)+ ' ' + str(self.longitude)