import pytest
from rest_framework.test import APIClient
from django.urls import reverse

from tko.tests.factories import ArticleFactory


@pytest.mark.django_db(transaction=True)
class TestLoadArticle:
    client = APIClient()

    @staticmethod
    def create_article(old, new):
        for _ in range(new): ArticleFactory(active_to=None)
        for _ in range(old): ArticleFactory()

    @pytest.mark.parametrize(
        ("articles", "length", "result"),
        [
            ((2, 5), 2, 200),
            ((2, 1), 1, 200),
            ((5, 0), 0, 200),
            ((3, 1), 1, 200),
        ]
    )
    def test_load_articles(self, articles, length, result):
        self.create_article(*articles)
        response = self.client.get(reverse("load-articles"))
        assert response.status_code == result
        assert len(response.data) == length


    @pytest.mark.parametrize(
        ("articles", "length", "result"),
        [
            ((2, 5), 5, 200),
            ((2, 1), 1, 200),
            ((5, 0), 0, 200),
            ((3, 1), 1, 200),
        ]
    )
    def test_load_all_articles(self, articles, length, result):
        self.create_article(*articles)
        response = self.client.get(
            path=reverse("load-all-articles")
        )
        assert response.status_code == result
        assert len(response.data) == length


    def test_str_article(self):
        title = "Test_article"
        assert str(ArticleFactory(title=title)) == title