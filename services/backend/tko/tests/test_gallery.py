import datetime

import pytest
from rest_framework.test import APIClient
from django.urls import reverse

from tko.tests.factories import GalleryFactory, ArticleFactory


# Create your tests here.
@pytest.mark.django_db(transaction=True)
class TestGallery:
    url = reverse("load-gallery")
    client = APIClient()


    @staticmethod
    def create_images(old, new):
        for _ in range(new):
            article = ArticleFactory(active_to=None)
            for _ in range(new): GalleryFactory(article=article)
        for _ in range(old):
            article = ArticleFactory()
            for _ in range(old): GalleryFactory(article=article)


    @pytest.mark.parametrize(
        ("gallery", "length", "result"),
        [
            ((2, 5), 29, 200),
            ((2, 1), 5, 200),
            ((4, 2), 20, 200),
            ((3, 1), 10, 200),
        ]
    )
    def test_load_gallery(self, gallery, length, result):
        self.create_images(*gallery)
        response = self.client.get(self.url)
        assert response.status_code == result
        assert len(response.data) == length


    @pytest.mark.parametrize(
        ("gallery", "length", "result"),
        [
            ((2, 5), 5, 200),
            ((2, 1), 1, 200),
            ((4, 0), 0, 200),
            ((3, 1), 1, 200),
        ]
    )
    def test_load_article_images(self, gallery, length, result):
        old, new = gallery
        self.create_images(*gallery)
        response = self.client.get(reverse("load-articles"))
        for article in response.data:
            assert len(article["images"]) == new
        assert response.status_code == result


    def test_str_article_image(self):
        title = "Test_article"
        assert str(
            GalleryFactory(article=ArticleFactory(title=title))
        ) == f"Image for {title}, {datetime.date.today()}"
