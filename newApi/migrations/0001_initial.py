# Generated by Django 4.2.6 on 2023-10-31 02:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
                ('number', models.IntegerField(max_length=10)),
                ('address', models.CharField(max_length=20)),
            ],
        ),
    ]