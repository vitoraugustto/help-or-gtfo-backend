# Generated by Django 4.2.4 on 2023-09-21 02:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rundown', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='expedition',
            name='display_name',
            field=models.CharField(max_length=4, null=True, verbose_name='Display name'),
        ),
    ]