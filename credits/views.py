from django.views.generic.list import ListView

from credits.models import Contributor


class ContributorListView(ListView):
    template_name = 'credits/credit_receivers_list.html'
    context_object_name = 'contributors'

    def get_queryset(self):
        return Contributor.objects.all().order_by('?')
