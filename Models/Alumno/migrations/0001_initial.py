# Generated by Django 3.0.8 on 2020-07-27 17:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Alumno',
            fields=[
                ('id_alumno', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=45)),
                ('apellido', models.CharField(max_length=45)),
                ('dpi', models.CharField(max_length=13, unique=True)),
                ('telefono', models.CharField(max_length=10)),
                ('correo', models.CharField(max_length=125)),
            ],
        ),
    ]
