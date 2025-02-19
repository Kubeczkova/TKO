from rest_framework.generics import ListAPIView, CreateAPIView
from rest_framework import permissions

from tko.models import Article, Event
from tko.serializers import ArticleListSerializer, EventListSerializer, ContactSerializer


class ContactView(CreateAPIView):
    serializer_class = ContactSerializer
    permission_classes = [permissions.AllowAny]


class ArticleListView(ListAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleListSerializer
    permission_classes = [permissions.AllowAny]


class EventListView(ListAPIView):
    queryset = Event.objects.all()
    serializer_class = EventListSerializer
    permission_classes = [permissions.AllowAny]
