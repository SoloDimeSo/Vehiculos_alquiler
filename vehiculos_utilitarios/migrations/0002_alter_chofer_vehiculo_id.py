# Generated by Django 4.2 on 2024-05-18 02:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vehiculos_utilitarios', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chofer',
            name='vehiculo_id',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='vehiculos_utilitarios.vehiculo'),
        ),
    ]
