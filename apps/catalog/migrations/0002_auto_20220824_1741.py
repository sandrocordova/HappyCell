# Generated by Django 3.2.14 on 2022-08-24 22:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TipoClase',
            fields=[
                ('CLIE_TIPO', models.CharField(max_length=2, primary_key=True, serialize=False)),
                ('DESC_TIPO', models.CharField(max_length=50, null=True)),
            ],
            options={
                'db_table': 'TIPO_CLASE',
            },
        ),
        migrations.RenameField(
            model_name='tiporol',
            old_name='TIROL_DESCRIPCIÒN',
            new_name='TIROL_DESCRIPCION',
        ),
    ]
