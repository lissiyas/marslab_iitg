from django.contrib import admin

from .models import News  ,Journal, Team,Research,Category,EventImage


admin.site.register(News)
admin.site.register(Journal)


admin.site.register(Team)
admin.site.register(Research)

admin.site.register(Category)
admin.site.register(EventImage)


# Register your models here.
