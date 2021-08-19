from django.db import models
from django.utils import timezone
# Create your models here.
from django.db import models

# Create your models here.
class Comp_detail(models.Model):
    username=models.CharField(default="",blank=True,null=True,max_length=100)
    email=models.EmailField(default="",blank=True,null=True,max_length=50)
    password=models.CharField(default="",blank=True,null=True,max_length=20)
    income=models.FloatField(default=0.0,blank=True,null=True)
    expense=models.FloatField(default=0.0,blank=True,null=True)
    balance=models.FloatField(default=0.0,blank=True, null=True)
    



class Desc(models.Model):
    user1=models.ForeignKey('Comp_detail',on_delete=models.CASCADE,blank=True, null=True)
    amount=models.FloatField(default=0.0)
    desc=models.CharField(default="",blank=True,null=True,max_length=500)
    type1=models.CharField(default="",blank=True,null=True,max_length=5)
    created_at=models.DateTimeField(auto_now_add=True,blank=True, null=True)
    
    
