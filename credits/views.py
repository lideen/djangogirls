from django.views.generic.list import ListView

from credits.models import CreditReceiver


class CreditReceiversView(ListView):
    template_name = 'credits/credit_receivers_list.html'
    context_object_name = 'credits'

    def get_queryset(self):
        return CreditReceiver.objects.all().order_by('?')
