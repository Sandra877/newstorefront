# Generated by Django 5.0.1 on 2024-02-03 22:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120)),
                ('details', models.CharField(max_length=200)),
                ('blogs', models.TextField(max_length=10000)),
            ],
        ),
    ]
