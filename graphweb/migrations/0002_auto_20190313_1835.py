# Generated by Django 2.1.1 on 2019-03-13 11:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('graphweb', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='data',
            name='datetime',
            field=models.DateField(default='2019-03-13'),
        ),
    ]