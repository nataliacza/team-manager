# Generated by Django 4.0.2 on 2022-02-22 13:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0036_alter_member_member_ref_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='member',
            name='member_ref_id',
        ),
    ]