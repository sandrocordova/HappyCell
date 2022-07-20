# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Agencia(models.Model):
    zona_codigo = models.ForeignKey('Zona', models.DO_NOTHING, db_column='ZONA_CODIGO', primary_key=True)  # Field name made lowercase.
    empr_codigo = models.ForeignKey('Empresa', models.DO_NOTHING, db_column='EMPR_CODIGO')  # Field name made lowercase.
    agen_codigo = models.DecimalField(db_column='AGEN_CODIGO', max_digits=4, decimal_places=0)  # Field name made lowercase.
    tiag_codigo = models.ForeignKey('TipoAgencia', models.DO_NOTHING, db_column='TIAG_CODIGO')  # Field name made lowercase.
    agen_descripcion = models.CharField(db_column='AGEN_DESCRIPCION', max_length=40)  # Field name made lowercase.
    agen_direccion = models.CharField(db_column='AGEN_DIRECCION', max_length=80)  # Field name made lowercase.
    agen_responsable = models.CharField(db_column='AGEN_RESPONSABLE', max_length=40)  # Field name made lowercase.
    agen_telefono = models.CharField(db_column='AGEN_TELEFONO', max_length=80)  # Field name made lowercase.
    agen_codigo_super = models.CharField(db_column='AGEN_CODIGO_SUPER', max_length=40, blank=True, null=True)  # Field name made lowercase.
    ciud_codigo = models.DecimalField(db_column='CIUD_CODIGO', max_digits=5, decimal_places=0, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'AGENCIA'
        unique_together = (('zona_codigo', 'empr_codigo', 'agen_codigo'),)


class AgenciaCentroCanje(models.Model):
    zona_codigo = models.ForeignKey(Agencia, models.DO_NOTHING, db_column='ZONA_CODIGO', primary_key=True)  # Field name made lowercase.
    empr_codigo = models.ForeignKey(Agencia, models.DO_NOTHING, db_column='EMPR_CODIGO')  # Field name made lowercase.
    agen_codigo = models.ForeignKey(Agencia, models.DO_NOTHING, db_column='AGEN_CODIGO')  # Field name made lowercase.
    ceca_codigo = models.ForeignKey('CentroDeCanje', models.DO_NOTHING, db_column='CECA_CODIGO')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'AGENCIA_CENTRO_CANJE'
        unique_together = (('zona_codigo', 'empr_codigo', 'agen_codigo', 'ceca_codigo'),)


class Asesor(models.Model):
    ases_codigo = models.DecimalField(db_column='ASES_CODIGO', primary_key=True, max_digits=4, decimal_places=0)  # Field name made lowercase.
    tias_codigo = models.ForeignKey('TipoAsesor', models.DO_NOTHING, db_column='TIAS_CODIGO')  # Field name made lowercase.
    ase_ases_codigo = models.ForeignKey('self', models.DO_NOTHING, db_column='ASE_ASES_CODIGO', blank=True, null=True)  # Field name made lowercase.
    tiba_codigo = models.ForeignKey('TipoDeBanca', models.DO_NOTHING, db_column='TIBA_CODIGO')  # Field name made lowercase.
    zona_codigo = models.ForeignKey(Agencia, models.DO_NOTHING, db_column='ZONA_CODIGO')  # Field name made lowercase.
    empr_codigo = models.ForeignKey(Agencia, models.DO_NOTHING, db_column='EMPR_CODIGO')  # Field name made lowercase.
    agen_codigo = models.ForeignKey(Agencia, models.DO_NOTHING, db_column='AGEN_CODIGO')  # Field name made lowercase.
    usua_codigo = models.ForeignKey('Usuario', models.DO_NOTHING, db_column='USUA_CODIGO')  # Field name made lowercase.
    ases_nombre = models.CharField(db_column='ASES_NOMBRE', max_length=40)  # Field name made lowercase.
    ases_clave = models.CharField(db_column='ASES_CLAVE', max_length=40)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ASESOR'


class AsesorCopy(models.Model):
    ases_codigo = models.DecimalField(db_column='ASES_CODIGO', primary_key=True, max_digits=4, decimal_places=0)  # Field name made lowercase.
    tias_codigo = models.DecimalField(db_column='TIAS_CODIGO', max_digits=2, decimal_places=0)  # Field name made lowercase.
    ase_ases_codigo = models.DecimalField(db_column='ASE_ASES_CODIGO', max_digits=4, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    tiba_codigo = models.DecimalField(db_column='TIBA_CODIGO', max_digits=2, decimal_places=0)  # Field name made lowercase.
    zona_codigo = models.DecimalField(db_column='ZONA_CODIGO', max_digits=4, decimal_places=0)  # Field name made lowercase.
    empr_codigo = models.CharField(db_column='EMPR_CODIGO', max_length=10)  # Field name made lowercase.
    agen_codigo = models.DecimalField(db_column='AGEN_CODIGO', max_digits=4, decimal_places=0)  # Field name made lowercase.
    usua_codigo = models.CharField(db_column='USUA_CODIGO', max_length=20)  # Field name made lowercase.
    ases_nombre = models.CharField(db_column='ASES_NOMBRE', max_length=40)  # Field name made lowercase.
    ases_clave = models.CharField(db_column='ASES_CLAVE', max_length=40)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ASESOR_copy'


class AuditoriaCampos(models.Model):
    auta_codigo = models.ForeignKey('AuditoriaTablas', models.DO_NOTHING, db_column='AUTA_CODIGO', primary_key=True)  # Field name made lowercase.
    auca_codigo = models.DecimalField(db_column='AUCA_CODIGO', max_digits=4, decimal_places=0)  # Field name made lowercase.
    auca_campo = models.CharField(db_column='AUCA_CAMPO', max_length=40)  # Field name made lowercase.
    auca_valor_antes = models.CharField(db_column='AUCA_VALOR_ANTES', max_length=40, blank=True, null=True)  # Field name made lowercase.
    auca_valor_despues = models.CharField(db_column='AUCA_VALOR_DESPUES', max_length=40, blank=True, null=True)  # Field name made lowercase.
    clave_primaria = models.CharField(db_column='CLAVE_PRIMARIA', max_length=200, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'AUDITORIA_CAMPOS'
        unique_together = (('auta_codigo', 'auca_codigo'),)


class AuditoriaTablas(models.Model):
    auta_codigo = models.DecimalField(db_column='AUTA_CODIGO', primary_key=True, max_digits=10, decimal_places=0)  # Field name made lowercase.
    auta_tabla = models.CharField(db_column='AUTA_TABLA', max_length=40)  # Field name made lowercase.
    auta_usuario = models.CharField(db_column='AUTA_USUARIO', max_length=40)  # Field name made lowercase.
    auta_fecha = models.DateTimeField(db_column='AUTA_FECHA')  # Field name made lowercase.
    auta_operacion = models.CharField(db_column='AUTA_OPERACION', max_length=1)  # Field name made lowercase.
    auta_estacion = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'AUDITORIA_TABLAS'


class Banco(models.Model):
    banc_codigo = models.DecimalField(db_column='BANC_CODIGO', primary_key=True, max_digits=4, decimal_places=0)  # Field name made lowercase.
    banc_descripcion = models.CharField(db_column='BANC_DESCRIPCION', max_length=40)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'BANCO'


class Bases(models.Model):
    name = models.CharField(max_length=128)

    class Meta:
        managed = False
        db_table = 'BASES'


class CatalogoTablas(models.Model):
    mosi_codigo = models.ForeignKey('ModuloSistema', models.DO_NOTHING, db_column='MOSI_CODIGO')  # Field name made lowercase.
    cata_titulo = models.CharField(db_column='CATA_TITULO', max_length=40)  # Field name made lowercase.
    cata_tabla = models.CharField(db_column='CATA_TABLA', max_length=40)  # Field name made lowercase.
    cata_grupo = models.CharField(db_column='CATA_GRUPO', max_length=6)  # Field name made lowercase.
    cata_comun = models.CharField(db_column='CATA_COMUN', max_length=1)  # Field name made lowercase.
    cata_datawindow = models.CharField(db_column='CATA_DATAWINDOW', max_length=40)  # Field name made lowercase.
    cata_tipo = models.CharField(db_column='CATA_TIPO', max_length=1)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CATALOGO_TABLAS'


class CentroDeCanje(models.Model):
    ceca_codigo = models.DecimalField(db_column='CECA_CODIGO', primary_key=True, max_digits=4, decimal_places=0)  # Field name made lowercase.
    zona_codigo = models.ForeignKey(Agencia, models.DO_NOTHING, db_column='ZONA_CODIGO')  # Field name made lowercase.
    empr_codigo = models.ForeignKey(Agencia, models.DO_NOTHING, db_column='EMPR_CODIGO')  # Field name made lowercase.
    agen_codigo = models.ForeignKey(Agencia, models.DO_NOTHING, db_column='AGEN_CODIGO')  # Field name made lowercase.
    ceca_descripcion = models.CharField(db_column='CECA_DESCRIPCION', max_length=40)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CENTRO_DE_CANJE'


class CentroDeCosto(models.Model):
    zona_codigo = models.ForeignKey(Agencia, models.DO_NOTHING, db_column='ZONA_CODIGO', primary_key=True)  # Field name made lowercase.
    empr_codigo = models.ForeignKey(Agencia, models.DO_NOTHING, db_column='EMPR_CODIGO')  # Field name made lowercase.
    agen_codigo = models.ForeignKey(Agencia, models.DO_NOTHING, db_column='AGEN_CODIGO')  # Field name made lowercase.
    cetc_codigo = models.DecimalField(db_column='CETC_CODIGO', max_digits=4, decimal_places=0)  # Field name made lowercase.
    cetc_descripcion = models.CharField(db_column='CETC_DESCRIPCION', max_length=40)  # Field name made lowercase.
    cetc_responsable = models.CharField(db_column='CETC_RESPONSABLE', max_length=40)  # Field name made lowercase.
    cetc_vigente = models.CharField(db_column='CETC_VIGENTE', max_length=1, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CENTRO_DE_COSTO'
        unique_together = (('zona_codigo', 'empr_codigo', 'agen_codigo', 'cetc_codigo'),)


class Ciudad(models.Model):
    zona_codigo = models.DecimalField(db_column='ZONA_CODIGO', primary_key=True, max_digits=4, decimal_places=0)  # Field name made lowercase.
    ciud_codigo = models.DecimalField(db_column='CIUD_CODIGO', max_digits=4, decimal_places=0)  # Field name made lowercase.
    ciud_nombre = models.CharField(db_column='CIUD_NOMBRE', max_length=50)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CIUDAD'
        unique_together = (('zona_codigo', 'ciud_codigo'),)


class ControlChecker(models.Model):
    coch_codigo = models.SmallIntegerField(db_column='COCH_CODIGO', primary_key=True)  # Field name made lowercase.
    coch_ejecuta = models.CharField(db_column='COCH_EJECUTA', max_length=1, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CONTROL_CHECKER'


class ControlCierre(models.Model):
    empr_codigo = models.ForeignKey('ModuloEmpresa', models.DO_NOTHING, db_column='EMPR_CODIGO', primary_key=True)  # Field name made lowercase.
    mosi_codigo = models.ForeignKey('ModuloEmpresa', models.DO_NOTHING, db_column='MOSI_CODIGO')  # Field name made lowercase.
    coci_confirma_precierre = models.CharField(db_column='COCI_CONFIRMA_PRECIERRE', max_length=1)  # Field name made lowercase.
    coci_confirma_cierre = models.CharField(db_column='COCI_CONFIRMA_CIERRE', max_length=1)  # Field name made lowercase.
    coci_orden = models.DecimalField(db_column='COCI_ORDEN', max_digits=2, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    fecha_actual = models.DateTimeField(db_column='FECHA_ACTUAL', blank=True, null=True)  # Field name made lowercase.
    fecha_anterior = models.DateTimeField(db_column='FECHA_ANTERIOR', blank=True, null=True)  # Field name made lowercase.
    fecha_siguiente = models.DateTimeField(db_column='FECHA_SIGUIENTE', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CONTROL_CIERRE'
        unique_together = (('empr_codigo', 'mosi_codigo'),)


class ControlCierrePc6(models.Model):
    empr_codigo = models.CharField(db_column='EMPR_CODIGO', max_length=10)  # Field name made lowercase.
    mosi_codigo = models.DecimalField(db_column='MOSI_CODIGO', max_digits=2, decimal_places=0)  # Field name made lowercase.
    coci_confirma_precierre = models.CharField(db_column='COCI_CONFIRMA_PRECIERRE', max_length=1)  # Field name made lowercase.
    coci_confirma_cierre = models.CharField(db_column='COCI_CONFIRMA_CIERRE', max_length=1)  # Field name made lowercase.
    coci_orden = models.DecimalField(db_column='COCI_ORDEN', max_digits=2, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    fecha_actual = models.DateTimeField(db_column='FECHA_ACTUAL', blank=True, null=True)  # Field name made lowercase.
    fecha_anterior = models.DateTimeField(db_column='FECHA_ANTERIOR', blank=True, null=True)  # Field name made lowercase.
    fecha_siguiente = models.DateTimeField(db_column='FECHA_SIGUIENTE', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CONTROL_CIERRE_PC6'


class ControlCierrePc7(models.Model):
    empr_codigo = models.CharField(db_column='EMPR_CODIGO', max_length=10)  # Field name made lowercase.
    mosi_codigo = models.DecimalField(db_column='MOSI_CODIGO', max_digits=2, decimal_places=0)  # Field name made lowercase.
    coci_confirma_precierre = models.CharField(db_column='COCI_CONFIRMA_PRECIERRE', max_length=1)  # Field name made lowercase.
    coci_confirma_cierre = models.CharField(db_column='COCI_CONFIRMA_CIERRE', max_length=1)  # Field name made lowercase.
    coci_orden = models.DecimalField(db_column='COCI_ORDEN', max_digits=2, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    fecha_actual = models.DateTimeField(db_column='FECHA_ACTUAL', blank=True, null=True)  # Field name made lowercase.
    fecha_anterior = models.DateTimeField(db_column='FECHA_ANTERIOR', blank=True, null=True)  # Field name made lowercase.
    fecha_siguiente = models.DateTimeField(db_column='FECHA_SIGUIENTE', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CONTROL_CIERRE_PC7'


class ControlCierrePc8(models.Model):
    empr_codigo = models.CharField(db_column='EMPR_CODIGO', max_length=10)  # Field name made lowercase.
    mosi_codigo = models.DecimalField(db_column='MOSI_CODIGO', max_digits=2, decimal_places=0)  # Field name made lowercase.
    coci_confirma_precierre = models.CharField(db_column='COCI_CONFIRMA_PRECIERRE', max_length=1)  # Field name made lowercase.
    coci_confirma_cierre = models.CharField(db_column='COCI_CONFIRMA_CIERRE', max_length=1)  # Field name made lowercase.
    coci_orden = models.DecimalField(db_column='COCI_ORDEN', max_digits=2, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    fecha_actual = models.DateTimeField(db_column='FECHA_ACTUAL', blank=True, null=True)  # Field name made lowercase.
    fecha_anterior = models.DateTimeField(db_column='FECHA_ANTERIOR', blank=True, null=True)  # Field name made lowercase.
    fecha_siguiente = models.DateTimeField(db_column='FECHA_SIGUIENTE', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CONTROL_CIERRE_PC8'


class ControlCierrePc9(models.Model):
    empr_codigo = models.CharField(db_column='EMPR_CODIGO', max_length=10)  # Field name made lowercase.
    mosi_codigo = models.DecimalField(db_column='MOSI_CODIGO', max_digits=2, decimal_places=0)  # Field name made lowercase.
    coci_confirma_precierre = models.CharField(db_column='COCI_CONFIRMA_PRECIERRE', max_length=1)  # Field name made lowercase.
    coci_confirma_cierre = models.CharField(db_column='COCI_CONFIRMA_CIERRE', max_length=1)  # Field name made lowercase.
    coci_orden = models.DecimalField(db_column='COCI_ORDEN', max_digits=2, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    fecha_actual = models.DateTimeField(db_column='FECHA_ACTUAL', blank=True, null=True)  # Field name made lowercase.
    fecha_anterior = models.DateTimeField(db_column='FECHA_ANTERIOR', blank=True, null=True)  # Field name made lowercase.
    fecha_siguiente = models.DateTimeField(db_column='FECHA_SIGUIENTE', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CONTROL_CIERRE_PC9'


class Cotizacion(models.Model):
    mone_empresa = models.ForeignKey('RelacionMonedas', models.DO_NOTHING, db_column='MONE_EMPRESA', primary_key=True)  # Field name made lowercase.
    mone_transaccion = models.ForeignKey('RelacionMonedas', models.DO_NOTHING, db_column='MONE_TRANSACCION')  # Field name made lowercase.
    zona_codigo = models.ForeignKey('Zona', models.DO_NOTHING, db_column='ZONA_CODIGO')  # Field name made lowercase.
    coti_fecha = models.DateTimeField(db_column='COTI_FECHA')  # Field name made lowercase.
    tico_codigo = models.ForeignKey('TipoCotizacion', models.DO_NOTHING, db_column='TICO_CODIGO')  # Field name made lowercase.
    coti_valor_compra = models.DecimalField(db_column='COTI_VALOR_COMPRA', max_digits=18, decimal_places=6)  # Field name made lowercase.
    coti_valor_venta = models.DecimalField(db_column='COTI_VALOR_VENTA', max_digits=18, decimal_places=6)  # Field name made lowercase.
    coti_valor_promedio = models.DecimalField(db_column='COTI_VALOR_PROMEDIO', max_digits=18, decimal_places=6)  # Field name made lowercase.
    coti_usuario = models.CharField(db_column='COTI_USUARIO', max_length=10)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'COTIZACION'
        unique_together = (('mone_empresa', 'mone_transaccion', 'zona_codigo', 'coti_fecha', 'tico_codigo'),)


class CuentaBancariaEmpresa(models.Model):
    banc_codigo = models.ForeignKey(Banco, models.DO_NOTHING, db_column='BANC_CODIGO', primary_key=True)  # Field name made lowercase.
    ticu_codigo = models.ForeignKey('TipoCuenta', models.DO_NOTHING, db_column='TICU_CODIGO')  # Field name made lowercase.
    empr_codigo = models.ForeignKey('Empresa', models.DO_NOTHING, db_column='EMPR_CODIGO')  # Field name made lowercase.
    cuba_codigo = models.DecimalField(db_column='CUBA_CODIGO', max_digits=2, decimal_places=0)  # Field name made lowercase.
    cuba_cuenta = models.CharField(db_column='CUBA_CUENTA', max_length=20)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CUENTA_BANCARIA_EMPRESA'
        unique_together = (('banc_codigo', 'ticu_codigo', 'empr_codigo', 'cuba_codigo'),)


class CuentaDebitoAutomatico(models.Model):
    cznucz = models.DecimalField(db_column='CZNUCZ', primary_key=True, max_digits=18, decimal_places=0)  # Field name made lowercase.
    cuen_num_cuenta = models.CharField(db_column='CUEN_NUM_CUENTA', max_length=20)  # Field name made lowercase.
    cuen_producto = models.CharField(db_column='CUEN_PRODUCTO', max_length=20)  # Field name made lowercase.
    cudb_estado = models.CharField(db_column='CUDB_ESTADO', max_length=10)  # Field name made lowercase.
    cudb_fecha_ingreso = models.DateTimeField(db_column='CUDB_FECHA_INGRESO')  # Field name made lowercase.
    cudb_usuario_ingreso = models.CharField(db_column='CUDB_USUARIO_INGRESO', max_length=20, blank=True, null=True)  # Field name made lowercase.
    cudb_fecha_modificacion = models.DateTimeField(db_column='CUDB_FECHA_MODIFICACION', blank=True, null=True)  # Field name made lowercase.
    cudb_usuario_modificacion = models.CharField(db_column='CUDB_USUARIO_MODIFICACION', max_length=20, blank=True, null=True)  # Field name made lowercase.
    banc_codigo = models.ForeignKey(Banco, models.DO_NOTHING, db_column='BANC_CODIGO')  # Field name made lowercase.
    tipo_cuenta = models.DecimalField(db_column='TIPO_CUENTA', max_digits=4, decimal_places=0, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CUENTA_DEBITO_AUTOMATICO'
        unique_together = (('cznucz', 'cuen_num_cuenta'),)


class Empresa(models.Model):
    empr_codigo = models.CharField(db_column='EMPR_CODIGO', primary_key=True, max_length=10)  # Field name made lowercase.
    emp_empr_codigo = models.ForeignKey('self', models.DO_NOTHING, db_column='EMP_EMPR_CODIGO', blank=True, null=True)  # Field name made lowercase.
    vele_codigo = models.ForeignKey('VehiculoLegal', models.DO_NOTHING, db_column='VELE_CODIGO')  # Field name made lowercase.
    tiem_codigo = models.ForeignKey('SubTipoEmpresa', models.DO_NOTHING, db_column='TIEM_CODIGO')  # Field name made lowercase.
    sute_codigo = models.ForeignKey('SubTipoEmpresa', models.DO_NOTHING, db_column='SUTE_CODIGO')  # Field name made lowercase.
    mone_codigo = models.ForeignKey('Moneda', models.DO_NOTHING, db_column='MONE_CODIGO')  # Field name made lowercase.
    empr_nombre = models.CharField(db_column='EMPR_NOMBRE', max_length=80)  # Field name made lowercase.
    empr_identificacion = models.CharField(db_column='EMPR_IDENTIFICACION', max_length=20)  # Field name made lowercase.
    empr_fecha_constitucion = models.DateTimeField(db_column='EMPR_FECHA_CONSTITUCION')  # Field name made lowercase.
    empr_fecha_creacion = models.DateTimeField(db_column='EMPR_FECHA_CREACION')  # Field name made lowercase.
    empr_direccion = models.CharField(db_column='EMPR_DIRECCION', max_length=80)  # Field name made lowercase.
    fecha_actual = models.DateTimeField(db_column='FECHA_ACTUAL')  # Field name made lowercase.
    fecha_anterior = models.DateTimeField(db_column='FECHA_ANTERIOR')  # Field name made lowercase.
    fecha_siguiente = models.DateTimeField(db_column='FECHA_SIGUIENTE')  # Field name made lowercase.
    grem_codigo = models.ForeignKey('GrupoEmpresarial', models.DO_NOTHING, db_column='GREM_CODIGO')  # Field name made lowercase.
    peri_codigo = models.ForeignKey('Periocidad', models.DO_NOTHING, db_column='PERI_CODIGO')  # Field name made lowercase.
    fecha_cierre = models.DateTimeField(db_column='FECHA_CIERRE', blank=True, null=True)  # Field name made lowercase.
    empr_vigente = models.CharField(db_column='EMPR_VIGENTE', max_length=1)  # Field name made lowercase.
    empr_periocidad = models.DecimalField(db_column='EMPR_PERIOCIDAD', max_digits=2, decimal_places=0)  # Field name made lowercase.
    empr_codigo_super = models.CharField(db_column='EMPR_CODIGO_SUPER', max_length=20, blank=True, null=True)  # Field name made lowercase.
    empr_rep_legal = models.CharField(max_length=50, blank=True, null=True)
    empr_cargo = models.CharField(max_length=30, blank=True, null=True)
    autorizacion_sri = models.CharField(max_length=30, blank=True, null=True)
    contribuyente_esp = models.CharField(max_length=50, blank=True, null=True)
    empr_fecha_emision = models.CharField(max_length=30, blank=True, null=True)
    empr_imprime_imagen = models.IntegerField(db_column='EMPR_IMPRIME_IMAGEN', blank=True, null=True)  # Field name made lowercase.
    empr_imagen = models.CharField(db_column='EMPR_IMAGEN', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'EMPRESA'


class ErrorProcesoRemoto(models.Model):
    empr_codigo = models.CharField(db_column='EMPR_CODIGO', primary_key=True, max_length=10)  # Field name made lowercase.
    mosi_codigo = models.DecimalField(db_column='MOSI_CODIGO', max_digits=2, decimal_places=0)  # Field name made lowercase.
    usua_identificacion = models.CharField(db_column='USUA_IDENTIFICACION', max_length=15)  # Field name made lowercase.
    maquina = models.CharField(db_column='MAQUINA', max_length=50)  # Field name made lowercase.
    erpr_proceso = models.CharField(db_column='ERPR_PROCESO', max_length=25)  # Field name made lowercase.
    erpr_identificador = models.CharField(db_column='ERPR_IDENTIFICADOR', max_length=50)  # Field name made lowercase.
    erpr_secuencial = models.DecimalField(db_column='ERPR_SECUENCIAL', max_digits=18, decimal_places=0)  # Field name made lowercase.
    erpr_fecha_empresa = models.DateTimeField(db_column='ERPR_FECHA_EMPRESA')  # Field name made lowercase.
    erpr_fecha_proceso = models.DateTimeField(db_column='ERPR_FECHA_PROCESO')  # Field name made lowercase.
    erpr_observacion = models.CharField(db_column='ERPR_OBSERVACION', max_length=200, blank=True, null=True)  # Field name made lowercase.
    erpr_estado = models.CharField(db_column='ERPR_ESTADO', max_length=1)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ERROR_PROCESO_REMOTO'
        unique_together = (('empr_codigo', 'mosi_codigo', 'usua_identificacion', 'maquina', 'erpr_proceso', 'erpr_identificador', 'erpr_secuencial'),)


class ErrorProcesoRemotoCotizaciones(models.Model):
    empr_codigo = models.CharField(db_column='EMPR_CODIGO', primary_key=True, max_length=10)  # Field name made lowercase.
    mosi_codigo = models.DecimalField(db_column='MOSI_CODIGO', max_digits=2, decimal_places=0)  # Field name made lowercase.
    usua_identificacion = models.CharField(db_column='USUA_IDENTIFICACION', max_length=15)  # Field name made lowercase.
    erpr_proceso = models.CharField(db_column='ERPR_PROCESO', max_length=25)  # Field name made lowercase.
    erpr_secuencial = models.DecimalField(db_column='ERPR_SECUENCIAL', max_digits=18, decimal_places=0)  # Field name made lowercase.
    erpr_fecha_empresa = models.DateTimeField(db_column='ERPR_FECHA_EMPRESA')  # Field name made lowercase.
    erpr_fecha_proceso = models.DateTimeField(db_column='ERPR_FECHA_PROCESO')  # Field name made lowercase.
    erpr_observacion = models.CharField(db_column='ERPR_OBSERVACION', max_length=200, blank=True, null=True)  # Field name made lowercase.
    erpr_estado = models.CharField(db_column='ERPR_ESTADO', max_length=1)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ERROR_PROCESO_REMOTO_COTIZACIONES'
        unique_together = (('empr_codigo', 'mosi_codigo', 'usua_identificacion', 'erpr_proceso', 'erpr_secuencial'),)


class EstadoUsuario(models.Model):
    esus_codigo = models.DecimalField(db_column='ESUS_CODIGO', primary_key=True, max_digits=2, decimal_places=0)  # Field name made lowercase.
    esus_descripcion = models.CharField(db_column='ESUS_DESCRIPCION', max_length=40)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ESTADO_USUARIO'


class EtapaCierre(models.Model):
    etci_codigo = models.DecimalField(db_column='ETCI_CODIGO', primary_key=True, max_digits=2, decimal_places=0)  # Field name made lowercase.
    etci_descripcion = models.CharField(db_column='ETCI_DESCRIPCION', max_length=40)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ETAPA_CIERRE'


class Feriado(models.Model):
    zona_codigo = models.ForeignKey(Agencia, models.DO_NOTHING, db_column='ZONA_CODIGO', primary_key=True)  # Field name made lowercase.
    empr_codigo = models.ForeignKey(Agencia, models.DO_NOTHING, db_column='EMPR_CODIGO')  # Field name made lowercase.
    agen_codigo = models.ForeignKey(Agencia, models.DO_NOTHING, db_column='AGEN_CODIGO')  # Field name made lowercase.
    feri_fecha = models.DateTimeField(db_column='FERI_FECHA')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'FERIADO'
        unique_together = (('zona_codigo', 'empr_codigo', 'agen_codigo', 'feri_fecha'),)


class FeriadoNacional(models.Model):
    fena_fecha = models.DateTimeField(db_column='FENA_FECHA', primary_key=True)  # Field name made lowercase.
    vele_codigo = models.ForeignKey('VehiculoLegal', models.DO_NOTHING, db_column='VELE_CODIGO')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'FERIADO_NACIONAL'
        unique_together = (('fena_fecha', 'vele_codigo'),)


class GrupoAsesor(models.Model):
    ases_codigo = models.ForeignKey(Asesor, models.DO_NOTHING, db_column='ASES_CODIGO', primary_key=True)  # Field name made lowercase.
    gras_codigo = models.ForeignKey('TipoGrupoAsesor', models.DO_NOTHING, db_column='GRAS_CODIGO')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'GRUPO_ASESOR'
        unique_together = (('ases_codigo', 'gras_codigo'),)


class GrupoEmpresarial(models.Model):
    grem_codigo = models.DecimalField(db_column='GREM_CODIGO', primary_key=True, max_digits=4, decimal_places=0)  # Field name made lowercase.
    grem_descripcion = models.CharField(db_column='GREM_DESCRIPCION', max_length=40)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'GRUPO_EMPRESARIAL'


class LogCfcFormatoGuayaquil(models.Model):
    lg_codigo = models.DecimalField(db_column='LG_CODIGO', max_digits=9, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    lg_empr_codigo = models.CharField(db_column='LG_EMPR_CODIGO', max_length=10, blank=True, null=True)  # Field name made lowercase.
    lg_agen_codigo = models.DecimalField(db_column='LG_AGEN_CODIGO', max_digits=9, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    lg_usua_codigo = models.CharField(db_column='LG_USUA_CODIGO', max_length=20, blank=True, null=True)  # Field name made lowercase.
    lg_clie_codigo = models.DecimalField(db_column='LG_CLIE_CODIGO', max_digits=9, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    lg_cotizacion = models.DecimalField(db_column='LG_COTIZACION', max_digits=9, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    lg_contrato = models.DecimalField(db_column='LG_CONTRATO', max_digits=9, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    lg_anexo = models.DecimalField(db_column='LG_ANEXO', max_digits=9, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    lg_banco = models.DecimalField(db_column='LG_BANCO', max_digits=5, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    lg_num_cuenta = models.CharField(db_column='LG_NUM_CUENTA', max_length=50, blank=True, null=True)  # Field name made lowercase.
    lg_tipo_cuenta = models.DecimalField(db_column='LG_TIPO_CUENTA', max_digits=5, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    lg_fecha = models.DateTimeField(db_column='LG_FECHA', blank=True, null=True)  # Field name made lowercase.
    lg_fecha_proceso = models.DateTimeField(db_column='LG_FECHA_PROCESO', blank=True, null=True)  # Field name made lowercase.
    lg_etapa = models.CharField(db_column='LG_ETAPA', max_length=50, blank=True, null=True)  # Field name made lowercase.
    lg_referencia = models.CharField(db_column='LG_REFERENCIA', max_length=25, blank=True, null=True)  # Field name made lowercase.
    lg_capital = models.DecimalField(db_column='LG_CAPITAL', max_digits=9, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    lg_interes = models.DecimalField(db_column='LG_INTERES', max_digits=9, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    lg_mora = models.DecimalField(db_column='LG_MORA', max_digits=9, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    lg_rubros_adicionales = models.DecimalField(db_column='LG_RUBROS_ADICIONALES', max_digits=9, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    lg_comisiones = models.DecimalField(db_column='LG_COMISIONES', max_digits=9, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    lg_otros_valores = models.DecimalField(db_column='LG_OTROS_VALORES', max_digits=9, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    lg_formato = models.CharField(db_column='LG_FORMATO', max_length=59, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'LOG_CFC_FORMATO_GUAYAQUIL'


class LogRespaldoBdd(models.Model):
    lrbd_codigo = models.AutoField(primary_key=True)
    lrbd_fecha = models.DateTimeField()
    lrbd_descripcion = models.CharField(max_length=60, blank=True, null=True)
    lrbd_base = models.CharField(max_length=60, blank=True, null=True)
    lrbd_usuario = models.CharField(max_length=15, blank=True, null=True)
    lrbd_opcion = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'LOG_RESPALDO_BDD'


class ModuloEmpresa(models.Model):
    empr_codigo = models.ForeignKey(Empresa, models.DO_NOTHING, db_column='EMPR_CODIGO', primary_key=True)  # Field name made lowercase.
    mosi_codigo = models.ForeignKey('ModuloSistema', models.DO_NOTHING, db_column='MOSI_CODIGO')  # Field name made lowercase.
    fecha_actual = models.DateTimeField(db_column='FECHA_ACTUAL', blank=True, null=True)  # Field name made lowercase.
    fecha_siguiente = models.DateTimeField(db_column='FECHA_SIGUIENTE', blank=True, null=True)  # Field name made lowercase.
    fecha_anterior = models.DateTimeField(db_column='FECHA_ANTERIOR', blank=True, null=True)  # Field name made lowercase.
    modu_periocidad = models.DecimalField(db_column='MODU_PERIOCIDAD', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    peri_codigo = models.ForeignKey('Periocidad', models.DO_NOTHING, db_column='PERI_CODIGO', blank=True, null=True)  # Field name made lowercase.
    modu_cierra_feriados = models.CharField(db_column='MODU_CIERRA_FERIADOS', max_length=1, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MODULO_EMPRESA'
        unique_together = (('empr_codigo', 'mosi_codigo'),)


class ModuloSistema(models.Model):
    mosi_codigo = models.DecimalField(db_column='MOSI_CODIGO', primary_key=True, max_digits=2, decimal_places=0)  # Field name made lowercase.
    mosi_descripcion = models.CharField(db_column='MOSI_DESCRIPCION', max_length=40)  # Field name made lowercase.
    mosi_bdd = models.CharField(db_column='MOSI_BDD', max_length=40)  # Field name made lowercase.
    mosi_servidor = models.CharField(db_column='MOSI_SERVIDOR', max_length=40)  # Field name made lowercase.
    mosi_login = models.CharField(db_column='MOSI_LOGIN', max_length=40)  # Field name made lowercase.
    mosi_password = models.CharField(db_column='MOSI_PASSWORD', max_length=40)  # Field name made lowercase.
    mosi_vigente = models.CharField(db_column='MOSI_VIGENTE', max_length=1, blank=True, null=True)  # Field name made lowercase.
    mosi_orden_presentacion = models.DecimalField(db_column='MOSI_ORDEN_PRESENTACION', max_digits=3, decimal_places=0, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MODULO_SISTEMA'


class Moneda(models.Model):
    mone_codigo = models.CharField(db_column='MONE_CODIGO', primary_key=True, max_length=3)  # Field name made lowercase.
    mone_descripcion = models.CharField(db_column='MONE_DESCRIPCION', max_length=40)  # Field name made lowercase.
    mone_decimales = models.DecimalField(db_column='MONE_DECIMALES', max_digits=2, decimal_places=0)  # Field name made lowercase.
    mone_alias = models.CharField(db_column='MONE_ALIAS', max_length=3)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MONEDA'


class OpcionMenu(models.Model):
    mosi_codigo = models.ForeignKey(ModuloSistema, models.DO_NOTHING, db_column='MOSI_CODIGO', primary_key=True)  # Field name made lowercase.
    opme_codigo = models.DecimalField(db_column='OPME_CODIGO', max_digits=3, decimal_places=0)  # Field name made lowercase.
    opme_descripcion = models.CharField(db_column='OPME_DESCRIPCION', max_length=40)  # Field name made lowercase.
    opme_ejecuta = models.CharField(db_column='OPME_EJECUTA', max_length=1)  # Field name made lowercase.
    opc_mosi_codigo = models.ForeignKey('self', models.DO_NOTHING, db_column='OPC_MOSI_CODIGO', blank=True, null=True)  # Field name made lowercase.
    opc_opme_codigo = models.ForeignKey('self', models.DO_NOTHING, db_column='OPC_OPME_CODIGO', blank=True, null=True)  # Field name made lowercase.
    opme_orden = models.DecimalField(db_column='OPME_ORDEN', max_digits=4, decimal_places=0, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'OPCION_MENU'
        unique_together = (('mosi_codigo', 'opme_codigo'),)


class OpcionMenuCarga(models.Model):
    mosi_codigo = models.DecimalField(db_column='MOSI_CODIGO', max_digits=2, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    opme_codigo = models.DecimalField(db_column='OPME_CODIGO', max_digits=3, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    opme_descripcion = models.CharField(db_column='OPME_DESCRIPCION', max_length=40, blank=True, null=True)  # Field name made lowercase.
    opme_ejecuta = models.CharField(db_column='OPME_EJECUTA', max_length=1, blank=True, null=True)  # Field name made lowercase.
    opc_mosi_codigo = models.DecimalField(db_column='OPC_MOSI_CODIGO', max_digits=2, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    opc_opme_codigo = models.DecimalField(db_column='OPC_OPME_CODIGO', max_digits=3, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    opme_orden = models.DecimalField(db_column='OPME_ORDEN', max_digits=4, decimal_places=0, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'OPCION_MENU_CARGA'


class Pais(models.Model):
    pais_codigo = models.CharField(db_column='PAIS_CODIGO', primary_key=True, max_length=3)  # Field name made lowercase.
    pais_descripcion = models.CharField(db_column='PAIS_DESCRIPCION', max_length=40)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PAIS'


class Parametros(models.Model):
    para_codigo = models.CharField(db_column='PARA_CODIGO', primary_key=True, max_length=30)  # Field name made lowercase.
    para_valor_string = models.CharField(db_column='PARA_VALOR_STRING', max_length=200, blank=True, null=True)  # Field name made lowercase.
    para_valor_numeric = models.DecimalField(db_column='PARA_VALOR_NUMERIC', max_digits=18, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    para_descripcion = models.CharField(db_column='PARA_DESCRIPCION', max_length=60, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PARAMETROS'


class Perfil(models.Model):
    tipe_codigo = models.ForeignKey('TipoPerfil', models.DO_NOTHING, db_column='TIPE_CODIGO', primary_key=True)  # Field name made lowercase.
    mosi_codigo = models.ForeignKey(ModuloSistema, models.DO_NOTHING, db_column='MOSI_CODIGO')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PERFIL'
        unique_together = (('tipe_codigo', 'mosi_codigo'),)


class PerfilOpciones(models.Model):
    opme_codigo = models.ForeignKey(OpcionMenu, models.DO_NOTHING, db_column='OPME_CODIGO', primary_key=True)  # Field name made lowercase.
    mosi_codigo = models.ForeignKey(OpcionMenu, models.DO_NOTHING, db_column='MOSI_CODIGO')  # Field name made lowercase.
    tipe_codigo = models.ForeignKey(Perfil, models.DO_NOTHING, db_column='TIPE_CODIGO')  # Field name made lowercase.
    per_mosi_codigo = models.ForeignKey(Perfil, models.DO_NOTHING, db_column='PER_MOSI_CODIGO')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PERFIL_OPCIONES'
        unique_together = (('opme_codigo', 'mosi_codigo', 'tipe_codigo', 'per_mosi_codigo'),)


class PerfilOpcionesCarga(models.Model):
    opme_codigo = models.DecimalField(db_column='OPME_CODIGO', max_digits=3, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    mosi_codigo = models.DecimalField(db_column='MOSI_CODIGO', max_digits=2, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    tipe_codigo = models.DecimalField(db_column='TIPE_CODIGO', max_digits=2, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    per_mosi_codigo = models.DecimalField(db_column='PER_MOSI_CODIGO', max_digits=2, decimal_places=0, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PERFIL_OPCIONES_CARGA'


class PerfilVentana(models.Model):
    opme_codigo = models.DecimalField(db_column='OPME_CODIGO', primary_key=True, max_digits=3, decimal_places=0)  # Field name made lowercase.
    mosi_codigo = models.ForeignKey('Ventana', models.DO_NOTHING, db_column='MOSI_CODIGO')  # Field name made lowercase.
    pece_secuencia = models.DecimalField(db_column='PECE_SECUENCIA', max_digits=2, decimal_places=0)  # Field name made lowercase.
    tipe_codigo = models.DecimalField(db_column='TIPE_CODIGO', max_digits=2, decimal_places=0)  # Field name made lowercase.
    per_mosi_codigo2 = models.DecimalField(db_column='PER_MOSI_CODIGO2', max_digits=2, decimal_places=0)  # Field name made lowercase.
    per_mosi_codigo = models.DecimalField(db_column='PER_MOSI_CODIGO', max_digits=2, decimal_places=0)  # Field name made lowercase.
    vent_codigo = models.ForeignKey('Ventana', models.DO_NOTHING, db_column='VENT_CODIGO')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PERFIL_VENTANA'
        unique_together = (('opme_codigo', 'mosi_codigo', 'tipe_codigo', 'per_mosi_codigo2', 'per_mosi_codigo', 'vent_codigo'),)


class PerfilVentanaCargar(models.Model):
    opme_codigo = models.DecimalField(db_column='OPME_CODIGO', max_digits=3, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    mosi_codigo = models.DecimalField(db_column='MOSI_CODIGO', max_digits=2, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    pece_secuencia = models.DecimalField(db_column='PECE_SECUENCIA', max_digits=2, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    tipe_codigo = models.DecimalField(db_column='TIPE_CODIGO', max_digits=2, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    per_mosi_codigo2 = models.DecimalField(db_column='PER_MOSI_CODIGO2', max_digits=2, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    per_mosi_codigo = models.DecimalField(db_column='PER_MOSI_CODIGO', max_digits=2, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    vent_codigo = models.CharField(db_column='VENT_CODIGO', max_length=40, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PERFIL_VENTANA_CARGAR'


class Periocidad(models.Model):
    peri_codigo = models.DecimalField(db_column='PERI_CODIGO', primary_key=True, max_digits=2, decimal_places=0)  # Field name made lowercase.
    peri_descripcion = models.CharField(db_column='PERI_DESCRIPCION', max_length=40)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PERIOCIDAD'


class PermisosUsuariosBases(models.Model):
    base = models.CharField(max_length=17)
    usuario = models.CharField(max_length=128)
    type_desc = models.CharField(max_length=60, blank=True, null=True)
    tipoobjeto = models.CharField(max_length=60, blank=True, null=True)
    permission_name = models.CharField(max_length=128, blank=True, null=True)
    state_desc = models.CharField(max_length=60, blank=True, null=True)
    nombreobjeto = models.CharField(max_length=128)
    tipo_usuario = models.CharField(db_column='TIPO_USUARIO', max_length=4)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PERMISOS_USUARIOS_BASES'


class ProcesosCierre(models.Model):
    empr_codigo = models.ForeignKey(ControlCierre, models.DO_NOTHING, db_column='EMPR_CODIGO', primary_key=True)  # Field name made lowercase.
    mosi_codigo = models.ForeignKey(ControlCierre, models.DO_NOTHING, db_column='MOSI_CODIGO')  # Field name made lowercase.
    prci_codigo = models.DecimalField(db_column='PRCI_CODIGO', max_digits=4, decimal_places=0)  # Field name made lowercase.
    etci_codigo = models.ForeignKey(EtapaCierre, models.DO_NOTHING, db_column='ETCI_CODIGO')  # Field name made lowercase.
    tipo_codigo = models.ForeignKey('TipoProceso', models.DO_NOTHING, db_column='TIPO_CODIGO')  # Field name made lowercase.
    prci_orden = models.DecimalField(db_column='PRCI_ORDEN', max_digits=3, decimal_places=0)  # Field name made lowercase.
    prci_descripcion = models.CharField(db_column='PRCI_DESCRIPCION', max_length=40)  # Field name made lowercase.
    prci_proceso = models.CharField(db_column='PRCI_PROCESO', max_length=40)  # Field name made lowercase.
    prci_fecha_ultima_ejecucion = models.DateTimeField(db_column='PRCI_FECHA_ULTIMA_EJECUCION', blank=True, null=True)  # Field name made lowercase.
    prci_fecha_proxima_ejecucion = models.DateTimeField(db_column='PRCI_FECHA_PROXIMA_EJECUCION')  # Field name made lowercase.
    prci_fecha_ejecucion = models.DateTimeField(db_column='PRCI_FECHA_EJECUCION')  # Field name made lowercase.
    prci_precierre = models.CharField(db_column='PRCI_PRECIERRE', max_length=1)  # Field name made lowercase.
    prci_periocidad = models.DecimalField(db_column='PRCI_PERIOCIDAD', max_digits=3, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    peri_codigo = models.ForeignKey(Periocidad, models.DO_NOTHING, db_column='PERI_CODIGO', blank=True, null=True)  # Field name made lowercase.
    mosi_codigo_origen = models.DecimalField(db_column='MOSI_CODIGO_ORIGEN', max_digits=2, decimal_places=0, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PROCESOS_CIERRE'
        unique_together = (('empr_codigo', 'mosi_codigo', 'prci_codigo'),)


class ProcesosCierrePc6(models.Model):
    empr_codigo = models.CharField(db_column='EMPR_CODIGO', max_length=10)  # Field name made lowercase.
    mosi_codigo = models.DecimalField(db_column='MOSI_CODIGO', max_digits=2, decimal_places=0)  # Field name made lowercase.
    prci_codigo = models.DecimalField(db_column='PRCI_CODIGO', max_digits=4, decimal_places=0)  # Field name made lowercase.
    etci_codigo = models.DecimalField(db_column='ETCI_CODIGO', max_digits=2, decimal_places=0)  # Field name made lowercase.
    tipo_codigo = models.DecimalField(db_column='TIPO_CODIGO', max_digits=2, decimal_places=0)  # Field name made lowercase.
    prci_orden = models.DecimalField(db_column='PRCI_ORDEN', max_digits=3, decimal_places=0)  # Field name made lowercase.
    prci_descripcion = models.CharField(db_column='PRCI_DESCRIPCION', max_length=40)  # Field name made lowercase.
    prci_proceso = models.CharField(db_column='PRCI_PROCESO', max_length=40)  # Field name made lowercase.
    prci_fecha_ultima_ejecucion = models.DateTimeField(db_column='PRCI_FECHA_ULTIMA_EJECUCION', blank=True, null=True)  # Field name made lowercase.
    prci_fecha_proxima_ejecucion = models.DateTimeField(db_column='PRCI_FECHA_PROXIMA_EJECUCION')  # Field name made lowercase.
    prci_fecha_ejecucion = models.DateTimeField(db_column='PRCI_FECHA_EJECUCION')  # Field name made lowercase.
    prci_precierre = models.CharField(db_column='PRCI_PRECIERRE', max_length=1)  # Field name made lowercase.
    prci_periocidad = models.DecimalField(db_column='PRCI_PERIOCIDAD', max_digits=3, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    peri_codigo = models.DecimalField(db_column='PERI_CODIGO', max_digits=2, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    mosi_codigo_origen = models.DecimalField(db_column='MOSI_CODIGO_ORIGEN', max_digits=2, decimal_places=0, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PROCESOS_CIERRE_PC6'


class ProcesosCierrePc7(models.Model):
    empr_codigo = models.CharField(db_column='EMPR_CODIGO', max_length=10)  # Field name made lowercase.
    mosi_codigo = models.DecimalField(db_column='MOSI_CODIGO', max_digits=2, decimal_places=0)  # Field name made lowercase.
    prci_codigo = models.DecimalField(db_column='PRCI_CODIGO', max_digits=4, decimal_places=0)  # Field name made lowercase.
    etci_codigo = models.DecimalField(db_column='ETCI_CODIGO', max_digits=2, decimal_places=0)  # Field name made lowercase.
    tipo_codigo = models.DecimalField(db_column='TIPO_CODIGO', max_digits=2, decimal_places=0)  # Field name made lowercase.
    prci_orden = models.DecimalField(db_column='PRCI_ORDEN', max_digits=3, decimal_places=0)  # Field name made lowercase.
    prci_descripcion = models.CharField(db_column='PRCI_DESCRIPCION', max_length=40)  # Field name made lowercase.
    prci_proceso = models.CharField(db_column='PRCI_PROCESO', max_length=40)  # Field name made lowercase.
    prci_fecha_ultima_ejecucion = models.DateTimeField(db_column='PRCI_FECHA_ULTIMA_EJECUCION', blank=True, null=True)  # Field name made lowercase.
    prci_fecha_proxima_ejecucion = models.DateTimeField(db_column='PRCI_FECHA_PROXIMA_EJECUCION')  # Field name made lowercase.
    prci_fecha_ejecucion = models.DateTimeField(db_column='PRCI_FECHA_EJECUCION')  # Field name made lowercase.
    prci_precierre = models.CharField(db_column='PRCI_PRECIERRE', max_length=1)  # Field name made lowercase.
    prci_periocidad = models.DecimalField(db_column='PRCI_PERIOCIDAD', max_digits=3, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    peri_codigo = models.DecimalField(db_column='PERI_CODIGO', max_digits=2, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    mosi_codigo_origen = models.DecimalField(db_column='MOSI_CODIGO_ORIGEN', max_digits=2, decimal_places=0, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PROCESOS_CIERRE_PC7'


class ProcesosCierrePc8(models.Model):
    empr_codigo = models.CharField(db_column='EMPR_CODIGO', max_length=10)  # Field name made lowercase.
    mosi_codigo = models.DecimalField(db_column='MOSI_CODIGO', max_digits=2, decimal_places=0)  # Field name made lowercase.
    prci_codigo = models.DecimalField(db_column='PRCI_CODIGO', max_digits=4, decimal_places=0)  # Field name made lowercase.
    etci_codigo = models.DecimalField(db_column='ETCI_CODIGO', max_digits=2, decimal_places=0)  # Field name made lowercase.
    tipo_codigo = models.DecimalField(db_column='TIPO_CODIGO', max_digits=2, decimal_places=0)  # Field name made lowercase.
    prci_orden = models.DecimalField(db_column='PRCI_ORDEN', max_digits=3, decimal_places=0)  # Field name made lowercase.
    prci_descripcion = models.CharField(db_column='PRCI_DESCRIPCION', max_length=40)  # Field name made lowercase.
    prci_proceso = models.CharField(db_column='PRCI_PROCESO', max_length=40)  # Field name made lowercase.
    prci_fecha_ultima_ejecucion = models.DateTimeField(db_column='PRCI_FECHA_ULTIMA_EJECUCION', blank=True, null=True)  # Field name made lowercase.
    prci_fecha_proxima_ejecucion = models.DateTimeField(db_column='PRCI_FECHA_PROXIMA_EJECUCION')  # Field name made lowercase.
    prci_fecha_ejecucion = models.DateTimeField(db_column='PRCI_FECHA_EJECUCION')  # Field name made lowercase.
    prci_precierre = models.CharField(db_column='PRCI_PRECIERRE', max_length=1)  # Field name made lowercase.
    prci_periocidad = models.DecimalField(db_column='PRCI_PERIOCIDAD', max_digits=3, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    peri_codigo = models.DecimalField(db_column='PERI_CODIGO', max_digits=2, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    mosi_codigo_origen = models.DecimalField(db_column='MOSI_CODIGO_ORIGEN', max_digits=2, decimal_places=0, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PROCESOS_CIERRE_PC8'


class ProcesosCierrePc9(models.Model):
    empr_codigo = models.CharField(db_column='EMPR_CODIGO', max_length=10)  # Field name made lowercase.
    mosi_codigo = models.DecimalField(db_column='MOSI_CODIGO', max_digits=2, decimal_places=0)  # Field name made lowercase.
    prci_codigo = models.DecimalField(db_column='PRCI_CODIGO', max_digits=4, decimal_places=0)  # Field name made lowercase.
    etci_codigo = models.DecimalField(db_column='ETCI_CODIGO', max_digits=2, decimal_places=0)  # Field name made lowercase.
    tipo_codigo = models.DecimalField(db_column='TIPO_CODIGO', max_digits=2, decimal_places=0)  # Field name made lowercase.
    prci_orden = models.DecimalField(db_column='PRCI_ORDEN', max_digits=3, decimal_places=0)  # Field name made lowercase.
    prci_descripcion = models.CharField(db_column='PRCI_DESCRIPCION', max_length=40)  # Field name made lowercase.
    prci_proceso = models.CharField(db_column='PRCI_PROCESO', max_length=40)  # Field name made lowercase.
    prci_fecha_ultima_ejecucion = models.DateTimeField(db_column='PRCI_FECHA_ULTIMA_EJECUCION', blank=True, null=True)  # Field name made lowercase.
    prci_fecha_proxima_ejecucion = models.DateTimeField(db_column='PRCI_FECHA_PROXIMA_EJECUCION')  # Field name made lowercase.
    prci_fecha_ejecucion = models.DateTimeField(db_column='PRCI_FECHA_EJECUCION')  # Field name made lowercase.
    prci_precierre = models.CharField(db_column='PRCI_PRECIERRE', max_length=1)  # Field name made lowercase.
    prci_periocidad = models.DecimalField(db_column='PRCI_PERIOCIDAD', max_digits=3, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    peri_codigo = models.DecimalField(db_column='PERI_CODIGO', max_digits=2, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    mosi_codigo_origen = models.DecimalField(db_column='MOSI_CODIGO_ORIGEN', max_digits=2, decimal_places=0, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PROCESOS_CIERRE_PC9'


class Productos(models.Model):
    mosi_codigo = models.DecimalField(db_column='MOSI_CODIGO', max_digits=2, decimal_places=0)  # Field name made lowercase.
    prdc_codigo = models.CharField(db_column='PRDC_CODIGO', max_length=10)  # Field name made lowercase.
    prdc_descripcion = models.CharField(db_column='PRDC_DESCRIPCION', max_length=40)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PRODUCTOS'


class RelacionMonedas(models.Model):
    mone_empresa = models.ForeignKey(Moneda, models.DO_NOTHING, db_column='MONE_EMPRESA', primary_key=True)  # Field name made lowercase.
    mone_transaccion = models.ForeignKey(Moneda, models.DO_NOTHING, db_column='MONE_TRANSACCION')  # Field name made lowercase.
    remo_operacion = models.CharField(db_column='REMO_OPERACION', max_length=1)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'RELACION_MONEDAS'
        unique_together = (('mone_empresa', 'mone_transaccion'),)


class ReplicaTablasComunes(models.Model):
    retc_tabla = models.CharField(db_column='RETC_TABLA', primary_key=True, max_length=40)  # Field name made lowercase.
    retc_vista = models.CharField(db_column='RETC_VISTA', max_length=1)  # Field name made lowercase.
    retc_replica = models.CharField(db_column='RETC_REPLICA', max_length=1)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'REPLICA_TABLAS_COMUNES'


class ResultadosScripts(models.Model):
    cadena = models.CharField(db_column='CADENA', max_length=1000)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'RESULTADOS_SCRIPTS'


class ScriptsSeguridad(models.Model):
    campo1 = models.CharField(max_length=149)
    name = models.CharField(max_length=128)
    xprec = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'SCRIPTS_SEGURIDAD'


class Secuencias(models.Model):
    empr_codigo = models.CharField(db_column='EMPR_CODIGO', primary_key=True, max_length=10)  # Field name made lowercase.
    secu_tabla = models.CharField(db_column='SECU_TABLA', max_length=40)  # Field name made lowercase.
    secu_valor_actual = models.DecimalField(db_column='SECU_VALOR_ACTUAL', max_digits=10, decimal_places=0)  # Field name made lowercase.
    secu_paso = models.DecimalField(db_column='SECU_PASO', max_digits=2, decimal_places=0)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'SECUENCIAS'
        unique_together = (('empr_codigo', 'secu_tabla'),)


class SubTipoEmpresa(models.Model):
    tiem_codigo = models.ForeignKey('TipoEmpresa', models.DO_NOTHING, db_column='TIEM_CODIGO', primary_key=True)  # Field name made lowercase.
    sute_codigo = models.DecimalField(db_column='SUTE_CODIGO', max_digits=3, decimal_places=0)  # Field name made lowercase.
    sute_descripcion = models.CharField(db_column='SUTE_DESCRIPCION', max_length=40)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'SUB_TIPO_EMPRESA'
        unique_together = (('tiem_codigo', 'sute_codigo'),)


class TablasComunesPc(models.Model):
    tcpc_tabla = models.CharField(db_column='TCPC_TABLA', max_length=40)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TABLAS_COMUNES_PC'


class TipoAgencia(models.Model):
    tiag_codigo = models.DecimalField(db_column='TIAG_CODIGO', primary_key=True, max_digits=2, decimal_places=0)  # Field name made lowercase.
    tiag_descripcion = models.CharField(db_column='TIAG_DESCRIPCION', max_length=40)  # Field name made lowercase.
    tiag_centro_canje = models.CharField(db_column='TIAG_CENTRO_CANJE', max_length=2)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TIPO_AGENCIA'


class TipoAsesor(models.Model):
    tias_codigo = models.DecimalField(db_column='TIAS_CODIGO', primary_key=True, max_digits=2, decimal_places=0)  # Field name made lowercase.
    tias_descripcion = models.CharField(db_column='TIAS_DESCRIPCION', max_length=40)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TIPO_ASESOR'


class TipoCotizacion(models.Model):
    tico_codigo = models.DecimalField(db_column='TICO_CODIGO', primary_key=True, max_digits=2, decimal_places=0)  # Field name made lowercase.
    tico_descripcion = models.CharField(db_column='TICO_DESCRIPCION', max_length=40)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TIPO_COTIZACION'


class TipoCuenta(models.Model):
    ticu_codigo = models.DecimalField(db_column='TICU_CODIGO', primary_key=True, max_digits=2, decimal_places=0)  # Field name made lowercase.
    ticu_descripcion = models.CharField(db_column='TICU_DESCRIPCION', max_length=40)  # Field name made lowercase.
    ticu_codigo_alt = models.CharField(db_column='TICU_CODIGO_ALT', max_length=5, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TIPO_CUENTA'


class TipoDeBanca(models.Model):
    tiba_codigo = models.DecimalField(db_column='TIBA_CODIGO', primary_key=True, max_digits=2, decimal_places=0)  # Field name made lowercase.
    tiba_descripcion = models.CharField(db_column='TIBA_DESCRIPCION', max_length=40)  # Field name made lowercase.
    tiba_responsable = models.CharField(db_column='TIBA_RESPONSABLE', max_length=40, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TIPO_DE_BANCA'


class TipoEmpresa(models.Model):
    tiem_codigo = models.DecimalField(db_column='TIEM_CODIGO', primary_key=True, max_digits=4, decimal_places=0)  # Field name made lowercase.
    tiem_descripcion = models.CharField(db_column='TIEM_DESCRIPCION', max_length=40)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TIPO_EMPRESA'


class TipoGrupoAsesor(models.Model):
    gras_codigo = models.DecimalField(db_column='GRAS_CODIGO', primary_key=True, max_digits=3, decimal_places=0)  # Field name made lowercase.
    gras_descripcion = models.CharField(db_column='GRAS_DESCRIPCION', max_length=40)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TIPO_GRUPO_ASESOR'


class TipoPerfil(models.Model):
    tipe_codigo = models.DecimalField(db_column='TIPE_CODIGO', primary_key=True, max_digits=2, decimal_places=0)  # Field name made lowercase.
    tipe_descripcion = models.CharField(db_column='TIPE_DESCRIPCION', max_length=40)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TIPO_PERFIL'


class TipoProceso(models.Model):
    tipo_codigo = models.DecimalField(db_column='TIPO_CODIGO', primary_key=True, max_digits=2, decimal_places=0)  # Field name made lowercase.
    tipo_nombre = models.CharField(db_column='TIPO_NOMBRE', max_length=40)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TIPO_PROCESO'


class Usuario(models.Model):
    usua_codigo = models.CharField(db_column='USUA_CODIGO', primary_key=True, max_length=20)  # Field name made lowercase.
    esus_codigo = models.ForeignKey(EstadoUsuario, models.DO_NOTHING, db_column='ESUS_CODIGO')  # Field name made lowercase.
    usua_nombre = models.CharField(db_column='USUA_NOMBRE', max_length=40)  # Field name made lowercase.
    usua_clave = models.CharField(db_column='USUA_CLAVE', max_length=20)  # Field name made lowercase.
    usua_fecha_creacion = models.DateTimeField(db_column='USUA_FECHA_CREACION')  # Field name made lowercase.
    usua_fecha_inicio = models.DateTimeField(db_column='USUA_FECHA_INICIO')  # Field name made lowercase.
    usua_fecha_fin = models.DateTimeField(db_column='USUA_FECHA_FIN')  # Field name made lowercase.
    usua_login = models.CharField(db_column='USUA_LOGIN', max_length=20)  # Field name made lowercase.
    zona_codigo = models.ForeignKey(CentroDeCosto, models.DO_NOTHING, db_column='ZONA_CODIGO', blank=True, null=True)  # Field name made lowercase.
    empr_codigo = models.ForeignKey(CentroDeCosto, models.DO_NOTHING, db_column='EMPR_CODIGO', blank=True, null=True)  # Field name made lowercase.
    agen_codigo = models.ForeignKey(CentroDeCosto, models.DO_NOTHING, db_column='AGEN_CODIGO', blank=True, null=True)  # Field name made lowercase.
    cetc_codigo = models.ForeignKey(CentroDeCosto, models.DO_NOTHING, db_column='CETC_CODIGO', blank=True, null=True)  # Field name made lowercase.
    usua_identificacion = models.CharField(db_column='USUA_IDENTIFICACION', max_length=15, blank=True, null=True)  # Field name made lowercase.
    usua_periocidad = models.DecimalField(db_column='USUA_PERIOCIDAD', max_digits=2, decimal_places=0)  # Field name made lowercase.
    usua_administrador = models.CharField(db_column='USUA_ADMINISTRADOR', max_length=1)  # Field name made lowercase.
    usua_cargo = models.CharField(db_column='USUA_CARGO', max_length=40, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'USUARIO'


class UsuarioAgencia(models.Model):
    zona_codigo = models.DecimalField(db_column='ZONA_CODIGO', max_digits=4, decimal_places=0)  # Field name made lowercase.
    empr_codigo = models.CharField(db_column='EMPR_CODIGO', max_length=10)  # Field name made lowercase.
    agen_codigo = models.DecimalField(db_column='AGEN_CODIGO', max_digits=4, decimal_places=0)  # Field name made lowercase.
    usua_codigo = models.CharField(db_column='USUA_CODIGO', max_length=20)  # Field name made lowercase.
    usag_principal = models.CharField(db_column='USAG_PRINCIPAL', max_length=2, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'USUARIO_AGENCIA'


class UsuarioCentroDeCosto(models.Model):
    vele_codigo = models.ForeignKey('UsuarioEmpresa', models.DO_NOTHING, db_column='VELE_CODIGO', primary_key=True)  # Field name made lowercase.
    usua_codigo = models.ForeignKey('UsuarioEmpresa', models.DO_NOTHING, db_column='USUA_CODIGO')  # Field name made lowercase.
    empr_codigo = models.ForeignKey('UsuarioEmpresa', models.DO_NOTHING, db_column='EMPR_CODIGO')  # Field name made lowercase.
    zona_codigo = models.ForeignKey(CentroDeCosto, models.DO_NOTHING, db_column='ZONA_CODIGO')  # Field name made lowercase.
    cen_empr_codigo = models.ForeignKey(CentroDeCosto, models.DO_NOTHING, db_column='CEN_EMPR_CODIGO')  # Field name made lowercase.
    agen_codigo = models.ForeignKey(CentroDeCosto, models.DO_NOTHING, db_column='AGEN_CODIGO')  # Field name made lowercase.
    cetc_codigo = models.ForeignKey(CentroDeCosto, models.DO_NOTHING, db_column='CETC_CODIGO')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'USUARIO_CENTRO_DE_COSTO'
        unique_together = (('vele_codigo', 'usua_codigo', 'empr_codigo'),)


class UsuarioEmpresa(models.Model):
    vele_codigo = models.ForeignKey('UsuarioVehiculo', models.DO_NOTHING, db_column='VELE_CODIGO', primary_key=True)  # Field name made lowercase.
    usua_codigo = models.ForeignKey('UsuarioVehiculo', models.DO_NOTHING, db_column='USUA_CODIGO')  # Field name made lowercase.
    empr_codigo = models.ForeignKey(Empresa, models.DO_NOTHING, db_column='EMPR_CODIGO')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'USUARIO_EMPRESA'
        unique_together = (('vele_codigo', 'usua_codigo', 'empr_codigo'),)


class UsuarioModulo(models.Model):
    usua_codigo = models.ForeignKey(Usuario, models.DO_NOTHING, db_column='USUA_CODIGO', primary_key=True)  # Field name made lowercase.
    tipe_codigo = models.ForeignKey(Perfil, models.DO_NOTHING, db_column='TIPE_CODIGO')  # Field name made lowercase.
    mosi_codigo = models.ForeignKey(Perfil, models.DO_NOTHING, db_column='MOSI_CODIGO')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'USUARIO_MODULO'
        unique_together = (('usua_codigo', 'tipe_codigo', 'mosi_codigo'),)


class UsuarioVehiculo(models.Model):
    vele_codigo = models.ForeignKey('VehiculoLegal', models.DO_NOTHING, db_column='VELE_CODIGO', primary_key=True)  # Field name made lowercase.
    usua_codigo = models.ForeignKey(Usuario, models.DO_NOTHING, db_column='USUA_CODIGO')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'USUARIO_VEHICULO'
        unique_together = (('vele_codigo', 'usua_codigo'),)


class VehiculoLegal(models.Model):
    vele_codigo = models.CharField(db_column='VELE_CODIGO', primary_key=True, max_length=3)  # Field name made lowercase.
    pais_codigo = models.ForeignKey(Pais, models.DO_NOTHING, db_column='PAIS_CODIGO')  # Field name made lowercase.
    vele_descripcion = models.CharField(db_column='VELE_DESCRIPCION', max_length=40)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'VEHICULO_LEGAL'


class Ventana(models.Model):
    mosi_codigo = models.ForeignKey(ModuloSistema, models.DO_NOTHING, db_column='MOSI_CODIGO', primary_key=True)  # Field name made lowercase.
    vent_codigo = models.CharField(db_column='VENT_CODIGO', max_length=40)  # Field name made lowercase.
    vent_descripcion = models.CharField(db_column='VENT_DESCRIPCION', max_length=40)  # Field name made lowercase.
    vent_ventana = models.CharField(db_column='VENT_VENTANA', max_length=40)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'VENTANA'
        unique_together = (('mosi_codigo', 'vent_codigo'),)


class VentanaCarga(models.Model):
    mosi_codigo = models.DecimalField(db_column='MOSI_CODIGO', max_digits=2, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    vent_codigo = models.CharField(db_column='VENT_CODIGO', max_length=40, blank=True, null=True)  # Field name made lowercase.
    vent_descripcion = models.CharField(db_column='VENT_DESCRIPCION', max_length=40, blank=True, null=True)  # Field name made lowercase.
    vent_ventana = models.CharField(db_column='VENT_VENTANA', max_length=40, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'VENTANA_CARGA'


class VentanaResultadosPrecierre(models.Model):
    empr_codigo = models.ForeignKey(ModuloEmpresa, models.DO_NOTHING, db_column='EMPR_CODIGO', primary_key=True)  # Field name made lowercase.
    mosi_codigo = models.ForeignKey(ModuloEmpresa, models.DO_NOTHING, db_column='MOSI_CODIGO')  # Field name made lowercase.
    vrpr_ventana = models.CharField(db_column='VRPR_VENTANA', max_length=40, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'VENTANA_RESULTADOS_PRECIERRE'
        unique_together = (('empr_codigo', 'mosi_codigo'),)


class Zona(models.Model):
    zona_codigo = models.DecimalField(db_column='ZONA_CODIGO', primary_key=True, max_digits=4, decimal_places=0)  # Field name made lowercase.
    pais_codigo = models.ForeignKey(Pais, models.DO_NOTHING, db_column='PAIS_CODIGO')  # Field name made lowercase.
    zona_descripcion = models.CharField(db_column='ZONA_DESCRIPCION', max_length=40)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ZONA'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Pbcatcol(models.Model):
    pbc_tnam = models.CharField(max_length=30, blank=True, null=True)
    pbc_tid = models.IntegerField(blank=True, null=True)
    pbc_ownr = models.CharField(max_length=30, blank=True, null=True)
    pbc_cnam = models.CharField(max_length=30, blank=True, null=True)
    pbc_cid = models.SmallIntegerField(blank=True, null=True)
    pbc_labl = models.CharField(max_length=254, blank=True, null=True)
    pbc_lpos = models.SmallIntegerField(blank=True, null=True)
    pbc_hdr = models.CharField(max_length=254, blank=True, null=True)
    pbc_hpos = models.SmallIntegerField(blank=True, null=True)
    pbc_jtfy = models.SmallIntegerField(blank=True, null=True)
    pbc_mask = models.CharField(max_length=31, blank=True, null=True)
    pbc_case = models.SmallIntegerField(blank=True, null=True)
    pbc_hght = models.SmallIntegerField(blank=True, null=True)
    pbc_wdth = models.SmallIntegerField(blank=True, null=True)
    pbc_ptrn = models.CharField(max_length=31, blank=True, null=True)
    pbc_bmap = models.CharField(max_length=1, blank=True, null=True)
    pbc_init = models.CharField(max_length=254, blank=True, null=True)
    pbc_cmnt = models.CharField(max_length=254, blank=True, null=True)
    pbc_edit = models.CharField(max_length=31, blank=True, null=True)
    pbc_tag = models.CharField(max_length=254, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pbcatcol'


class Pbcatedt(models.Model):
    pbe_name = models.CharField(max_length=30)
    pbe_edit = models.CharField(max_length=254, blank=True, null=True)
    pbe_type = models.SmallIntegerField()
    pbe_cntr = models.IntegerField(blank=True, null=True)
    pbe_seqn = models.SmallIntegerField()
    pbe_flag = models.IntegerField(blank=True, null=True)
    pbe_work = models.CharField(max_length=32, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pbcatedt'


class Pbcatfmt(models.Model):
    pbf_name = models.CharField(max_length=30)
    pbf_frmt = models.CharField(max_length=254)
    pbf_type = models.SmallIntegerField()
    pbf_cntr = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pbcatfmt'


class Pbcattbl(models.Model):
    pbt_tnam = models.CharField(max_length=30, blank=True, null=True)
    pbt_tid = models.IntegerField(blank=True, null=True)
    pbt_ownr = models.CharField(max_length=30, blank=True, null=True)
    pbd_fhgt = models.SmallIntegerField(blank=True, null=True)
    pbd_fwgt = models.SmallIntegerField(blank=True, null=True)
    pbd_fitl = models.CharField(max_length=1, blank=True, null=True)
    pbd_funl = models.CharField(max_length=1, blank=True, null=True)
    pbd_fchr = models.SmallIntegerField(blank=True, null=True)
    pbd_fptc = models.SmallIntegerField(blank=True, null=True)
    pbd_ffce = models.CharField(max_length=18, blank=True, null=True)
    pbh_fhgt = models.SmallIntegerField(blank=True, null=True)
    pbh_fwgt = models.SmallIntegerField(blank=True, null=True)
    pbh_fitl = models.CharField(max_length=1, blank=True, null=True)
    pbh_funl = models.CharField(max_length=1, blank=True, null=True)
    pbh_fchr = models.SmallIntegerField(blank=True, null=True)
    pbh_fptc = models.SmallIntegerField(blank=True, null=True)
    pbh_ffce = models.CharField(max_length=18, blank=True, null=True)
    pbl_fhgt = models.SmallIntegerField(blank=True, null=True)
    pbl_fwgt = models.SmallIntegerField(blank=True, null=True)
    pbl_fitl = models.CharField(max_length=1, blank=True, null=True)
    pbl_funl = models.CharField(max_length=1, blank=True, null=True)
    pbl_fchr = models.SmallIntegerField(blank=True, null=True)
    pbl_fptc = models.SmallIntegerField(blank=True, null=True)
    pbl_ffce = models.CharField(max_length=18, blank=True, null=True)
    pbt_cmnt = models.CharField(max_length=254, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pbcattbl'


class Pbcatvld(models.Model):
    pbv_name = models.CharField(max_length=30)
    pbv_vald = models.CharField(max_length=254)
    pbv_type = models.SmallIntegerField()
    pbv_cntr = models.IntegerField(blank=True, null=True)
    pbv_msg = models.CharField(max_length=254, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pbcatvld'


class ProcesosCartera(models.Model):
    col001 = models.CharField(db_column='Col001', max_length=255, blank=True, null=True)  # Field name made lowercase.
    col002 = models.CharField(db_column='Col002', max_length=255, blank=True, null=True)  # Field name made lowercase.
    col003 = models.CharField(db_column='Col003', max_length=255, blank=True, null=True)  # Field name made lowercase.
    col004 = models.CharField(db_column='Col004', max_length=255, blank=True, null=True)  # Field name made lowercase.
    col005 = models.CharField(db_column='Col005', max_length=255, blank=True, null=True)  # Field name made lowercase.
    col006 = models.CharField(db_column='Col006', max_length=255, blank=True, null=True)  # Field name made lowercase.
    col007 = models.CharField(db_column='Col007', max_length=255, blank=True, null=True)  # Field name made lowercase.
    col008 = models.CharField(db_column='Col008', max_length=255, blank=True, null=True)  # Field name made lowercase.
    col009 = models.CharField(db_column='Col009', max_length=255, blank=True, null=True)  # Field name made lowercase.
    col010 = models.CharField(db_column='Col010', max_length=255, blank=True, null=True)  # Field name made lowercase.
    col011 = models.CharField(db_column='Col011', max_length=255, blank=True, null=True)  # Field name made lowercase.
    col012 = models.CharField(db_column='Col012', max_length=255, blank=True, null=True)  # Field name made lowercase.
    col013 = models.CharField(db_column='Col013', max_length=255, blank=True, null=True)  # Field name made lowercase.
    col014 = models.CharField(db_column='Col014', max_length=255, blank=True, null=True)  # Field name made lowercase.
    col015 = models.CharField(db_column='Col015', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'procesos_cartera'


class Sysdiagrams(models.Model):
    name = models.CharField(max_length=128)
    principal_id = models.IntegerField()
    diagram_id = models.AutoField(primary_key=True)
    version = models.IntegerField(blank=True, null=True)
    definition = models.BinaryField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sysdiagrams'
        unique_together = (('principal_id', 'name'),)


class TablasLogCab(models.Model):
    tlgc_codigo = models.DecimalField(max_digits=9, decimal_places=0)
    tlgc_tabla = models.CharField(max_length=40)
    tlgc_fecha = models.DateTimeField()
    tlgc_usuario = models.CharField(max_length=20)
    tlgc_estado = models.CharField(max_length=1)
    tlgc_tipo = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'tablas_log_cab'


class TablasLogDet(models.Model):
    tlgc_codigo = models.DecimalField(max_digits=9, decimal_places=0)
    tlgd_codigo = models.AutoField()
    tlgd_campo = models.CharField(max_length=40)
    tlgd_valor_antes = models.CharField(max_length=40, blank=True, null=True)
    tlgd_valor_despues = models.CharField(max_length=40, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tablas_log_det'


class TempReport(models.Model):
    cadena = models.CharField(max_length=300)
    cantidad = models.DecimalField(max_digits=5, decimal_places=0)

    class Meta:
        managed = False
        db_table = 'temp_report'


class VentanaTablaTmp(models.Model):
    mosi_codigo = models.DecimalField(max_digits=5, decimal_places=0, blank=True, null=True)
    vent_ventana = models.CharField(max_length=40, blank=True, null=True)
    vtab_tabla = models.CharField(max_length=40, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ventana_tabla_tmp'


class VentanaTablas(models.Model):
    vtab_codigo = models.DecimalField(max_digits=9, decimal_places=0)
    mosi_codigo = models.DecimalField(max_digits=5, decimal_places=0)
    vent_codigo = models.CharField(max_length=40)
    vent_ventana = models.CharField(max_length=40)
    vtab_tabla = models.CharField(max_length=40)

    class Meta:
        managed = False
        db_table = 'ventana_tablas'
