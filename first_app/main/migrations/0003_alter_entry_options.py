# Generated by Django 4.2.5 on 2023-10-11 16:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_entry'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='entry',
            options={'verbose_name_plural': 'entries'},
        ),
    ]