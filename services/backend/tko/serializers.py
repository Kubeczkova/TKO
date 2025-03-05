from rest_framework import serializers
from django.utils.timezone import localtime

from tko.models import Contact, Article, Event


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'


class ArticleListSerializer(serializers.ModelSerializer):
    date = serializers.SerializerMethodField()

    class Meta:
        model = Article
        fields = ["id", "author", "content", "date", "image", "title"]

    @staticmethod
    def get_date(obj):
        return obj.date.strftime("%-d. %-m. %Y")


class EventListSerializer(serializers.ModelSerializer):
    start = serializers.SerializerMethodField()
    end = serializers.SerializerMethodField()

    class Meta:
        model = Event
        fields = ["title", "end", "start", "color"]

    @staticmethod
    def get_start(obj):
        return localtime(obj.start_date).isoformat() if obj.start_date else None

    @staticmethod
    def get_end(obj):
        return localtime(obj.end_date).isoformat() if obj.end_date else None