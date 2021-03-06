# Generated by Django 2.0 on 2018-02-23 04:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventario', '0005_equipos1_personas1'),
    ]

    operations = [
        migrations.AddField(
            model_name='equipos1',
            name='modelo',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='equipos1',
            name='serial',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='personas1',
            name='departamento',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='equipos1',
            name='descripcion',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
