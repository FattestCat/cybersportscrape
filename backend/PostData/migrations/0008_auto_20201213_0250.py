# Generated by Django 3.1.2 on 2020-12-13 02:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PostData', '0007_word_tags'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='word',
            options={'ordering': ['-count']},
        ),
        migrations.CreateModel(
            name='CleanWord',
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
