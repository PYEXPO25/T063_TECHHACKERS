# Generated by Django 5.1.6 on 2025-02-21 12:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CMS', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100, unique=True)),
                ('password', models.CharField(max_length=225)),
            ],
        ),
    ]
