# Generated by Django 4.1.3 on 2022-12-13 17:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('transaccions', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='transferencias',
            old_name='ingresar_cuenta_destino',
            new_name='ingresar_numero_cuenta_destino',
        ),
    ]
