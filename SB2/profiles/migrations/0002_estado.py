# Generated by Django 4.1.3 on 2022-12-12 20:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Estado',
            fields=[
                ('nombre_usuario', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('dinero', models.IntegerField()),
                ('numero_cuenta', models.IntegerField()),
            ],
        ),
    ]
