from django.db import models

# Create your models here.

class Resume(models.Model):
    phone=models.BigIntegerField(primary_key=True)
    about=models.TextField()
    name=models.CharField(max_length=100)    
    email=models.CharField(max_length=200)
    links=models.CharField(max_length=200)

    bachelors=models.CharField(max_length=100)
    bcollege=models.CharField(max_length=100)
    bpercent=models.IntegerField()
    bpass=models.IntegerField()

    stream=models.CharField(max_length=100)
    school=models.CharField(max_length=100)
    spercent=models.IntegerField()
    spass=models.IntegerField()

    skill1=models.CharField(max_length=50)
    skill2=models.CharField(max_length=50)
    skill3=models.CharField(max_length=50)
    skill4=models.CharField(max_length=50)

    exp1=models.CharField(max_length=100)
    exp2=models.CharField(max_length=100)
    exp3=models.CharField(max_length=100)
    exp4=models.CharField(max_length=100)

