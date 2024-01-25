from django.contrib import admin

from .models import News  ,Journal, Team,Research,Category,EventImage , Infrastructure


admin.site.register(News)
admin.site.register(Journal)


admin.site.register(Team)
admin.site.register(Research)

admin.site.register(Category)
admin.site.register(EventImage)
admin.site.register(Infrastructure)


# Register your models here.
