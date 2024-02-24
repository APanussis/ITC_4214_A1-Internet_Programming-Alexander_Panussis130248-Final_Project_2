# Generated by Django 4.2.7 on 2024-02-23 05:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ItemsApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ModelCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sourceCategory', models.CharField(max_length=20)),
            ],
            options={
                'ordering': ['sourceCategory'],
            },
        ),
        migrations.CreateModel(
            name='ModelManufacturer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sourceManufacturer', models.CharField(max_length=30)),
            ],
            options={
                'ordering': ['sourceManufacturer'],
            },
        ),
        migrations.RemoveField(
            model_name='modelproduct',
            name='category',
        ),
        migrations.RemoveField(
            model_name='modelproduct',
            name='manufacturer',
        ),
        migrations.AddField(
            model_name='modelproduct',
            name='category',
            field=models.ManyToManyField(to='ItemsApp.modelcategory'),
        ),
        migrations.AddField(
            model_name='modelproduct',
            name='manufacturer',
            field=models.ManyToManyField(to='ItemsApp.modelmanufacturer'),
        ),
    ]