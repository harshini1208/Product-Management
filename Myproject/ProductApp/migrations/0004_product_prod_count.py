# Generated by Django 5.0.1 on 2024-01-12 10:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ProductApp', '0003_alter_product_exp_alter_product_mfd_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='prod_count',
            field=models.IntegerField(default=0),
        ),
    ]