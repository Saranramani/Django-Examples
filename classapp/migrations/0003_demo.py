# Generated by Django 4.2.2 on 2023-06-30 07:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classapp', '0002_remove_todoclass_createdon'),
    ]

    operations = [
        migrations.CreateModel(
            name='Demo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
                ('passwosd', models.CharField(max_length=100)),
            ],
        ),
    ]
