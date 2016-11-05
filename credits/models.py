from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from easy_thumbnails.exceptions import InvalidImageFormatError
from easy_thumbnails.files import get_thumbnailer

from core.models import Coach, Sponsor
from credits.constants import DEFAULT_CREDIT_RECEIVER_PHOTO, CREDIT_CATEGORY_CHOICES


@python_2_unicode_compatible
class CreditReceiver(models.Model):
    name = models.CharField(max_length=256, null=False, blank=False)
    photo = models.ImageField(null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    show_email_in_public = models.BooleanField(default=False)
    link = models.CharField(max_length=1024, null=True, blank=True,
                            help_text="Link to the person (twitter or something else)")

    def __str__(self):
        return self.name

    class Meta:
        ordering = ("name",)
        verbose_name_plural = "CreditReceivers"

    @property
    def photo_url(self):
        if self.photo:
            try:
                return get_thumbnailer(self.photo)['credit_receiver'].url
            except InvalidImageFormatError:
                return DEFAULT_CREDIT_RECEIVER_PHOTO
        return DEFAULT_CREDIT_RECEIVER_PHOTO


@python_2_unicode_compatible
class Credit(models.Model):
    receiver = models.ForeignKey(CreditReceiver, null=False, blank=False, related_name='credits')
    credit = models.CharField(max_length=512, null=False, blank=False)
    category = models.CharField(max_length=512, null=False, blank=True, choices=CREDIT_CATEGORY_CHOICES)

    def __str__(self):
        return self.credit

    class Meta:
        ordering = ("credit", "category")
