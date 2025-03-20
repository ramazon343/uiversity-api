# Generated by Django 5.1.7 on 2025-03-19 16:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=255)),
                ('course', models.IntegerField()),
                ('education_type', models.CharField(choices=[('full_time', 'Full-time'), ('part_time', 'Part-time')], max_length=100)),
                ('birth_date', models.DateField()),
            ],
        ),
    ]
