# Generated by Django 4.2.3 on 2023-07-19 18:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_autos'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Autos',
        ),
    ]