# Generated by Django 3.1.14 on 2023-07-14 06:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pictures',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='Название')),
                ('pictures', models.ImageField(upload_to='photos/%Y/%n/%d', verbose_name='Картинка')),
            ],
            options={
                'verbose_name': 'Картинка',
                'verbose_name_plural': 'Картинки',
            },
        ),
        migrations.CreateModel(
            name='Program',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='Имя программы')),
                ('program', models.TextField(verbose_name='Программа')),
            ],
            options={
                'verbose_name': 'Программа',
                'verbose_name_plural': 'Программы',
            },
        ),
    ]
