from django.contrib import admin

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
        return qs[:1]

admin.site.register(About, AboutAdminModel)
