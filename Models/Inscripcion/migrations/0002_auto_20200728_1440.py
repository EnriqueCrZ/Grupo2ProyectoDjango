# Generated by Django 3.0.8 on 2020-07-28 20:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Inscripcion', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inscripcion',
            name='usuario_id_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
