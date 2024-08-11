# Generated by Django 4.2.9 on 2024-06-13 13:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_company_news1source_company_news2source_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='comments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=150)),
                ('body', models.CharField(max_length=400)),
                ('upvotes', models.IntegerField()),
                ('downvotes', models.IntegerField()),
                ('date', models.DateField()),
            ],
        ),
    ]
