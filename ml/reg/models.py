from django.db import models

# Create your models here.
class Data(models.Model):
	x = models.CharField(max_length=10000)
	y = models.CharField(max_length=10000,blank=True)
	testx = models.CharField(max_length=10000,blank=True)