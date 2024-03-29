# Generated by Django 3.2.14 on 2022-08-22 18:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ActividadEconomica',
            fields=[
                ('ACTI_CODIGO', models.PositiveIntegerField(primary_key=True, serialize=False)),
                ('ACTI_DESCRIPCION', models.CharField(max_length=40)),
            ],
            options={
                'db_table': 'ACTIVIDAD_ECONOMICA',
            },
        ),
        migrations.CreateModel(
            name='Agencia',
            fields=[
                ('ZONA_CODIGO', models.PositiveIntegerField()),
                ('EMPR_CODIGO', models.PositiveIntegerField()),
                ('AGEN_CODIGO', models.PositiveIntegerField(primary_key=True, serialize=False)),
                ('TIAG_CODIGO', models.PositiveIntegerField()),
                ('AGEN_DESCRIPCION', models.CharField(max_length=40)),
                ('AGEN_DIRECCION', models.CharField(max_length=40)),
                ('AGEN_RESPONSABLE', models.CharField(max_length=40)),
                ('AGEN_TELEFONO', models.CharField(max_length=40)),
                ('AGEN_CODIGO_SUPER', models.CharField(max_length=40, null=True)),
                ('CIUD_CODIGO', models.PositiveIntegerField()),
            ],
            options={
                'db_table': 'AGENCIA',
            },
        ),
        migrations.CreateModel(
            name='Banco',
            fields=[
                ('BANC_CODIGO', models.PositiveIntegerField(primary_key=True, serialize=False)),
                ('BANC_DESCRIPCION', models.CharField(max_length=40)),
            ],
            options={
                'db_table': 'BANCO',
            },
        ),
        migrations.CreateModel(
            name='Canton',
            fields=[
                ('PROV_CODIGO', models.CharField(max_length=5)),
                ('CANT_CODIGO', models.CharField(max_length=5, primary_key=True, serialize=False)),
                ('CANT_NOMBRE', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'CANTON',
            },
        ),
        migrations.CreateModel(
            name='CuentaBalance',
            fields=[
                ('CUBA_CUENTA', models.PositiveBigIntegerField(primary_key=True, serialize=False)),
                ('TICB_CODIGO', models.PositiveIntegerField()),
                ('CUBA_DESCRIPCION', models.CharField(max_length=40)),
            ],
            options={
                'db_table': 'CUENTA_BALANCE',
            },
        ),
        migrations.CreateModel(
            name='EstadoCivil',
            fields=[
                ('ESCI_CODIGO', models.AutoField(primary_key=True, serialize=False)),
                ('ESCI_DESCRIPCION', models.CharField(max_length=40)),
            ],
            options={
                'db_table': 'ESTADO_CIVIL',
            },
        ),
        migrations.CreateModel(
            name='GrupoEconomico',
            fields=[
                ('GREC_CODIGO', models.PositiveIntegerField(primary_key=True, serialize=False)),
                ('GREC_DESCRIPCION', models.CharField(max_length=40)),
            ],
            options={
                'db_table': 'GRUPO_ECONOMICO',
            },
        ),
        migrations.CreateModel(
            name='Moneda',
            fields=[
                ('MONE_CODIGO', models.CharField(max_length=3, primary_key=True, serialize=False)),
                ('MONE_DESCRIPCION', models.CharField(max_length=40)),
                ('MONE_DECIMALES', models.PositiveIntegerField()),
                ('MONE_ALIAS', models.CharField(max_length=3)),
            ],
            options={
                'db_table': 'MONEDA',
            },
        ),
        migrations.CreateModel(
            name='Nacionalidad',
            fields=[
                ('NACI_CODIGO', models.PositiveIntegerField(primary_key=True, serialize=False)),
                ('NACI_DESCRIPCION', models.CharField(max_length=40)),
            ],
            options={
                'db_table': 'NACIONALIDAD',
            },
        ),
        migrations.CreateModel(
            name='NivelInstruccion',
            fields=[
                ('NIIN_CODIGO', models.AutoField(primary_key=True, serialize=False)),
                ('NIIN_DESCRIPCION', models.CharField(max_length=40)),
            ],
            options={
                'db_table': 'NIVEL_INSTRUCCION',
            },
        ),
        migrations.CreateModel(
            name='Pais',
            fields=[
                ('PAIS_CODIGO', models.CharField(max_length=3, primary_key=True, serialize=False)),
                ('PAIS_DESCRIPCION', models.CharField(max_length=40)),
            ],
            options={
                'db_table': 'PAIS',
            },
        ),
        migrations.CreateModel(
            name='Parroquia',
            fields=[
                ('PROV_CODIGO', models.CharField(max_length=5)),
                ('CANT_CODIGO', models.CharField(max_length=5)),
                ('PARR_CODIGO', models.CharField(max_length=5, primary_key=True, serialize=False)),
                ('PARR_NOMBRE', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'PARROQUIA',
            },
        ),
        migrations.CreateModel(
            name='Periocidad',
            fields=[
                ('PERI_CODIGO', models.PositiveIntegerField(primary_key=True, serialize=False)),
                ('PERI_DESCRIPCION', models.CharField(max_length=40)),
            ],
            options={
                'db_table': 'PERIOCIDAD',
            },
        ),
        migrations.CreateModel(
            name='Profesion',
            fields=[
                ('PROF_CODIGO', models.AutoField(primary_key=True, serialize=False)),
                ('PROF_DESCRIPCION', models.CharField(max_length=40)),
            ],
            options={
                'db_table': 'PROFESION',
            },
        ),
        migrations.CreateModel(
            name='Provincia',
            fields=[
                ('PAIS_CODIGO', models.CharField(max_length=3)),
                ('PROV_CODIGO', models.CharField(max_length=5, primary_key=True, serialize=False)),
                ('PROV_NOMBRE', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'PROVINCIA',
            },
        ),
        migrations.CreateModel(
            name='Sexo',
            fields=[
                ('SEXO_CODIGO', models.CharField(max_length=3, primary_key=True, serialize=False)),
                ('SEXO_DESCRIPCION', models.CharField(max_length=40)),
            ],
            options={
                'db_table': 'SEXO',
            },
        ),
        migrations.CreateModel(
            name='SituacionLaboral',
            fields=[
                ('SITL_CODIGO', models.AutoField(primary_key=True, serialize=False)),
                ('SITL_DESCRIPCION', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'SITUACION_LABORAL',
            },
        ),
        migrations.CreateModel(
            name='SubtipoEmpresa',
            fields=[
                ('TIEM_CODIGO', models.PositiveIntegerField()),
                ('SUTE_CODIGO', models.PositiveIntegerField(primary_key=True, serialize=False)),
                ('SUTE_DESCRIPCION', models.CharField(max_length=40)),
            ],
            options={
                'db_table': 'SUB_TIPO_EMPRESA',
            },
        ),
        migrations.CreateModel(
            name='TipoAgencia',
            fields=[
                ('TIAG_CODIGO', models.PositiveIntegerField(primary_key=True, serialize=False)),
                ('TIAG_DESCRIPCION', models.CharField(max_length=40)),
                ('TIAG_CENTRO_CANJE', models.CharField(max_length=2)),
            ],
            options={
                'db_table': 'TIPO_AGENCIA',
            },
        ),
        migrations.CreateModel(
            name='TipoAsesor',
            fields=[
                ('TIAS_CODIGO', models.PositiveIntegerField(primary_key=True, serialize=False)),
                ('TIAS_DESCRIPCION', models.CharField(max_length=40)),
            ],
            options={
                'db_table': 'TIPO_ASESOR',
            },
        ),
        migrations.CreateModel(
            name='TipoBanca',
            fields=[
                ('TIBA_CODIGO', models.PositiveIntegerField(primary_key=True, serialize=False)),
                ('TIBA_DESCRIPCION', models.CharField(max_length=40)),
                ('TIBA_RESPONSABLE', models.CharField(max_length=40)),
            ],
            options={
                'db_table': 'TIPO_DE_BANCA',
            },
        ),
        migrations.CreateModel(
            name='TipoCliente',
            fields=[
                ('TICL_CODIGO', models.CharField(max_length=2, primary_key=True, serialize=False)),
                ('TICL_DESCRIPCION', models.CharField(max_length=40)),
            ],
            options={
                'db_table': 'TIPO_CLIENTE',
            },
        ),
        migrations.CreateModel(
            name='TipoCuenta',
            fields=[
                ('TICU_CODIGO', models.PositiveIntegerField(primary_key=True, serialize=False)),
                ('TICU_DESCRIPCION', models.CharField(max_length=40)),
                ('TICU_CODIGO_ALT', models.CharField(max_length=5)),
            ],
            options={
                'db_table': 'TIPO_CUENTA',
            },
        ),
        migrations.CreateModel(
            name='TipoCuentaBalance',
            fields=[
                ('TICB_CODIGO', models.PositiveIntegerField(primary_key=True, serialize=False)),
                ('TICB_DESCRIPCION', models.CharField(max_length=40)),
            ],
            options={
                'db_table': 'TIPO_CUENTA_BALANCE',
            },
        ),
        migrations.CreateModel(
            name='TipoDireccion',
            fields=[
                ('TIDE_CODIGO', models.AutoField(primary_key=True, serialize=False)),
                ('TIDE_DESCRIPCION', models.CharField(max_length=40)),
            ],
            options={
                'db_table': 'TIPO_DIRECCION',
            },
        ),
        migrations.CreateModel(
            name='TipoEmpresa',
            fields=[
                ('TIEM_CODIGO', models.PositiveIntegerField(primary_key=True, serialize=False)),
                ('TIEM_DESCRIPCION', models.CharField(max_length=40)),
            ],
            options={
                'db_table': 'TIPO_EMPRESA',
            },
        ),
        migrations.CreateModel(
            name='TipoObservacion',
            fields=[
                ('TIOC_CODIGO', models.AutoField(primary_key=True, serialize=False)),
                ('TIOC_DESCRI', models.CharField(max_length=40)),
                ('TIOC_CAMBIO', models.PositiveIntegerField()),
            ],
            options={
                'db_table': 'TIPO_OBSERVACION_CLIENTE',
            },
        ),
        migrations.CreateModel(
            name='TipoProyecto',
            fields=[
                ('COD_TIPO_PROYECTO', models.PositiveIntegerField(primary_key=True, serialize=False)),
                ('DESC_TIPO_PROYECTO', models.CharField(max_length=50, null=True)),
            ],
            options={
                'db_table': 'CLIE_TIPO_PROYECTO',
            },
        ),
        migrations.CreateModel(
            name='TipoRol',
            fields=[
                ('TIRO_CODIGO', models.CharField(max_length=2, primary_key=True, serialize=False)),
                ('TIROL_DESCRIPCIÒN', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'TIPO_ROL',
            },
        ),
        migrations.CreateModel(
            name='TipoTelefono',
            fields=[
                ('TITE_CODIGO', models.AutoField(primary_key=True, serialize=False)),
                ('TITE_DESCRIPCION', models.CharField(max_length=40)),
            ],
            options={
                'db_table': 'TIPO_TELEFONO',
            },
        ),
        migrations.CreateModel(
            name='VehiculoLegal',
            fields=[
                ('VELE_CODIGO', models.CharField(max_length=3, primary_key=True, serialize=False)),
                ('PAIS_CODIGO', models.CharField(max_length=3)),
                ('VELE_DESCRIPCION', models.CharField(max_length=40)),
            ],
            options={
                'db_table': 'VEHICULO_LEGAL',
            },
        ),
        migrations.CreateModel(
            name='Vivienda',
            fields=[
                ('VIVI_CODIGO', models.AutoField(primary_key=True, serialize=False)),
                ('VIVI_DESCRIPCION', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'VIVIENDA',
            },
        ),
        migrations.CreateModel(
            name='Zona',
            fields=[
                ('ZONA_CODIGO', models.PositiveIntegerField(primary_key=True, serialize=False)),
                ('PAIS_CODIGO', models.PositiveIntegerField()),
                ('ZONA_DESCRIPCION', models.CharField(max_length=40)),
            ],
            options={
                'db_table': 'ZONA',
            },
        ),
        migrations.CreateModel(
            name='TipoVinculo',
            fields=[
                ('TICL_CODIGO', models.CharField(max_length=2)),
                ('TIVI_CODIGO', models.PositiveIntegerField(primary_key=True, serialize=False)),
                ('TIVI_DESCRIPCION', models.CharField(max_length=40)),
            ],
            options={
                'db_table': 'TIPO_VINCULO',
                'unique_together': {('TICL_CODIGO', 'TIVI_CODIGO')},
            },
        ),
        migrations.CreateModel(
            name='TipoDocumento',
            fields=[
                ('TICL_CODIGO', models.PositiveIntegerField()),
                ('TIDO_CODIGO', models.CharField(max_length=2, primary_key=True, serialize=False)),
                ('TIDO_DESCRIPCION', models.CharField(max_length=40)),
            ],
            options={
                'db_table': 'TIPO_DOCUMENTO',
                'unique_together': {('TICL_CODIGO', 'TIDO_CODIGO')},
            },
        ),
        migrations.CreateModel(
            name='Ciudad',
            fields=[
                ('CIUD_CODIGO', models.AutoField(primary_key=True, serialize=False)),
                ('CIUD_NOMBRE', models.CharField(max_length=50)),
                ('ZONA_CODIGO', models.ForeignKey(db_column='ZONA_CODIGO', on_delete=django.db.models.deletion.CASCADE, to='catalog.zona')),
            ],
            options={
                'db_table': 'CIUDAD',
            },
        ),
    ]
