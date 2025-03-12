from rest_framework import serializers
from django.utils.timezone import localtime

from tko.models import Contact, Article, Event, ArticleImage


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'


class ArticleImageSerializer(serializers.ModelSerializer):
    title = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = ArticleImage
        fields = ['image', 'title']

    @staticmethod
    def get_title(obj):
        return obj.article.title


class ArticleListSerializer(serializers.ModelSerializer):
    date = serializers.SerializerMethodField()
    image = serializers.SerializerMethodField()
    images = ArticleImageSerializer(many=True, read_only=True)

    class Meta:
        model = Article
        fields = ["id", "author", "content", "date", "image", "title", "images"]

    @staticmethod
    def get_date(obj):
        return obj.date.strftime("%-d. %-m. %Y")

    @staticmethod
    def get_image(obj):
        main_image = obj.images.order_by("main").first()
        return main_image.image.url if main_image else None


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