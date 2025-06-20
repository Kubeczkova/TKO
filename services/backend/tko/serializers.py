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
        return obj.article.title if obj.article else ''


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

    def get_image(self, obj):
        main_image = next(iter(obj.images.all()), None)

        if main_image:
            return ArticleImageSerializer(main_image, context=self.context).data
        return {
            "image": "http://localhost:8000/media/images/image.jpg",
            "title": "Výchozí obrázek",
        }


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