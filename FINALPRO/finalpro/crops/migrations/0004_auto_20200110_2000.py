# Generated by Django 3.0.2 on 2020-01-10 14:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crops', '0003_auto_20200110_1841'),
    ]

    operations = [
        migrations.CreateModel(
            name='inputCrops',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('region', models.CharField(max_length=10)),
                ('subregion', models.CharField(max_length=100)),
                ('soil', models.CharField(max_length=100)),
            ],
        ),
        migrations.RenameField(
            model_name='farmer',
            old_name='phone',
            new_name='contact',
        ),
        migrations.RenameField(
            model_name='farmer',
            old_name='last_name',
            new_name='firstname',
        ),
        migrations.RenameField(
            model_name='farmer',
            old_name='name',
            new_name='lastname',
        ),
        migrations.AddField(
            model_name='farmer',
            name='username',
            field=models.CharField(default='', max_length=100),
        ),
    ]
