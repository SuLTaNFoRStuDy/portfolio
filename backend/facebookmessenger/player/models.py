from django.db import models

# Create your models here.
class Some(models.Model):
    ism=models.CharField(max_length=200,default="N/A",null=False)
    