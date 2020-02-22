# Generated by Django 3.0.3 on 2020-02-20 16:30

from django.db import migrations

def is_new_building(apps, schema_editor):
    Flat = apps.get_model('property', 'Flat')
    for flat in Flat.objects.all():
        flat.new_building = flat.construction_year >= 2015
        flat.save()


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0004_auto_20200220_1007'),
    ]

    operations = [
        migrations.RunPython(is_new_building)
    ]
