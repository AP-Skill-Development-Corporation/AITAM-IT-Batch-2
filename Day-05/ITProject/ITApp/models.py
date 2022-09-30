from django.db import models

# Create your models here.
class Employee(models.Model):
	eid = models.CharField(max_length=50)
	ename = models.CharField(max_length=150)
	eemail = models.EmailField(max_length=200)
	eage = models.IntegerField()
	