# Generated by Django 3.2.9 on 2022-02-19 19:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0017_auto_20220219_2040'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='dog_guide_course',
            field=models.CharField(blank=True, choices=[('NIE', 'Nie'), ('TAK', 'Tak')], default='NIE', max_length=3, null=True, verbose_name='Kurs Przewodników'),
        ),
        migrations.AlterField(
            model_name='member',
            name='kpp_course',
            field=models.CharField(blank=True, choices=[('NIE', 'Nie'), ('TAK', 'Tak')], default='NIE', max_length=3, null=True, verbose_name='KPP'),
        ),
        migrations.AlterField(
            model_name='member',
            name='medical_exam',
            field=models.CharField(blank=True, choices=[('NIE', 'Nie'), ('TAK', 'Tak')], default='NIE', max_length=3, null=True, verbose_name='Badania Lekarskie'),
        ),
        migrations.AlterField(
            model_name='member',
            name='osp_course',
            field=models.CharField(blank=True, choices=[('NIE', 'Nie'), ('TAK', 'Tak')], default='NIE', max_length=3, null=True, verbose_name='Kurs OSP'),
        ),
    ]
