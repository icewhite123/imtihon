# Generated by Django 4.1.4 on 2023-03-01 11:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=30)),
                ('familliya', models.CharField(max_length=20)),
                ('tel', models.CharField(max_length=30)),
            ],
        ),
    ]
