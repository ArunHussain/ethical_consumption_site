# Generated by Django 4.2.9 on 2024-06-12 20:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='rating',
            field=models.IntegerField(default=2),
            preserve_default=False,
        ),
    ]
