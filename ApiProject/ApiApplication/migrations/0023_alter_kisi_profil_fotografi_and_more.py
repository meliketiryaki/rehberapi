# Generated by Django 4.2.3 on 2023-07-14 09:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ApiApplication', '0022_alter_kisi_kisi_tel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kisi',
            name='profil_fotografi',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='sirket',
            name='sirket_profil_fotografi',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
    ]
