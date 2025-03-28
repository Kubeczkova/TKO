import pytest
from rest_framework.test import APIClient
from django.urls import reverse

from tko.admin import ContactAdmin
from tko.models import Contact
from tko.tests.factories import UserFactory

from django.contrib.admin.sites import site


# Create your tests here.
@pytest.mark.django_db(transaction=True)
class TestAdmin:
    url = reverse("admin:index")
    client = APIClient()

    def test_has_add_permission(self):
        user = UserFactory()
        admin = ContactAdmin(Contact, site)
        request = self.client.get(self.url)
        request.user = user
        assert admin.has_add_permission(request) is False

    def test_has_delete_permission(self):
        user = UserFactory()
        admin = ContactAdmin(Contact, site)
        request = self.client.get(self.url)
        request.user = user
        assert admin.has_delete_permission(request) is False

    def test_has_change_permission(self):
        user = UserFactory()
        admin = ContactAdmin(Contact, site)
        request = self.client.get(self.url)
        request.user = user
        assert admin.has_change_permission(request) is False