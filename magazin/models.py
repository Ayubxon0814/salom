from django.db import models
from django.forms import CharField


class TimeStampedModel(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    class Meta:
        abstract = True

class Oluvchi(TimeStampedModel):
    yosh = models.PositiveIntegerField(null=True, blank=True)
    Char = models.CharField(null=True, blank=True)
    Text = models.TextField(null=True, blank=True)
    Email = models.EmailField(null=True, blank=True)
    URL = models.URLField(null=True, blank=True)
    yosh6 = models.IntegerField(null=True, blank=True)
    yosh7 = models.FloatField(null=True, blank=True)
    yosh8 = models.DecimalField(null=True, blank=True)
    yosh9 = models.DateField(null=True, blank=True)
    yosh10 = models.TimeField(null=True, blank=True)
    yosh11 = models.DateTimeField(null=True, blank=True)
    yosh12 = models.DurationField(null=True, blank=True)
    yosh13 = models.BooleanField(null=True, blank=True)
    yosh14 = models.FileField(null=True, blank=True)


