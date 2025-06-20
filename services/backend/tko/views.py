from django.utils import timezone
from django.db.models import Q, Prefetch

from post_office import mail

from rest_framework.generics import ListAPIView, CreateAPIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response

from tko.models import Article, Event, ArticleImage
from tko.serializers import ArticleListSerializer, EventListSerializer, ContactSerializer, ArticleImageSerializer


class ContactView(CreateAPIView):
    serializer_class = ContactSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        mail.send(
            recipients="kubeczkova.n@gmail.com",
            subject="Zpráva z webu TKO",
            message=f"Jméno: {serializer.data['name']}\n"
                    f"Email: {serializer.data['email']}\n"
                    f"Telefón: {serializer.data['phone_number']}\n\n"
                    f"Zpráva: {serializer.data['content']}",
        )

        return Response(serializer.data)


class NewArticleListView(ListAPIView):
    serializer_class = ArticleListSerializer

    def get_queryset(self):
        return Article.objects.filter(
            Q(active_to__gte=timezone.now()) | Q(active_to__isnull=True)
        ).order_by('-date')[:2]


class AllArticleListView(ListAPIView):
    serializer_class = ArticleListSerializer

    def get_queryset(self):
        return Article.objects.filter(
            Q(active_to__gte=timezone.now()) | Q(active_to__isnull=True)
        ).order_by('-date').prefetch_related(
            Prefetch('images', queryset=ArticleImage.objects.order_by('-main'))
        )


class GalleryView(ListAPIView):
    permission=[AllowAny]
    queryset = ArticleImage.objects.all().order_by("-article_id", "main")
    serializer_class = ArticleImageSerializer


class EventListView(ListAPIView):
    queryset = Event.objects.all()
    serializer_class = EventListSerializer
