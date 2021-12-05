from django.db import models

roles = (
    ('Staff', 'Staff'),
    ('Teacher', 'Teacher'),
    ('Student', 'Student'),
)
genders = (
    ('Male', 'Male'),
    ('Female', 'Female'),
)


# Create your models here.
class Teachers(models.Model):
    user_id= models.CharField(max_length=26)
    name= models.CharField(max_length=26)
    Date_Of_Birth= models.DateTimeField()
    age= models.IntegerField()
    gender = models.CharField(max_length=25, choices=genders, default='Select Gender')
    role = models.CharField(max_length=25, choices=roles, default='Role')
