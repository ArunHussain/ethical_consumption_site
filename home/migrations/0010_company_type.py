# Generated by Django 4.2.9 on 2024-06-14 08:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_remove_company_supports_israel_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='type',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]
