from django.db import models

# Create your models here.
class user(models.Model):
    account = models.CharField(max_length=32)
    password = models.CharField(max_length=32)
    email =models.EmailField(null=True)
    tel = models.IntegerField(null=True,default=12345678911)
    insert_time = models.DateTimeField(null=True)
    update_time = models.DateTimeField(null=True)

