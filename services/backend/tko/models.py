from django.db import models
from wagtail.admin.panels import FieldPanel
from wagtail.fields import RichTextField
from wagtail.models import Page
from datetime import date


# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=16)
    content = models.TextField()

    def __str__(self):
        return f"{self.name}, {self.email}, {self.phone_number}"


class Article(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    image = models.FileField(default="default.png", blank=True)
    date = models.DateField(auto_now_add=True)
    author = models.CharField(max_length=100)

    active_to = models.DateField(null=True, blank=True)  # do not show some invitation after this date

    def __str__(self):
        return self.title


class Event(models.Model):
    title = models.CharField(max_length=100)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    color = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class EventPage(Page):
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    color = models.CharField(max_length=100)

    content_panels = Page.content_panels + ["start_date", "end_date", "color"]


class ArticlePage(Page):
    name = models.CharField(max_length=100)
    content = models.CharField(max_length=500)
    image = models.ManyToManyField('wagtailimages.Image')
    date = models.DateField(default=date.today)
    author = models.CharField(max_length=100)

    content_panels = Page.content_panels + ["name", "content", "image", "date", "author", "expire_at"]