# Generated by Django 4.2.9 on 2024-06-18 13:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0011_rename_type_company_comp_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='survey_answers',
            name='placeholder',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
    ]
