from django_dynamic_fixture import G

from django.test import TestCase
from mock import patch

from credits.constants import DEFAULT_CREDIT_RECEIVER_PHOTO
from credits.models import Contributor


class TestContributorModel(TestCase):
    @patch('credits.models.has_gravatar')
    @patch('credits.models.get_gravatar_url')
    def test_photo_url_if_email_is_set(self, get_gravatar_url_mock, has_gravatar_mock):
        """
        Here we expect that the gravatar url is used if a user have an email set
        :param get_gravatar_url_mock: mock of the get_gravatal_url function (third-party)
        :param has_gravatar_mock: mock of the has_gravatar_mock function (third-party)
        :return:
        """
        has_gravatar_mock.return_value = True
        get_gravatar_url_mock.return_value = 'https://mock.url'
        contributor = G(Contributor, email='django@girl.org')
        self.assertEqual(contributor.photo_url, 'https://mock.url')
        self.assertEqual(has_gravatar_mock.call_count, 1)
        self.assertEqual(get_gravatar_url_mock.call_count, 1)

    def test_photo_url_not_set(self):
        """
        Expect default photo url to be returned if no photo is set
        :return:
        """
        contributor = G(Contributor, photo_url=None, email=None)
        self.assertEqual(contributor.photo_url, DEFAULT_CREDIT_RECEIVER_PHOTO)
