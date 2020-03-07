# Generated by Django 3.0.3 on 2020-03-07 16:21

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('property', '0021_auto_20200301_2042'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flat',
            name='likes',
            field=models.ManyToManyField(blank=True, default=None, to=settings.AUTH_USER_MODEL, verbose_name='Кто лайкнул'),
        ),
    ]
