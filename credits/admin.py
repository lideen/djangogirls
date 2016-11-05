from django.contrib import admin

from credits.models import CreditReceiver, Credit


class CreditReceiverAdmin(admin.ModelAdmin):
    pass


class CreditAdmin(admin.ModelAdmin):
    pass

admin.site.register(CreditReceiver, CreditReceiverAdmin)
admin.site.register(Credit, CreditAdmin)
