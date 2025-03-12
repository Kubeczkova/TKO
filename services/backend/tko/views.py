from django.utils import timezone
from django.db.models import Q

from rest_framework.generics import ListAPIView, CreateAPIView
from rest_framework import permissions

from tko.models import Article, Event, ArticleImage
from tko.serializers import ArticleListSerializer, EventListSerializer, ContactSerializer, ArticleImageSerializer


class ContactView(CreateAPIView):
    serializer_class = ContactSerializer
    permission_classes = [permissions.AllowAny]


class NewArticleListView(ListAPIView):
    serializer_class = ArticleListSerializer
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        return Article.objects.filter(
            Q(active_to__gte=timezone.now()) | Q(active_to__isnull=True)
        ).order_by('-date')[:2]


class AllArticleListView(ListAPIView):
    serializer_class = ArticleListSerializer
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        return Article.objects.filter(
            Q(active_to__gte=timezone.now()) | Q(active_to__isnull=True)
        ).order_by('-date')


class GalleryView(ListAPIView):
    queryset = ArticleImage.objects.all().order_by("-article_id", "main")
    serializer_class = ArticleImageSerializer
    permission_classes = [permissions.AllowAny]


class EventListView(ListAPIView):
    queryset = Event.objects.all()
    serializer_class = EventListSerializer
    permission_classes = [permissions.AllowAny]
