# Generated by Django 4.0.4 on 2022-04-26 18:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_banner_productattribut'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ProductAttribut',
            new_name='ProductAttribute',
        ),
    ]