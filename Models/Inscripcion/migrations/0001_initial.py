# Generated by Django 3.0.8 on 2020-07-27 17:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Alumno', '0001_initial'),
        ('Nivel', '0001_initial'),
        ('Usuario', '0001_initial'),
        ('Sucursal', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Inscripcion',
            fields=[
                ('id_inscripcion', models.AutoField(primary_key=True, serialize=False)),
                ('fecha', models.DateField()),
                ('alumno_id_alumno', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Alumno.Alumno')),
                ('nivel_id_nivel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Nivel.Nivel')),
                ('sucursal_id_sucursal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Sucursal.Sucursal')),
                ('usuario_id_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Usuario.Usuario')),
            ],
        ),
        migrations.CreateModel(
            name='Nota',
            fields=[
                ('id_nota', models.AutoField(primary_key=True, serialize=False)),
                ('fecha', models.DateField()),
                ('inscripcion_id_inscripcion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Inscripcion.Inscripcion')),
            ],
        ),
    ]
