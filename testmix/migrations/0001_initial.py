# Generated by Django 4.2.2 on 2023-06-27 16:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('discription', models.CharField(max_length=100)),
                ('content', models.TextField()),
                ('author', models.CharField(max_length=20)),
            ],
        ),
    ]
