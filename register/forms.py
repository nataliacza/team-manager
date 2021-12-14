from django import forms

from register.models import Member, Dog, Equipment, EquipmentCategory


class MemberForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = "__all__"


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
