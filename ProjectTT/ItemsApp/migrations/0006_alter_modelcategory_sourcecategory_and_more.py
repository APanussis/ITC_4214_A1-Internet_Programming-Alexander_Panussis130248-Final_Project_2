# Generated by Django 4.2.7 on 2024-02-23 12:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ItemsApp', '0005_alter_modelcategory_sourcecategory_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='modelcategory',
            name='sourceCategory',
            field=models.CharField(max_length=20, unique=True),
        ),
        migrations.AlterField(
            model_name='modelmanufacturer',
            name='sourceManufacturer',
            field=models.CharField(max_length=30, unique=True),
        ),
    ]
