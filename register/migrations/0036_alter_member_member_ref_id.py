# Generated by Django 4.0.2 on 2022-02-22 13:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0035_member_member_ref_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='member_ref_id',
            field=models.CharField(blank=True, editable=False, max_length=4, null=True, unique=True, verbose_name='RefID'),
        ),
    ]
