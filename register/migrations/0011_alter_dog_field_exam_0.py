# Generated by Django 3.2.9 on 2022-02-19 18:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0010_auto_20220219_1922'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dog',
            name='field_exam_0',
            field=models.CharField(blank=True, choices=[('NIE', 'Nie'), ('TAK', 'Tak')], default='Nie', max_length=3, null=True, verbose_name='Egzamin teren 0'),
        ),
    ]