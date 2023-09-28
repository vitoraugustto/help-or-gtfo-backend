# Generated by Django 4.2.4 on 2023-09-28 02:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rundown', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='expedition',
            name='main_sector',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='expedition',
            name='overload_sector',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='expedition',
            name='secondary_sector',
            field=models.BooleanField(default=False),
        ),
    ]
