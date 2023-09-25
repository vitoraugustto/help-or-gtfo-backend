# Generated by Django 4.2.4 on 2023-09-24 21:38

from django.db import migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('rundown', '0008_alter_expedition_sectors'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expedition',
            name='sectors',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('main', 'Main'), ('secondary', 'Secondary'), ('overload', 'Overload')], default='main', max_length=23, verbose_name='Sectors'),
        ),
    ]
