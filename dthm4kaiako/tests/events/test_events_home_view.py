from tests.BaseTestWithDB import BaseTestWithDB
from django.urls import reverse
from http import HTTPStatus
from django.test.utils import override_settings


class HomeViewTest(BaseTestWithDB):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.language = "en"

    @override_settings(GOOGLE_MAPS_API_KEY="mocked")
    def test_home_view_success_response(self):
        response = self.client.get(reverse("events:home"))
        self.assertEqual(HTTPStatus.OK, response.status_code)
        self.assertContains(response, "Events")
