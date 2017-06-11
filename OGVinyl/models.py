from django.db import models

# Create your models here.

class Artist(models.Model):
    name = models.CharField(max_length=200)
    line_up = models.CharField(max_length=1000, null=True, blank=True)
    def __str__(self):
        return self.name

class Format(models.Model):
    medium = models.CharField(max_length=50)
    def __str__(self):
        return self.medium

class Genre(models.Model):
    genre = models.CharField(max_length=50)
    def __str__(self):
        return self.genre

class Record(models.Model):
    created = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=100)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    year = models.IntegerField(null=True, blank=True) 
    medium = models.ForeignKey(Format, on_delete=models.CASCADE)
    release = models.CharField(max_length=50, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    genre = models.ManyToManyField(Genre)
    owned = models.BooleanField()
    note = models.CharField(max_length=200, null=True, blank=True)
    image = models.CharField(max_length=100, null=True, blank=True)
    featured = models.BooleanField(default=0)
    def __str__(self):
        return self.name


