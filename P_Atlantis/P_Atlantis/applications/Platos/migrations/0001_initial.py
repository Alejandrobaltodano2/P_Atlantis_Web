# Generated by Django 4.2.4 on 2023-11-20 19:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Platos',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_plato', models.CharField(max_length=250, verbose_name='nombre_plato')),
                ('categoria', models.CharField(choices=[('0', 'Criollos'), ('1', 'Ceviches'), ('2', 'Especialidades'), ('3', 'Chicharrones'), ('4', 'Parrillas'), ('5', 'postres'), ('6', 'Gaseosas'), ('7', 'TAPERS')], max_length=1, verbose_name='Categoria')),
                ('imagen', models.ImageField(upload_to='platos')),
                ('precio', models.FloatField(verbose_name='precio')),
            ],
        ),
    ]
