from django.contrib.staticfiles.templatetags.staticfiles import static
from django.utils.translation import ugettext as _

DEFAULT_CREDIT_RECEIVER_PHOTO = static('img/global/coach-empty.jpg')

CREDIT_CATEGORY_NONE = ''
CREDIT_CATEGORY_ORGANIZER = 'organiser'
CREDIT_CATEGORY_COACH = 'coach'
CREDIT_CATEGORY_TUTORIAL = 'tutorial'
CREDIT_CATEGORY_CHOICES = (
    (_('-----'), CREDIT_CATEGORY_NONE),
    (_('Organiser'), CREDIT_CATEGORY_ORGANIZER),
    (_('Coach'), CREDIT_CATEGORY_COACH),
    (_('Tutorial'), CREDIT_CATEGORY_TUTORIAL),
)
