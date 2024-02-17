from django.db import models

# Create your models here.

class Datas(models.Model):
    Name=models.CharField(max_length=20,default="")
    Issue_ID=models.IntegerField(default="")
    Issue=models.CharField(max_length=50,default="")
    Contact=models.IntegerField(default="")
    Mail=models.CharField(max_length=50,default="")