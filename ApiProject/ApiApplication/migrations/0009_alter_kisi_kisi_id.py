# Generated by Django 4.2.3 on 2023-07-11 11:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ApiApplication', '0008_remove_kisi_kisi_sirket_kisi_sirketler'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kisi',
            name='kisi_id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]