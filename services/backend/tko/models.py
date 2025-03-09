from django.db import models


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
    image = models.FileField(upload_to="images/%Y", default="default.png", blank=True)
    date = models.DateField(auto_now_add=True)
    author = models.CharField(max_length=100)

    active_to = models.DateField(null=True, blank=True)  # do not show some invitation after this date

    def __str__(self):
        return self.title


class ArticleImage(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='images')
    image = models.FileField(upload_to="images/%Y")

    def __str__(self):
        return f"Image for {self.article.title}, {self.article.date}"


class Event(models.Model):
    title = models.CharField(max_length=100)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    color = models.CharField(max_length=100)

    def __str__(self):
        return self.title
