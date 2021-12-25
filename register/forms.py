from django import forms
from django.forms import TextInput, FileInput, Select, EmailInput, SelectMultiple

from register.models import Member, Dog, Equipment, EquipmentCategory


class MemberForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = ["member_image", "member_name", "member_surname", "member_mobile", "member_email", "kpp_course",
                  "medical_exam", "dog_guide_course", "osp_course", "owned_dog"]
        widgets = {
            "member_image": FileInput(),
            "member_name": TextInput(),
            "member_surname": TextInput(),
            "member_mobile": TextInput(),
            "member_email": EmailInput(),
            "kpp_course": Select(),
            "medical_exam": Select(),
            "dog_guide_course": Select(),
            "osp_course": Select(),
            "owned_dog": SelectMultiple(),
        }


class DogForm(forms.ModelForm):
    class Meta:
        model = Dog
        fields = "__all__"


class EquipmentForm(forms.ModelForm):
    class Meta:
        model = Equipment
        fields = "__all__"


class EquipmentCategoryForm(forms.ModelForm):
    class Meta:
        model = EquipmentCategory
        fields = "__all__"
