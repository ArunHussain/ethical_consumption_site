# Generated by Django 4.2.9 on 2024-06-14 13:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0010_company_type'),
    ]

    operations = [
        migrations.RenameField(
            model_name='company',
            old_name='type',
            new_name='comp_type',
        ),
    ]
