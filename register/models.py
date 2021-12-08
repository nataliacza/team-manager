from sys import getsizeof
from datetime import date
from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator, validate_image_file_extension
from django.db import models


def validate_isalphabet(name):
    if not name.replace(" ", "").isalpha():
        raise ValidationError(f"Niepoprawna wartość '{name}'. Nazwa musi składać się z liter!")


def validate_file_size_3MB(file):
    limit = 3000000
    file_size = getsizeof(file)
    if file_size > limit:
        raise ValidationError(f"Dozwolona wielkość pliku 3 MB.")


def validate_future_date(date_given):
    today_is = date.today()
    if date_given > today_is:
        raise ValidationError("Data nie może być z przyszłości.")


GENDER_CHOICES = (
    ("Suka", "Suka"),
    ("Pies", "Pies"),
)

YES_NO_CHOICES = (
    ("TAK", "Tak"),
    ("NIE", "Nie"),
)


class Member(models.Model):
    member_image = models.ImageField(upload_to="members/", null=True, blank=True, max_length=100, height_field=None,
                                     width_field=None,
                                     validators=[validate_image_file_extension, validate_file_size_3MB])
    member_name = models.CharField(max_length=20, null=False, blank=False,
                                   validators=[MinLengthValidator(2), validate_isalphabet])
    member_surname = models.CharField(max_length=20, null=False, blank=False,
                                      validators=[MinLengthValidator(2), validate_isalphabet])
    member_mobile = models.IntegerField(null=True, blank=True)
    member_email = models.EmailField(null=True, blank=True,
                                     validators=[MinLengthValidator(6)])
    kpp_course = models.CharField(max_length=3, choices=YES_NO_CHOICES, null=True, blank=True)
    medical_exam = models.CharField(max_length=3, choices=YES_NO_CHOICES, null=True, blank=True)
    dog_guide_course = models.CharField(max_length=3, choices=YES_NO_CHOICES, null=True, blank=True)
    osp_course = models.CharField(max_length=3, choices=YES_NO_CHOICES, null=True, blank=True)
    owned_dog = models.ManyToManyField("Dog", null=True, blank=True, related_name="member")

    def get_full_name(self):
        return f"{self.member_name} {self.member_surname}"

    def __str__(self):
        return self.get_full_name()


class Dog(models.Model):
    dog_image = models.ImageField(upload_to="dogs/", null=True, blank=True, max_length=100, height_field=None,
                                  width_field=None,
                                  validators=[validate_image_file_extension, validate_file_size_3MB])
    dog_name = models.CharField(max_length=50, null=False, blank=False,
                                validators=[MinLengthValidator(3), validate_isalphabet])
    breeder = models.CharField(max_length=50, null=True, blank=True,
                               validators=[MinLengthValidator(3), validate_isalphabet])
    gender = models.CharField(max_length=4, choices=GENDER_CHOICES, null=False, blank=False)
    day_of_birth = models.DateField(null=False, blank=False,
                                    validators=[validate_future_date])
    chip_number = models.CharField(max_length=20, null=True, blank=True,
                                   validators=[MinLengthValidator(4)])
    field_exam_0 = models.CharField(max_length=3, choices=YES_NO_CHOICES, null=True, blank=True)
    field_exam_1 = models.CharField(max_length=3, choices=YES_NO_CHOICES, null=True, blank=True)
    ruins_exam_0 = models.CharField(max_length=3, choices=YES_NO_CHOICES, null=True, blank=True)
    ruins_exam_1 = models.CharField(max_length=3, choices=YES_NO_CHOICES, null=True, blank=True)
    owner = models.ForeignKey("Member", null=False, blank=False, on_delete=models.CASCADE, related_name="dog")

    def get_dog_name(self):
        return f"{self.dog_name}"

    def __str__(self):
        return f"{self.dog_name}"


class EquipmentCategory(models.Model):
    category = models.CharField(max_length=50, null=False, blank=False,
                                validators=[validate_isalphabet])

    def get_category_name(self):
        return f"{self.category}"

    def __str__(self):
        return f"{self.category}"


class Equipment(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False,
                            validators=[validate_isalphabet])
    category = models.ForeignKey("EquipmentCategory", null=False, blank=False, on_delete=models.CASCADE,
                                 related_name="equipment")
    purchase_date = models.DateField(null=True, blank=True,
                                     validators=[validate_future_date])
    last_service_date = models.DateField(null=True, blank=True,
                                         validators=[validate_future_date])
    mileage = models.PositiveIntegerField(null=True, blank=True)
    additional_notes = models.TextField(max_length=500, null=True, blank=True)

    def get_equipment_name(self):
        return f"{self.name}"

    def __str__(self):
        return f"{self.name}"
