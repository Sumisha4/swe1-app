from django.test import TestCase
from django.urls import reverse


class PollsIndexViewTests(TestCase):
    def test_index_page_loads(self):
        """The polls index renders, with or without questions."""
        response = self.client.get(reverse("polls:index"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No polls are available.")
