from django.db import models

class Shelf(models.Model):
    title = models.CharField(max_length=150)
    author = models.CharField(max_length=150)
    year = models.IntegerField()
    short_story_tells = models.TextField(blank=True)
    rate = models.FloatField()
    l_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)