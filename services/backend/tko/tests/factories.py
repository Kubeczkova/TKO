from random import randint

import factory
import datetime

from django.contrib.auth.models import User
from factory.fuzzy import FuzzyDate
from datetime import date

from tko.models import Article, Event, ArticleImage, Contact


class ContactFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Contact

    name = factory.Faker("name")
    email = factory.Faker("email")
    phone_number = factory.Faker("phone_number")
    content = factory.Faker("text")


class ArticleFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Article

    title = factory.Faker("name")
    content = factory.Faker("text")
    date = FuzzyDate(datetime.date(2021, 1, 1), date.today())
    author = factory.Faker("name")
    active_to = FuzzyDate(datetime.date(2021, 1, 1), datetime.date(2025, 1, 1))


class GalleryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = ArticleImage

    article = factory.SubFactory(ArticleFactory)
    image = factory.django.FileField(filename='image.png')
    main = factory.Faker("boolean")


class EventFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Event

    title = factory.Faker("name")
    start_date = FuzzyDate(datetime.date(2021, 1, 1), datetime.date(2025, 1, 1))
    end_date = factory.LazyAttribute(
        lambda obj: obj.start_date + datetime.timedelta(minutes=randint(5, 5 * 24 * 60))
    )
    color = factory.Faker("color")


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    username = factory.Faker("name")
    email = factory.Faker("email")
    password = "password"
    is_superuser = True
