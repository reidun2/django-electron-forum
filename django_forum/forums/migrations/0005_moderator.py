# Generated by Django 5.2 on 2025-04-23 20:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forums', '0004_forum_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Moderator',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=150, unique=True)),
                ('password', models.CharField(max_length=128)),
            ],
        ),
    ]
