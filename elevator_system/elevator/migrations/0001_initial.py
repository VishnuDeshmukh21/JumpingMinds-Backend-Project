# Generated by Django 4.2.1 on 2023-12-07 18:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Request',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('floor', models.IntegerField()),
                ('direction', models.CharField(choices=[('up', 'Up'), ('down', 'Down')], max_length=5)),
                ('served', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Elevator',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('operational', models.BooleanField(default=True)),
                ('in_maintenance', models.BooleanField(default=False)),
                ('current_floor', models.IntegerField(default=1)),
                ('moving_up', models.BooleanField(default=False)),
                ('requests', models.ManyToManyField(related_name='elevators', to='elevator.request')),
            ],
        ),
    ]
