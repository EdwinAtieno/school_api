from django.db import models

doms = (
    ('Menengai', 'Menengai'),
    ('Satima', 'Satima'),
    ('Batian', 'Batian'),
    ('Lenana', 'Lenana')
)


# Create your models here.
class Students(models.Model):
    Sid = models.CharField(max_length=26)
    user_id = models.TextField()
    Class = models.CharField(max_length=25)
    Dormitory = models.CharField(max_length=25,choices=doms, default='doms')