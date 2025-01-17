# Generated by Django 4.2.9 on 2024-06-11 16:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40, unique=True)),
                ('fairtrade', models.BooleanField()),
                ('supports_palestine', models.BooleanField()),
                ('supports_israel', models.BooleanField()),
                ('nochildlabor', models.BooleanField()),
                ('bcorp', models.BooleanField()),
                ('peta', models.BooleanField()),
                ('fsc', models.BooleanField()),
                ('point1', models.CharField(max_length=1000)),
                ('source1', models.CharField(max_length=200)),
                ('point2', models.CharField(blank=True, max_length=1000)),
                ('source2', models.CharField(blank=True, max_length=200)),
                ('point3', models.CharField(blank=True, max_length=1000)),
                ('source3', models.CharField(blank=True, max_length=200)),
                ('point4', models.CharField(blank=True, max_length=1000)),
                ('source4', models.CharField(blank=True, max_length=200)),
                ('point5', models.CharField(blank=True, max_length=1000)),
                ('source5', models.CharField(blank=True, max_length=200)),
                ('point6', models.CharField(blank=True, max_length=1000)),
                ('source6', models.CharField(blank=True, max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='survey_answers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('supports_palestine', models.BooleanField()),
                ('supports_israel', models.BooleanField()),
                ('supports_fairtrade', models.BooleanField()),
                ('supports_nochildlabor', models.BooleanField()),
                ('supports_lowcarbonemissions', models.BooleanField()),
                ('user_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
