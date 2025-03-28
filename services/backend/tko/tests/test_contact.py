import pytest
from rest_framework.test import APIClient
from django.urls import reverse

from tko.tests.factories import ContactFactory


# Create your tests here.
@pytest.mark.django_db(transaction=True)
class TestContact:
    url = reverse("create-contact")
    client = APIClient()

    @pytest.mark.parametrize(
        ("name", "email", "phone", "message", "result"),
    [
        ("name", "email@tko.cz", "770707505", "message", 200),
        ("name", "email@tko.cz", "", "message", 400),
        ("name", "", "770707505", "message", 400),
        ("name", "", "", "message", 400),
        ("name ahoj", "email@tko.cz", "+420770707505", "message skdo nsdkl skd sakdksd", 200),
        ("", "email", "770707505", "message", 400),
    ])
    def test_create_contact(self, name, email, phone, message, result):
        response = self.client.post(
            path=self.url,
            data={
                "name": name,
                "email": email,
                "phone_number": phone,
                "content": message,
            }
        )
        assert response.status_code == result
        if result == 200:
            assert str(ContactFactory(
                name=name,
                email=email,
                phone_number=phone,
            )) == f"{name}, {email}, {phone}"