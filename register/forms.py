from django import forms
from django.forms import (TextInput, FileInput, Select, EmailInput, SelectMultiple, DateInput, NumberInput,
                          Textarea,)

from register.models import Member, Dog, Fleet, Equipment, EquipmentCategory


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


class FleetForm(forms.ModelForm):
    class Meta:
        model = Fleet
        fields = ["brand_name", "brand_model", "year", "fuel", "last_service_date", "mileage", "max_passengers",
                  "max_dogs", "additional_notes"]
        widgets = {
            "brand_name": TextInput(),
            "brand_model": TextInput(),
            "year": NumberInput(),
            "fuel": Select(),
            "last_service_date": DateInput(),
            "mileage": NumberInput(),
            "max_passengers": NumberInput(),
            "additional_notes": Textarea(),
        }


class EquipmentForm(forms.ModelForm):
    class Meta:
        model = Equipment
        fields = "__all__"


class EquipmentCategoryForm(forms.ModelForm):
    class Meta:
        model = EquipmentCategory
        fields = "__all__"
