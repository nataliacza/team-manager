from django import forms
from django.forms import TextInput, FileInput, Select, EmailInput, SelectMultiple, DateInput

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
        fields = ["dog_image", "dog_name", "breeder", "gender", "day_of_birth", "chip_number",
                  "field_exam_0", "field_exam_1", "ruins_exam_0", "ruins_exam_1", "owner"]
        widgets = {
            "dog_image": FileInput(),
            "dog_name": TextInput(),
            "breeder": TextInput(),
            "gender": Select(),
            "day_of_birth": DateInput(),
            "chip_number": TextInput(),
            "field_exam_0": Select(),
            "field_exam_1": Select(),
            "ruins_exam_0": Select(),
            "ruins_exam_1": Select(),
            "owner": Select(),
        }


class EquipmentForm(forms.ModelForm):
    class Meta:
        model = Equipment
        fields = "__all__"


class EquipmentCategoryForm(forms.ModelForm):
    class Meta:
        model = EquipmentCategory
        fields = "__all__"
