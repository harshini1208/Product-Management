# Generated by Django 5.0.1 on 2024-01-11 06:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ProductApp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='productdiscount',
            old_name='pname',
            new_name='prodname',
        ),
    ]