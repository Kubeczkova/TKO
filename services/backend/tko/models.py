from django.db import models

# Create your models here.
class Contact(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=16)
    content = models.TextField()


class Article(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    # image = models.ImageField(upload_to='articles/%Y/%m/%d')
    date = models.DateField()
    author = models.CharField(max_length=100)

    active_to = models.DateField(null=True, blank=True)  # do not show some invitation after this date


class Event(models.Model):
    title = models.CharField(max_length=100)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    color = models.CharField(max_length=100)
