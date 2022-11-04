# Generated by Django 3.2.9 on 2022-02-19 18:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0008_alter_dog_field_exam_0'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dog',
            name='field_exam_0',
            field=models.BooleanField(blank=True, choices=[('TAK', 'Tak'), ('NIE', 'Nie')], default='Nie', null=True, verbose_name='Egzamin teren 0'),
        ),
    ]
