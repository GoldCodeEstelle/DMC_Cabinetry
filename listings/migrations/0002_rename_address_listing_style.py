# Generated by Django 4.0.1 on 2022-01-17 02:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='listing',
            old_name='address',
            new_name='style',
        ),
    ]
