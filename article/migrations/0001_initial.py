# Generated by Django 4.0.6 on 2022-07-22 06:36

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('content', models.TextField()),
                ('pub_date', models.DateTimeField(verbose_name=datetime.datetime(2022, 7, 22, 6, 36, 42, 295613, tzinfo=utc))),
            ],
        ),
    ]
