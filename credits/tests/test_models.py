from django_dynamic_fixture import G

from django.test import TestCase

from credits.constants import DEFAULT_CREDIT_RECEIVER_PHOTO
from credits.models import Contributor


class TestContributorModel(TestCase):
    def test_photo_url_not_set(self):
        """
        Expect default photo url to be returned if no photo is set
        :return:
        """
        credit_receiver = G(Contributor, photo_url=None)
        self.assertEqual(credit_receiver.photo_url, DEFAULT_CREDIT_RECEIVER_PHOTO)
