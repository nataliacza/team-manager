from django.contrib import admin
from register.models import Dog, Equipment, EquipmentCategory, Fleet, Member

class MemberAdmin(admin.ModelAdmin):
    list_filter = ("member_name", "member_surname",)
    list_display = ("id",
                    "member_name",
                    "member_surname",
                    "member_mobile",
                    "member_email",
                    "kpp_course",
                    "kpp_validity",
                    "medical_exam",
                    "medical_exam_validity",
                    "dog_guide_course",
                    "osp_course",)
    prepopulated_fields = {"slug": ("member_name", "member_surname")}


class DogAdmin(admin.ModelAdmin):
    list_filter = ("dog_name", "owner")
    list_display = ("id",
                    "dog_name",
                    "breeder",
                    "gender",
                    "day_of_birth",
                    "chip_number",
                    "field_exam_0",
                    "field_exam_1",
                    "ruins_exam_0",
                    "ruins_exam_1",
                    "owner",)
    prepopulated_fields = {"slug": ("dog_name",)}


admin.site.register(Dog, DogAdmin)
admin.site.register(Member, MemberAdmin)
admin.site.register(Fleet)
admin.site.register(Equipment)
admin.site.register(EquipmentCategory)
