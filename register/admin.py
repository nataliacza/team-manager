from django.contrib import admin
from register.models import Dog, Equipment, EquipmentCategory, Fleet, Member

admin.site.register(Dog)
admin.site.register(Member)
admin.site.register(Fleet)
admin.site.register(Equipment)
admin.site.register(EquipmentCategory)
