# Generated by Django 3.0.9 on 2020-08-03 22:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Alumno', '0002_auto_20200728_1440'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alumno',
            name='nombre',
            field=models.CharField(max_length=46),
        ),
    ]
