from django.contrib.auth import get_user_model
from django.test import TestCase

from taxi.models import Manufacturer, Car


class ModelsTests(TestCase):
    def test_manufacturer_str(self):
        format_ = Manufacturer.objects.create(name="Test", country="Universe")
        self.assertEqual(str(format_), f"{format_.name} - {format_.country}")

    def test_driver_str(self):
        driver = get_user_model().objects.create_user(
            username="Test",
            password="T123456",
            first_name="Test first",
            last_name="Test last"
        )
        self.assertEqual(str(driver),
                         f"{driver.username} "
                         f"({driver.first_name} {driver.last_name})")

    def test_car_str(self):
        manufacturer = \
            Manufacturer.objects.create(name="Test", country="Universe")
        car = Car.objects.create(
            model="Test Model",
            manufacturer=manufacturer,
            year=2022,
            color="Test color",
        )
        self.assertEqual(str(car), car.model)

    def test_create_driver_with_license_number(self):
        username = "Test"
        password = "T123456"
        license_number = "DMV12345"
        driver = get_user_model().objects.create_user(
            username=username,
            password=password,
            license_number=license_number
        )
        self.assertEqual(driver.username, username)
        self.assertTrue(driver.check_password(password))
        self.assertEqual(driver.license_number, license_number)
