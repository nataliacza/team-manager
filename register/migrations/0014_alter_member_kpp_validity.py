# Generated by Django 3.2.9 on 2022-02-19 19:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0013_auto_20220219_1925'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='kpp_validity',
            field=models.DateField(null=True, verbose_name='Termin ważności KPP'),
        ),
    ]
