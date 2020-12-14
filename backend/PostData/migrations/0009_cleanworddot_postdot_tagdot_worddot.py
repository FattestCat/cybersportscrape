# Generated by Django 3.1.2 on 2020-12-14 02:14

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('PostData', '0008_auto_20201213_0250'),
    ]

    operations = [
        migrations.CreateModel(
            name='PostDot',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('content', models.TextField(blank=True)),
                ('date', models.DateTimeField(blank=True, default=django.utils.timezone.now)),
                ('tags', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='TagDot',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='WordDot',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('word', models.CharField(max_length=200)),
                ('count', models.IntegerField(default=0)),
                ('tags', models.ManyToManyField(blank=True, to='PostData.Tag')),
            ],
            options={
                'ordering': ['-count'],
            },
        ),
        migrations.CreateModel(
            name='CleanWordDot',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('word', models.CharField(max_length=200)),
                ('count', models.IntegerField(default=0)),
                ('tags', models.ManyToManyField(blank=True, to='PostData.Tag')),
            ],
            options={
                'ordering': ['-count'],
            },
        ),
    ]
