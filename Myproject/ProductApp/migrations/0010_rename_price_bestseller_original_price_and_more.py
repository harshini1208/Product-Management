# Generated by Django 5.0.1 on 2024-01-31 06:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ProductApp', '0009_remove_product_disount_per_product_discount_per_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bestseller',
            old_name='price',
            new_name='original_price',
        ),
        migrations.RemoveField(
            model_name='bestseller',
            name='id',
        ),
        migrations.AddField(
            model_name='bestseller',
            name='discount_per',
            field=models.CharField(default=0),
        ),
        migrations.AddField(
            model_name='bestseller',
            name='new_price',
            field=models.CharField(default=0, max_length=100),
        ),
        migrations.AlterField(
            model_name='bestseller',
            name='pcode',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='bestseller',
            name='prod_count',
            field=models.CharField(default=0),
        ),
    ]
