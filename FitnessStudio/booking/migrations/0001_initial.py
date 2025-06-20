# Generated by Django 5.1.4 on 2025-06-06 16:18

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Fitness',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('instructor', models.CharField(max_length=50)),
                ('start_date', models.DateTimeField()),
                ('available_slot', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client_name', models.CharField(max_length=50)),
                ('client_email', models.EmailField(max_length=254)),
                ('booked_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('fitness_class', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='booking.fitness')),
            ],
        ),
    ]
