# Generated by Django 4.2.3 on 2023-07-14 08:52

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ApiApplication', '0019_alter_sirket_sirket_tel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sirket',
            name='sirket_tel',
            field=models.CharField(blank=True, max_length=11, null=True, validators=[django.core.validators.MinLengthValidator(11, message='Enter a valid 11-digit phone number.')]),
        ),
    ]