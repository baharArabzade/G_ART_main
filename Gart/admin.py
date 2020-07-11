from django.contrib import admin
from .models import Studio_item,Tutorial_item, Collection_item, Event_item ,Studio_Photo

admin.site.register(Studio_item)
admin.site.register(Tutorial_item)
admin.site.register(Collection_item)
admin.site.register(Event_item)
admin.site.register(Studio_Photo)