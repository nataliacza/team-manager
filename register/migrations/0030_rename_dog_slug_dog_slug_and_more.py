# Generated by Django 4.0.2 on 2022-02-20 17:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0029_alter_equipment_category'),
    ]

    operations = [
        migrations.RenameField(
            model_name='dog',
            old_name='dog_slug',
            new_name='slug',
        ),
        migrations.RenameField(
            model_name='member',
            old_name='member_slug',
            new_name='slug',
        ),
    ]
