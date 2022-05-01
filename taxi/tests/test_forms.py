from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from taxi.forms import DriverCreationForm
from taxi.models import Manufacturer


class FormsTest(TestCase):
    def test_driver_creation_form(self):
        form_data = {
            "username": "new_user",
            "license_number": "AAA12345",
            "first_name": "Test first",
            "last_name": "Test last",
            "password1": "Test12345",
            "password2": "Test12345"
        }
        form = DriverCreationForm(data=form_data)
        self.assertTrue(form.is_valid())
        self.assertEqual(form.cleaned_data, form_data)


class PrivateDriverTests(TestCase):
    def setUp(self) -> None:
        self.user = get_user_model().objects.create_user(
            "test",
            "Test12345"
        )
        self.client.force_login(self.user)

    def test_create_driver(self):
        form_data = {
            "username": "new_user",
            "license_number": "AAA12345",
            "first_name": "Test first",
            "last_name": "Test last",
            "password1": "Test12345",
            "password2": "Test12345"
        }
        self.client.post(reverse("taxi:driver-create"), data=form_data)
        new_user = get_user_model().objects.get(username=form_data["username"])

        self.assertEqual(new_user.first_name, form_data["first_name"])
        self.assertEqual(new_user.last_name, form_data["last_name"])
        self.assertEqual(new_user.license_number, form_data["license_number"])

    def test_create_manufacturer(self):
        form_data = {
            "name": "Test",
            "country": "Universe"
        }
        self.client.post(reverse("taxi:manufacturer-create"), data=form_data)
        new_manufacturer = Manufacturer.objects.get(name=form_data["name"])

        self.assertEqual(new_manufacturer.name, form_data["name"])
        self.assertEqual(new_manufacturer.country, form_data["country"])
