# Generated by Django 3.0.2 on 2020-01-10 13:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crops', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='farmer',
            name='phone',
            field=models.IntegerField(),
        ),
    ]