# Generated by Django 4.0.3 on 2022-04-02 06:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='test2',
            name='name',
            field=models.CharField(max_length=10, unique=True),
        ),
    ]
