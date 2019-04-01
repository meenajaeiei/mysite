from django.db import models


class Data(models.Model):
    AGE = models.IntegerField(default=0)
    HEIGHT = models.IntegerField(default=0)
    datetime = models.DateField(default="2019-03-13")
    WEIGHT = models.FloatField(default=0)
    FATPER = models.FloatField(default=0)
    FATAMT = models.FloatField(default=0)
    FFMAMT = models.FloatField(default=0)
    MSLAMT = models.FloatField(default=0)
    BMI = models.FloatField(default=0)
    Muscle_Index = models.FloatField(default=0)


class PublishedManager(models.Manager):
    def get_queryset(self):
        return super(PublishedManager, self).get_queryset().all()

class History(models.Model):
    datetime_data = models.DateField(default="7777-01-01")
    datetime_trans = models.DateField(default="7777-01-01")
    author = models.CharField(default="default", max_length=50)
    filename = models.CharField(default="default", max_length=50)
    published = PublishedManager()  # Our custom manager.


