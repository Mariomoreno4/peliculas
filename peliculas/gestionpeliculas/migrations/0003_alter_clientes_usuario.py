# Generated by Django 4.2.5 on 2023-10-07 02:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestionpeliculas', '0002_libros_alter_clientes_password'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clientes',
            name='usuario',
            field=models.CharField(max_length=100),
        ),
    ]
