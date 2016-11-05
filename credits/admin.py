from django.contrib import admin

from credits.models import Contributor, Credit


class ContributorAdmin(admin.ModelAdmin):
    pass


class CreditAdmin(admin.ModelAdmin):
    pass

admin.site.register(Contributor, ContributorAdmin)
admin.site.register(Credit, CreditAdmin)
