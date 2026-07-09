from django.test import TestCase
import pytest
from django.test import Client


@pytest.mark.django_db
def test_weather_endpoint_returns_200():
    client = Client()

    response = client.get("/api/weather/?city=Copenhagen")

    assert response.status_code == 200
    assert response.json()["city"] == "Copenhagen"
    assert "temperature" in response.json()
