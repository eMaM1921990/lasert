from django.contrib import admin
from django.contrib.sessions.models import Session

# Register your models here.
from lasertApp.models import *

admin.site.register(Clients)
admin.site.register(Partners)
admin.site.register(SolutionCategory)
admin.site.register(Recommends)
admin.site.register(Solutions)
admin.site.register(Serivces)
admin.site.register(Careers)
admin.site.register(Subscribers)
admin.site.register(Slider)
admin.site.register(Mailer)


class AboutAdminModel(admin.ModelAdmin):
    def queryset(self, request):
        qs = super(AboutAdminModel, self).queryset(request)
        return qs.first()


admin.site.register(About, AboutAdminModel)


class SessionAdmin(admin.ModelAdmin):
    def _session_data(self, obj):
        return obj.get_decoded()

    list_display = ['session_key', '_session_data', 'expire_date']


admin.site.register(Session, SessionAdmin)


class ContactUsAdmin(admin.ModelAdmin):
    def queryset(self, request):
        qs = super(ContactUsAdmin, self).queryset(request)
        return qs.first()


admin.site.register(ContactUs, ContactUsAdmin)
