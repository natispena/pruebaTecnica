# Generated by Django 4.0 on 2021-12-29 17:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libreria', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Turnos',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('numero', models.IntegerField()),
                ('hora', models.TimeField()),
                ('estado', models.CharField(max_length=100)),
                ('Usuario', models.CharField(max_length=100)),
            ],
        ),
        migrations.AlterField(
            model_name='usuario',
            name='identificacion',
            field=models.CharField(max_length=100),
        ),
    ]
