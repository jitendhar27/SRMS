# Generated by Django 4.2.8 on 2024-01-03 11:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0004_alter_destination_table_hotel'),
    ]

    operations = [
        migrations.CreateModel(
            name='Airport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('code', models.CharField(max_length=3)),
            ],
        ),
        migrations.CreateModel(
            name='Flight',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('airline', models.CharField(max_length=255)),
                ('flight_number', models.CharField(max_length=10)),
                ('departure_date', models.DateTimeField()),
                ('arrival_date', models.DateTimeField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('destination', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='arriving_flights', to='adminapp.airport')),
                ('origin', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='departing_flights', to='adminapp.airport')),
            ],
        ),
    ]
