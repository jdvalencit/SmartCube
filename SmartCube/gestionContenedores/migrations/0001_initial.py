# Generated by Django 4.0.2 on 2022-03-03 00:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='contenedor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.BooleanField()),
                ('tipo', models.CharField(max_length=50)),
                ('organizacion', models.CharField(max_length=50)),
            ],
        ),
    ]
