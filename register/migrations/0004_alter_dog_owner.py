# Generated by Django 3.2.9 on 2022-02-17 17:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0003_auto_20220210_2234'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dog',
            name='owner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='dogs', to='register.member', verbose_name='Właściciel'),
        ),
    ]
