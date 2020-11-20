# Generated by Django 3.1.2 on 2020-11-16 21:35

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PostData', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TagsCount',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tagscount', models.JSONField()),
            ],
        ),
        migrations.AlterField(
            model_name='post',
            name='content',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 11, 16, 21, 35, 34, 112036)),
        ),
        migrations.AlterField(
            model_name='post',
            name='tags',
            field=models.TextField(blank=True),
        ),
    ]