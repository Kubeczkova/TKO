import pytest
from rest_framework.test import APIClient
from django.urls import reverse

from tko.tests.factories import EventFactory


# Create your tests here.
@pytest.mark.django_db(transaction=True)
class TestEvent:
    url = reverse("load-events")
    client = APIClient()

    @staticmethod
    def create_events(length):
        EventFactory.create_batch(size=length)

    @pytest.mark.parametrize(
        ("length", "result"),
        [
            (2, 200),
            (6, 200),
        ]
    )
    def test_load_events(self, length, result):
        self.create_events(length)
        response = self.client.get(self.url)
        assert response.status_code == result
        assert len(response.data) == length


    def test_str_article_image(self):
        title = "Test_event"
        assert str(
            EventFactory(title=title)
        ) == title
