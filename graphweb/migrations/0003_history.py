# Generated by Django 2.1.1 on 2019-03-15 04:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('graphweb', '0002_auto_20190313_1835'),
    ]

    operations = [
        migrations.CreateModel(
            name='History',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datetime_data', models.DateField(default='7777-01-01')),
                ('datetime_trans', models.DateField(default='7777-01-01')),
                ('author', models.CharField(default='default', max_length=50)),
                ('filename', models.CharField(default='default', max_length=50)),
            ],
        ),
    ]