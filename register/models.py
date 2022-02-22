from sys import getsizeof
from datetime import date

from django.db import models
from django.utils.text import slugify

from django.core.exceptions import ValidationError
from django.core.validators import (MinLengthValidator,
                                    validate_image_file_extension,
                                    EmailValidator,
                                    MinValueValidator,
                                    MaxValueValidator)


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


def current_year():
    return date.today().year


def validate_min_value_year_200(value):
    return MinValueValidator(current_year() - 200)(value)


GENDER_CHOICES = (
    ("Suka", "Suka"),
    ("Pies", "Pies"),
)

NO_YES_CHOICES = (
    ("NIE", "Nie"),
    ("TAK", "Tak"),
)

FUEL_CHOICES = (
    ("Benzyna", "Benzyna"),
    ("Diesel", "Diesel"),
    ("Inne", "Inne"),
)


class Member(models.Model):
    member_name = models.CharField(max_length=20, null=False, blank=False, verbose_name="Imię",
                                   validators=[MinLengthValidator(2), validate_isalphabet])
    member_surname = models.CharField(max_length=20, null=False, blank=False, verbose_name="Nazwisko",
                                      validators=[MinLengthValidator(2), validate_isalphabet])
    slug = models.SlugField(unique=True, null=False, blank=False, db_index=True)
    member_image = models.ImageField(upload_to="members/", null=True, blank=True, max_length=100,
                                     height_field=None, width_field=None, verbose_name="Zdjęcie",
                                     validators=[validate_image_file_extension, validate_file_size_3MB])
    member_mobile = models.IntegerField(null=True, blank=True, verbose_name="Kontakt")
    member_email = models.EmailField(null=True, blank=True, verbose_name="Email",
                                     validators=[MinLengthValidator(6), EmailValidator])
    kpp_course = models.CharField(max_length=3, null=True, blank=True, choices=NO_YES_CHOICES,
                                  verbose_name="KPP")
    kpp_validity = models.DateField(null=True, blank=True, default=None, verbose_name="Termin ważności KPP")
    medical_exam = models.CharField(max_length=3, null=True, blank=True, choices=NO_YES_CHOICES,
                                    verbose_name="Badania Lekarskie")
    medical_exam_validity = models.DateField(null=True, blank=True, default=None, verbose_name="Termin ważności badań")
    dog_guide_course = models.CharField(max_length=3, null=True, blank=True, choices=NO_YES_CHOICES,
                                        verbose_name="Kurs Przewodników")
    osp_course = models.CharField(max_length=3, null=True, blank=True, choices=NO_YES_CHOICES,
                                  verbose_name="Kurs OSP")

    def save(self, *args, **kwargs):
        super(Member, self).save(*args, **kwargs)
        if not self.slug:
            slug = slugify(f"{self.member_name}-{self.member_surname}")
            try:
                member_obj = Member.objects.get(slug=slug)
                slug += "-" + str(member_obj.id)
            except Member.DoesNotExist:
                pass
            self.slug = slug
            self.save()

    class Meta:
        verbose_name_plural = "Lista członków"

    def get_full_name(self):
        return f"{self.member_name} {self.member_surname}"

    def __str__(self):
        return self.get_full_name()


class Dog(models.Model):
    dog_name = models.CharField(max_length=50, null=False, blank=False, verbose_name="Imię",
                                validators=[MinLengthValidator(3), validate_isalphabet])
    slug = models.SlugField(unique=True, null=False, blank=False, db_index=True)
    dog_image = models.ImageField(upload_to="dogs/", null=True, blank=True, max_length=100,
                                  height_field=None, width_field=None, verbose_name="Zdjęcie",
                                  validators=[validate_image_file_extension, validate_file_size_3MB])
    breeder = models.CharField(max_length=50, null=True, blank=True, verbose_name="Hodowla",
                               validators=[MinLengthValidator(3), validate_isalphabet])
    gender = models.CharField(max_length=4, choices=GENDER_CHOICES, null=False, blank=False, verbose_name="Płeć")
    day_of_birth = models.DateField(null=False, blank=False, verbose_name="Data urodzenia",
                                    validators=[validate_future_date])
    chip_number = models.CharField(max_length=20, null=True, blank=True, verbose_name="Numer chipa",
                                   validators=[MinLengthValidator(4)])
    field_exam_0 = models.CharField(max_length=3, null=True, blank=True, choices=NO_YES_CHOICES,
                                    verbose_name="Egzamin teren 0")
    field_exam_1 = models.CharField(max_length=3, null=True, blank=True, choices=NO_YES_CHOICES,
                                    verbose_name="Egzamin teren 1")
    ruins_exam_0 = models.CharField(max_length=3, null=True, blank=True, choices=NO_YES_CHOICES,
                                    verbose_name="Egzamin gruzy 0")
    ruins_exam_1 = models.CharField(max_length=3, null=True, blank=True, choices=NO_YES_CHOICES,
                                    verbose_name="Egzamin gruzy 1")
    owner = models.ForeignKey("Member", on_delete=models.SET_NULL, null=True, blank=True, related_name="dogs",
                              verbose_name="Właściciel")

    def save(self, *args, **kwargs):
        super(Dog, self).save(*args, **kwargs)
        if not self.slug:
            slug = slugify(self.dog_name)
            try:
                dog_obj = Dog.objects.get(slug=slug)
                slug += "-" + str(dog_obj.id)
            except Dog.DoesNotExist:
                pass
            self.slug = slug
            self.save()

    class Meta:
        verbose_name_plural = "Psy"

    def __str__(self):
        return f"{self.dog_name}"


class EquipmentCategory(models.Model):
    category = models.CharField(max_length=50, null=False, blank=False, unique=True, verbose_name="Kategoria",
                                validators=[validate_isalphabet])

    class Meta:
        verbose_name_plural = "Kategorie sprzętu"

    def __str__(self):
        return f"{self.category}"


class Equipment(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False, verbose_name="Nazwa")
    category = models.ForeignKey("EquipmentCategory", on_delete=models.SET_NULL, null=True, blank=True,
                                 related_name="equipment", verbose_name="Kategoria")
    amount = models.PositiveIntegerField(null=True, blank=True, verbose_name="Ilość",
                                         validators=[MaxValueValidator(999)])
    additional_notes = models.TextField(max_length=500, null=True, blank=True, verbose_name="Uwagi")

    class Meta:
        verbose_name_plural = "Sprzęt"

    def __str__(self):
        return f"{self.name}"


class Fleet(models.Model):
    brand_name = models.CharField(max_length=50, null=False, blank=False, verbose_name="Marka")
    brand_model = models.CharField(max_length=50, null=False, blank=False, verbose_name="Model")
    year = models.PositiveIntegerField(null=False, blank=False, verbose_name="Rok",
                                       validators=[validate_min_value_year_200,
                                                   MaxValueValidator(current_year)])
    fuel = models.CharField(max_length=10, null=True, blank=True, choices=FUEL_CHOICES, verbose_name="Paliwo")
    last_service_date = models.DateField(null=True, blank=True, verbose_name="Data serwisu",
                                         validators=[validate_future_date])
    mileage = models.PositiveIntegerField(null=True, blank=True, verbose_name="Przebieg (km)",
                                          validators=[MaxValueValidator(999999)])
    max_passengers = models.PositiveIntegerField(null=True, blank=True, verbose_name="Ilość osób")
    max_dogs = models.PositiveIntegerField(null=True, blank=True, verbose_name="Ilość psów")
    additional_notes = models.TextField(max_length=150, null=True, blank=True, verbose_name="Uwagi")

    class Meta:
        verbose_name_plural = "Flota"

    def __str__(self):
        return f"{self.brand_name} {self.brand_model} ({self.year})"
