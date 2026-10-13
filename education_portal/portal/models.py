from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class CustomUserModel(AbstractUser):
    USER_TYPE={
        ('Admin','Admin'),
        ('Teacher','Teacher'),
    }

    user_type=models.CharField(max_length=10,choices=USER_TYPE)




class TeacherModel(models.Model):
    teacher_name=models.CharField(max_length=100,null=True)
    last_education=models.CharField(max_length=100,null=True)
    phone = models.CharField(max_length=15)
    address = models.TextField()

    def __str__(self):
        return self.teacher_name

class StudentBasicInfoModel(models.Model):
    name=models.CharField(max_length=100,null=True)
    email=models.ImageField()
    address=models.TextField()

    def __str__(self):
        return self.name

class StudentEducationInfoModel(models.Model):
    student=models.ForeignKey(StudentBasicInfoModel,on_delete=models.CASCADE,related_name='educations')
    degree_name=models.CharField(max_length=100,null=True)
    degree=models.CharField(max_length=20,null=True)
    passing_year=models.CharField(max_length=20,null=True)

    def __str__(self):
        return self.name