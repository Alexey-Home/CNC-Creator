# Generated by Django 3.1.14 on 2023-07-14 08:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('creatorprogram', '0002_auto_20230714_0923'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pictures',
            name='pictures',
            field=models.ImageField(upload_to='photos/', verbose_name='Картинка'),
        ),
    ]
