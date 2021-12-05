from django.db import models

Deps = (
    ('Languages', 'Languages'),
    ('Maths', 'Maths'),
    ('Sciences', 'Sciences'),
    ('Humanities', 'Humanities'),
    ('Others', 'Others'),
    ('Hr', 'Hr'),
)


# Create your models here.
class Teachers(models.Model):
    Tid= models.CharField(max_length=26)
    user_id= models.TextField()
    D_O_E= models.DateTimeField()
    Department= models.CharField(max_length=50,choices=Deps, default='Departments')