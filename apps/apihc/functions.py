from .choices import ERRCLI_CODES
from apps.catalog.models import Agencia, Banco, Canton, Ciudad, CuentaBalance, GrupoEconomico, Nacionalidad, Parroquia, TipoAgencia, TipoAsesor, TipoBanca, TipoCliente, TipoCuenta, TipoCuentaBalance, TipoDireccion, TipoDocumento, TipoEmpresa, TipoObservacion, TipoRol, TipoTelefono, TipoVinculo, Zona, ActividadEconomica, Profesion, NivelInstruccion, Sexo, EstadoCivil, Vivienda, SituacionLaboral
from .models import Asesor, BalanceCliente, Cliente, ClienteAsesor, ClienteJuridico, ClienteNatural, CuentaBancariaCliente, Direccion, Empresa, Observacion, Telefono, Usuario, Vinculo

def validarCliente(data):
    success = True
    log = {}
    indexLog = 0

    nacionalidad = Nacionalidad.objects.using('clientes').filter(NACI_CODIGO = data['NACI_CODIGO']).first()
    if nacionalidad is None:
        nacionalidaderrorCodes = ERRCLI_CODES(data['NACI_CODIGO'], "Nacionalidad", "")
        log[indexLog] = nacionalidaderrorCodes['ERRCLI001']
        indexLog += 1    
        success = False

    tipoCliente = TipoCliente.objects.using('clientes').filter(TICL_CODIGO = data['TICL_CODIGO']).first()
    if tipoCliente is None:
        tipoClienteerrorCodes = ERRCLI_CODES(data['TICL_CODIGO'], "Tipo Cliente", "")
        log[indexLog] = tipoClienteerrorCodes['ERRCLI001']
        indexLog += 1    
        success = False

    tipoDocument = TipoDocumento.objects.using('clientes').filter(TIDO_CODIGO = data['TIDO_CODIGO']).first()
    if tipoDocument is None:
        tipoDocumenterrorCodes = ERRCLI_CODES(data['TIDO_CODIGO'], "Tipo Documento", "")
        log[indexLog] = tipoDocumenterrorCodes['ERRCLI001']
        indexLog += 1    
        success = False

    actividadEconomica = ActividadEconomica.objects.using('clientes').filter(ACTI_CODIGO = data['ACTI_CODIGO']).first()
    if actividadEconomica is None:
        actividadEconomicaerrorCodes = ERRCLI_CODES(data['ACTI_CODIGO'], "Actividad Economica", "")
        log[indexLog] = actividadEconomicaerrorCodes['ERRCLI001']
        indexLog += 1    
        success = False

    asesor = Asesor.objects.using('clientes').filter(ASES_CODIGO = data['ASES_CODIGO']).first()
    if asesor is None:
        asesorerrorCodes = ERRCLI_CODES(data['ASES_CODIGO'], "Asesor", "")
        log[indexLog] = asesorerrorCodes['ERRCLI001']
        indexLog += 1    
        success = False

    tipoRol = TipoRol.objects.using('clientes').filter(TIRO_CODIGO = data['CLIE_TIPO_ROL']).first()
    if tipoRol is None:
        tipoRolerrorCodes = ERRCLI_CODES(data['CLIE_TIPO_ROL'], "Tipo Rol", "")
        log[indexLog] = tipoRolerrorCodes['ERRCLI001']
        indexLog += 1    
        success = False

    return {
        'status': success, 
        'message': log
        }

def validarClienteNatural(data):
    success = True
    log = {}
    indexLog = 0

    profesion = Profesion.objects.using('clientes').filter(PROF_CODIGO = data['PROF_CODIGO']).first()
    if profesion is None:
        profesionerrorCodes = ERRCLI_CODES(data['PROF_CODIGO'], "Profesion", "")
        log[indexLog] = profesionerrorCodes['ERRCLI001']
        indexLog += 1   
        success = False
    nivelInstruccion = NivelInstruccion.objects.using('clientes').filter(NIIN_CODIGO = data['NIIN_CODIGO']).first()
    if nivelInstruccion is None:
        nivelInstruccionerrorCodes = ERRCLI_CODES(data['NIIN_CODIGO'], "Nivel Instruccion", "")
        log[indexLog] = nivelInstruccionerrorCodes['ERRCLI001']
        indexLog += 1   
        success = False
    sexo = Sexo.objects.using('clientes').filter(SEXO_CODIGO = data['SEXO_CODIGO']).first()
    if sexo is None:
        sexoerrorCodes = ERRCLI_CODES(data['SEXO_CODIGO'], "Sexo", "")
        log[indexLog] = sexoerrorCodes['ERRCLI001']
        indexLog += 1   
        success = False
    estadoCivil = EstadoCivil.objects.using('clientes').filter(ESCI_CODIGO = data['ESCI_CODIGO']).first()
    if estadoCivil is None:
        estadoCivilerrorCodes = ERRCLI_CODES(data['ESCI_CODIGO'], "Estado Civil", "")
        log[indexLog] = estadoCivilerrorCodes['ERRCLI001']
        indexLog += 1   
        success = False
    tipoVivienda = Vivienda.objects.using('clientes').filter(VIVI_CODIGO = data['CLIE_TIPO_VIVIENDA']).first()
    if tipoVivienda is None:
        tipoViviendaerrorCodes = ERRCLI_CODES(data['CLIE_TIPO_VIVIENDA'], "Vivienda", "")
        log[indexLog] = tipoViviendaerrorCodes['ERRCLI001']
        indexLog += 1   
        success = False
    situacionLaboral = SituacionLaboral.objects.using('clientes').filter(SITL_CODIGO = data['CLIE_SITUACION_LABORAL']).first()
    if situacionLaboral is None:
        situacionLaboralerrorCodes = ERRCLI_CODES(data['CLIE_SITUACION_LABORAL'], "Situacion Laboral", "")
        log[indexLog] = situacionLaboralerrorCodes['ERRCLI001']
        indexLog += 1   
        success = False
    return {'status': success, 'message': log }

def validarClienteJuridico(data):
    success = True
    indexLog = 0
    log = {}

    tipoEmpresa = TipoEmpresa.objects.using('clientes').filter(TIEM_CODIGO = data['TIEM_CODIGO']).first()
    if tipoEmpresa is None:
        tipoEmpresaerrorCodes = ERRCLI_CODES(data['TIEM_CODIGO'], "Tipo Empresa", "")
        log[indexLog] = tipoEmpresaerrorCodes['ERRCLI001']
        success = False
    grupoEconomico = GrupoEconomico.objects.using('clientes').filter(GREC_CODIGO = data['GREC_CODIGO']).first()
    if grupoEconomico is None:
        grupoEconomicoerrorCodes = ERRCLI_CODES(data['GREC_CODIGO'], "Grupo Economico", "")
        log[indexLog] = grupoEconomicoerrorCodes['ERRCLI001']
        success = False
    
    return {'status': success, 'message': log }

def validarDireccion(data):
    success = True
    log = {}
    indexLog = 0

    parroquia = Parroquia.objects.using('clientes').filter(PARR_CODIGO = data['parr_codigo']).first()
    if parroquia:
        canton = Parroquia.objects.using('clientes').filter(PARR_CODIGO = data['parr_codigo'], CANT_CODIGO = data['cant_codigo']).first()
        if canton is None:
            log[indexLog] = f"Cantón no válido: {data['cant_codigo']} para la Parroquia: {parroquia.PARR_CODIGO}. Revisar ficha técnica"
            indexLog += 1
            success = False
    else:
        log[indexLog] = f"Parroquia no válida: {data['parr_codigo']}. Revisar ficha técnica"
        indexLog += 1
        success = False

    canton = Canton.objects.using('clientes').filter(CANT_CODIGO = data['cant_codigo']).first()
    if canton:
        provincia = Canton.objects.using('clientes').filter(PROV_CODIGO = data['prov_codigo'], CANT_CODIGO = data['cant_codigo']).first()
        if provincia is None:
            log[indexLog] = f"Provincia no válida: {data['prov_codigo']} para el Cantón: {canton.CANT_CODIGO}. Revisar ficha técnica"
            indexLog += 1
            success = False
    else:
        log[indexLog] = f"Cantón no válido: {data['cant_codigo']}. Revisar ficha técnica"
        indexLog += 1
        success = False

    tipo = TipoDireccion.objects.using('clientes').filter(TIDE_CODIGO = data['TIDE_CODIGO']).first()
    if tipo is None:
        log[indexLog] = f"Tipo de Dirección no válido: {data['TIDE_CODIGO']}. Revisar ficha técnica"
        indexLog += 1
        success = False

    return {'status': success, 'message': log }

def validarTelefono(data):
    success = True
    log = {}
    indexLog = 0
    telefono = data['TELE_NUMERO']

    if telefono.isdigit():
        if len(telefono) < 10:
            log[indexLog] = f"Teléfono no válido: {data['TELE_NUMERO']}. Revisar ficha técnica"
            indexLog += 1
            success = False
    else:
        log[indexLog] = f"Teléfono no válido: {data['TELE_NUMERO']}. Revisar ficha técnica"
        indexLog += 1
        success = False

    tipo = TipoTelefono.objects.using('clientes').filter(TITE_CODIGO = data['TITE_CODIGO']).first()
    if tipo is None:
        log[indexLog] = f"Tipo de Teléfono no existe: {data['TITE_CODIGO']}. Revisar ficha técnica"
        indexLog += 1
        success = False

    direccion = Direccion.objects.using('clientes').filter(DIRE_CODIGO = data['DIRE_CODIGO'], CLIE_CODIGO = data['CLIE_CODIGO']).first()
    if direccion is None:
        log[indexLog] = f"DIRE_CODIGO {data['DIRE_CODIGO']} no corresponde a Cliente: {data['CLIE_CODIGO']}. Revisar ficha técnica"
        indexLog += 1
        success = False

    tipoD = TipoDireccion.objects.using('clientes').filter(TIDE_CODIGO = data['TIDE_CODIGO']).first()
    if tipoD is None:
        log[indexLog] = f"Tipo de Dirección no existe: {data['TIDE_CODIGO']}. Revisar ficha técnica"
        indexLog += 1
        success = False
    elif tipoD.TIDE_CODIGO == 2:
        log[indexLog] = f"Tipo de Dirección no válido: {data['TIDE_CODIGO']}. Revisar ficha técnica"
        indexLog += 1
        success = False
    

    return {'status': success, 'message': log }

def validarAsesor(data):
    success = True
    log = {}
    indexLog = 0
    log[indexLog] = "==================================================================="
    indexLog += 1


    zona = Zona.objects.using('clientes').filter(ZONA_CODIGO = data['ZONA_CODIGO']).first()
    if zona:
        log[indexLog] = f"Zona válido: {data['ZONA_CODIGO']}, DESCRIPCIÓN: {zona.ZONA_DESCRIPCION}"
        indexLog += 1
    else:
        log[indexLog] = f"Zona no válido: {data['ZONA_CODIGO']}. Revisar ficha técnica"
        indexLog += 1
        success = False

    agencia = Agencia.objects.using('clientes').filter(AGEN_CODIGO = data['AGEN_CODIGO']).first()
    if agencia:
        log[indexLog] = f"Agencia válido: {data['AGEN_CODIGO']}, DESCRIPCIÓN: {agencia.AGEN_DESCRIPCION}"
        indexLog += 1
    else:
        log[indexLog] = f"Agencia no válido: {data['AGEN_CODIGO']}. Revisar ficha técnica"
        indexLog += 1
        success = False

    usuario = Usuario.objects.filter(USUA_CODIGO = data['USUA_CODIGO']).first()
    if usuario:
        log[indexLog] = f"Usuario válido: {data['USUA_CODIGO']}, DESCRIPCIÓN: {usuario.USUA_NOMBRE}"
        indexLog += 1
    else:
        log[indexLog] = f"Usuario no válido: {data['USUA_CODIGO']}. Revisar ficha técnica"
        indexLog += 1
        log[indexLog] = f"Como el ASES_CODIGO es indispensable para guardar cliente, el proceso se ha cancelado."
        indexLog += 1
        success = False

    return {'status': success, 'message': log }

def validarAsesorExiste(data):
    result = False
    asesor = Asesor.objects.using('clientes').filter(AGEN_CODIGO = data['AGEN_CODIGO'], USUA_CODIGO = data['USUA_CODIGO'], ASES_NOMBRE = data['ASES_NOMBRE']).first()
    if asesor: 
        result = True
        id = asesor.ASES_CODIGO
    else:
        lastId = Asesor.objects.using('clientes').order_by('-ASES_CODIGO').first()
        id = lastId.ASES_CODIGO + 1

    return {
        'result': result,
        'id': id
        }

def validarClienteAsesor(data):
    success = True
    log = {}
    indexLog = 0

    asesor = Asesor.objects.using('clientes').filter(ASES_CODIGO = data, EMPR_CODIGO = 8).first()
    if asesor is None:
        log[indexLog] = f"Asesor no existe: {data}. Revisar ficha técnica"
        indexLog += 1
        success = False

    return {'status': success, 'message': log }

def validarObservacion(data):
    success = True
    log = {}
    indexLog = 0

    tipo = TipoObservacion.objects.using('clientes').filter(TIOC_CODIGO = data['TIOC_CODIGO']).first()
    if tipo:
        log[indexLog] = f"Tipo de Observacion válido: {data['TIOC_CODIGO']}, DESCRIPCIÓN: {tipo.TIOC_DESCRI}"
        indexLog += 1
    else:
        log[indexLog] = f"Tipo de Observacion no válido: {data['TIOC_CODIGO']}. Revisar ficha técnica"
        indexLog += 1
        success = False

    return {'status': success, 'message': log }

def validarCuenta(data):
    success = True
    log = {}
    indexLog = 0
    log[indexLog] = "==================================================================="
    indexLog += 1


    tipo = TipoCuenta.objects.using('clientes').filter(TICU_CODIGO = data['TICU_CODIGO']).first()
    if tipo:
        log[indexLog] = f"Tipo de Cuenta válido: {data['TICU_CODIGO']}, DESCRIPCIÓN: {tipo.TICU_DESCRIPCION}"
        indexLog += 1
    else:
        log[indexLog] = f"Tipo de Cuenta no válido: {data['TICU_CODIGO']}. Revisar ficha técnica"
        indexLog += 1
        success = False

    banco = Banco.objects.using('clientes').filter(BANC_CODIGO = data['BANC_CODIGO']).first()
    if banco:
        log[indexLog] = f"Banco válido: {data['BANC_CODIGO']}, DESCRIPCIÓN: {banco.BANC_DESCRIPCION}"
        indexLog += 1
    else:
        log[indexLog] = f"Banco no válido: {data['BANC_CODIGO']}. Revisar ficha técnica"
        indexLog += 1
        success = False

    return {'status': success, 'message': log }

def validarVinculo(data):
    success = True
    log = {}
    indexLog = 0

    tipo = TipoVinculo.objects.using('clientes').filter(TIVI_CODIGO = data['TIVI_CODIGO'], TICL_CODIGO = data['TICL_CODIGO']).first()
    if tipo is None:
        log[indexLog] = f"Tipo de Vínculo no válido o no corresponde con el Tipo de Cliente: {data['TIVI_CODIGO']}. Revisar ficha técnica"
        indexLog += 1
        success = False 

    nacionalidad = Nacionalidad.objects.using('clientes').filter(NACI_CODIGO = data['NACI_CODIGO']).first()
    if nacionalidad is None:
        log[indexLog] = f"Nacionalidad no válido: {data['NACI_CODIGO']}. Revisar ficha técnica"
        indexLog += 1
        success = False

    profesion = Profesion.objects.using('clientes').filter(PROF_CODIGO = data['PROF_CODIGO']).first()
    if profesion is None:
        log[indexLog] = f"Profesion no válido: {data['PROF_CODIGO']}. Revisar ficha técnica"
        indexLog += 1
        success = False

    estadoCivil = EstadoCivil.objects.using('clientes').filter(ESCI_CODIGO = data['esci_codigo']).first()
    if estadoCivil is None:
        log[indexLog] = f"Estado Civil no válido: {data['esci_codigo']}. Revisar ficha técnica"
        indexLog += 1
        success = False

    ciudad = Ciudad.objects.using('clientes').filter(CIUD_CODIGO = data['CIUD_CODIGO']).first()
    if ciudad is None:
        log[indexLog] = f"Ciudad no válida: {data['CIUD_CODIGO']}. Revisar ficha técnica"
        indexLog += 1
        success = False

    return {'status': success, 'message': log }

def guardarCliente(data):
    clienteSave = Cliente(**data)
    clienteSave.save(using = 'clientes', force_insert = True)
    return {'success': True, 'message': f"Cliente guardado con el CLIE_CODIGO: {data['CLIE_CODIGO']}"}

def guardarClienteNatural(data):
    clienteNSave = ClienteNatural(**data)
    clienteNSave.save(using = 'clientes', force_insert = True)
    return {'success': True, 'message': f"Cliente Natural guardado con el CLIE_CODIGO: {data['CLIE_CODIGO']}"}

def guardarClienteJuridico(data):
    clienteJSave = ClienteJuridico(**data)
    clienteJSave.save(using = 'clientes', force_insert = True)
    return {'success': True, 'message': f"Cliente Juridico guardado con el CLIE_CODIGO: {data['CLIE_CODIGO']}"}

def guardarDireccion(data):
    direccionSave = Direccion(**data)
    direccionSave.save(using = 'clientes', force_insert = True)
    return {'success': True, 'message': f"Dirección de Cliente guardada con el DIRE_CODIGO: {data['DIRE_CODIGO']}"}

def guardarTelefono(data):
    telefonoSave = Telefono(**data)
    telefonoSave.save(using = 'clientes', force_insert = True)
    return {'success': True, 'message': f"Teléfono de Cliente guardado con el TELE_CODIGO: {data['TELE_CODIGO']} y DIRE_CODIGO: {data['DIRE_CODIGO']}"}

def guardarAsesor(data):
    asesorSave = Asesor(**data)
    asesorSave.save(using = 'clientes', force_insert = True)
    return {'success': True, 'message':f"Asesor guardado con el ASES_CODIGO: {data['ASES_CODIGO']}"}

def guardarAsesorCliente(data):
    asesorSave = ClienteAsesor(**data)
    asesorSave.save(using = 'clientes', force_insert = True)
    return {'success': True, 'message':f"Asesor de Cliente guardado con el ASES_CODIGO: {data['ASES_CODIGO']}"}

def guardarObservacion(data):
    observacionSave = Observacion(**data)
    observacionSave.save(using = 'clientes', force_insert = True)
    return {'success': True, 'message':f"Observacion de Cliente guardada con el OBCL_CODIGO: {data['OBCL_CODIGO']}"}

def guardarCuentaBancaria(data):
    cuentaBancariaSave = CuentaBancariaCliente(**data)
    cuentaBancariaSave.save(using = 'clientes', force_insert = True)
    return {'success': True, 'message':f"Cuenta Bancaria de Cliente guardada con el CUBC_CODIGO: {data['CUBC_CODIGO']}"}

def guardarVinculo(data):
    vinculoSave = Vinculo(**data)
    vinculoSave.save(using = 'clientes', force_insert = True)
    return {'success': True, 'message':f"Vínculo de Cliente guardado con el VINC_CODIGO: {data['VINC_CODIGO']}"}

def actualizarCliente(data, cliente):
    cambios = 0

    if cliente.TIDO_CODIGO != data['TIDO_CODIGO']:
        Cliente.objects.using('clientes').filter(CLIE_CODIGO = cliente.CLIE_CODIGO).update(TIDO_CODIGO = data['TIDO_CODIGO'])
        cambios += 1
        Cliente.objects.using('clientes').filter(CLIE_CODIGO = cliente.CLIE_CODIGO).update(CLIE_IDENTIFICACION = data['CLIE_IDENTIFICACION'])
        cambios += 1
    if cliente.ACTI_CODIGO != data['ACTI_CODIGO']:
        Cliente.objects.using('clientes').filter(CLIE_CODIGO = cliente.CLIE_CODIGO).update(ACTI_CODIGO = data['ACTI_CODIGO'])
        cambios += 1
    if cliente.CLIE_NOMBRE_CORRESPONDENCIA != data['CLIE_NOMBRE_CORRESPONDENCIA']:
        Cliente.objects.using('clientes').filter(CLIE_CODIGO = cliente.CLIE_CODIGO).update(CLIE_NOMBRE_CORRESPONDENCIA = data['CLIE_NOMBRE_CORRESPONDENCIA'])
        cambios += 1

    return cambios

def actualizarClienteNatural(data, cliente):
    cambios = 0
    
    if cliente.PROF_CODIGO != data['PROF_CODIGO']:
        ClienteNatural.objects.using('clientes').filter(CLIE_CODIGO = cliente.CLIE_CODIGO).update(PROF_CODIGO = data['PROF_CODIGO'])
        cambios += 1
    if cliente.NIIN_CODIGO != data['NIIN_CODIGO']:
        ClienteNatural.objects.using('clientes').filter(CLIE_CODIGO = cliente.CLIE_CODIGO).update(NIIN_CODIGO = data['NIIN_CODIGO'])
        cambios += 1
    if cliente.SEXO_CODIGO != data['SEXO_CODIGO']:
        ClienteNatural.objects.using('clientes').filter(CLIE_CODIGO = cliente.CLIE_CODIGO).update(SEXO_CODIGO = data['SEXO_CODIGO'])
        cambios += 1
    if cliente.ESCI_CODIGO != data['ESCI_CODIGO']:
        ClienteNatural.objects.using('clientes').filter(CLIE_CODIGO = cliente.CLIE_CODIGO).update(ESCI_CODIGO = data['ESCI_CODIGO'])
        cambios += 1
    if cliente.CLIE_TIPO_VIVIENDA != data['CLIE_TIPO_VIVIENDA']:
        ClienteNatural.objects.using('clientes').filter(CLIE_CODIGO = cliente.CLIE_CODIGO).update(CLIE_TIPO_VIVIENDA = data['CLIE_TIPO_VIVIENDA'])
        cambios += 1
    if cliente.CLIE_SITUACION_LABORAL != data['CLIE_SITUACION_LABORAL']:
        ClienteNatural.objects.using('clientes').filter(CLIE_CODIGO = cliente.CLIE_CODIGO).update(CLIE_SITUACION_LABORAL = data['CLIE_SITUACION_LABORAL'])
        cambios += 1
    if cliente.CLNA_EXPIRA_PASAPORTE != data['CLNA_EXPIRA_PASAPORTE']:
        ClienteNatural.objects.using('clientes').filter(CLIE_CODIGO = cliente.CLIE_CODIGO).update(CLNA_EXPIRA_PASAPORTE = data['CLNA_EXPIRA_PASAPORTE'])
        cambios += 1
    if cliente.CLNA_EMPRESA_TRABAJA != data['CLNA_EMPRESA_TRABAJA']:
        ClienteNatural.objects.using('clientes').filter(CLIE_CODIGO = cliente.CLIE_CODIGO).update(CLNA_EMPRESA_TRABAJA = data['CLNA_EMPRESA_TRABAJA'])
        cambios += 1

    return cambios

def actualizarClienteJuridico(data, cliente):
    cambios = 0

    if cliente.TIEM_CODIGO != data['TIEM_CODIGO']:
        ClienteJuridico.objects.using('clientes').filter(CLIE_CODIGO = cliente.CLIE_CODIGO).update(TIEM_CODIGO = data['TIEM_CODIGO'])
        cambios += 1
    if cliente.GREC_CODIGO != data['GREC_CODIGO']:
        ClienteJuridico.objects.using('clientes').filter(CLIE_CODIGO = cliente.CLIE_CODIGO).update(GREC_CODIGO = data['GREC_CODIGO'])
        cambios += 1
    if cliente.CLJU_NOMBRE_PUBLICITARIO != data['CLJU_NOMBRE_PUBLICITARIO']:
        ClienteJuridico.objects.using('clientes').filter(CLIE_CODIGO = cliente.CLIE_CODIGO).update(CLJU_NOMBRE_PUBLICITARIO = data['CLJU_NOMBRE_PUBLICITARIO'])
        cambios += 1
    if cliente.CLJU_RAZON_SOCIAL != data['CLJU_RAZON_SOCIAL']:
        ClienteJuridico.objects.using('clientes').filter(CLIE_CODIGO = cliente.CLIE_CODIGO).update(CLJU_RAZON_SOCIAL = data['CLJU_RAZON_SOCIAL'])
        cambios += 1
    if cliente.CLJU_REPRESENTANTE != data['CLJU_REPRESENTANTE']:
        ClienteJuridico.objects.using('clientes').filter(CLIE_CODIGO = cliente.CLIE_CODIGO).update(CLJU_REPRESENTANTE = data['CLJU_REPRESENTANTE'])
        cambios += 1

    return cambios

def actualizarDireccion(data, direccion):
    cambios = 0

    if direccion.DIRE_DESCRIPCION != data['DIRE_DESCRIPCION']:
        Direccion.objects.using('clientes').filter(CLIE_CODIGO = data['CLIE_CODIGO'], DIRE_CODIGO = data['DIRE_CODIGO']).update(DIRE_DESCRIPCION = data['DIRE_DESCRIPCION'])
        cambios += 1
    if direccion.prov_codigo != data['prov_codigo']:
        Direccion.objects.using('clientes').filter(CLIE_CODIGO = data['CLIE_CODIGO'], DIRE_CODIGO = data['DIRE_CODIGO']).update(prov_codigo = data['prov_codigo'])
        cambios += 1
    if direccion.cant_codigo != data['cant_codigo']:
        Direccion.objects.using('clientes').filter(CLIE_CODIGO = data['CLIE_CODIGO'], DIRE_CODIGO = data['DIRE_CODIGO']).update(cant_codigo = data['cant_codigo'])
        cambios += 1
    if direccion.parr_codigo != data['parr_codigo']:
        Direccion.objects.using('clientes').filter(CLIE_CODIGO = data['CLIE_CODIGO'], DIRE_CODIGO = data['DIRE_CODIGO']).update(parr_codigo = data['parr_codigo'])
        cambios += 1

    return cambios

def actualizarTelefono(data, telefono):
    cambios = 0

    if telefono.TELE_NUMERO != data['TELE_NUMERO']:
        Telefono.objects.using('clientes').filter(CLIE_CODIGO = data['CLIE_CODIGO'], DIRE_CODIGO = data['DIRE_CODIGO'], TELE_CODIGO = data['TELE_CODIGO']).update(TELE_NUMERO = data['TELE_NUMERO'])
        cambios += 1
        
    return cambios

def actualizarVinculo(data, vinculo):
    cambios = 0

    if vinculo.TIVI_CODIGO != data['TIVI_CODIGO']:
        Vinculo.objects.using('clientes').filter(CLIE_CODIGO = data['CLIE_CODIGO'], VINC_CODIGO = data['VINC_CODIGO']).update(TIVI_CODIGO = data['TIVI_CODIGO'])
        cambios += 1
    if vinculo.VINC_IDENTIFICACION != data['VINC_IDENTIFICACION']:
        Vinculo.objects.using('clientes').filter(CLIE_CODIGO = data['CLIE_CODIGO'], VINC_CODIGO = data['VINC_CODIGO']).update(VINC_IDENTIFICACION = data['VINC_IDENTIFICACION'])
        cambios += 1
    if vinculo.VINC_NOMBRE != data['VINC_NOMBRE']:
        Vinculo.objects.using('clientes').filter(CLIE_CODIGO = data['CLIE_CODIGO'], VINC_CODIGO = data['VINC_CODIGO']).update(VINC_NOMBRE = data['VINC_NOMBRE'])
        cambios += 1
    if vinculo.VINC_DIRECCION != data['VINC_DIRECCION']:
        Vinculo.objects.using('clientes').filter(CLIE_CODIGO = data['CLIE_CODIGO'], VINC_CODIGO = data['VINC_CODIGO']).update(VINC_DIRECCION = data['VINC_DIRECCION'])
        cambios += 1
    if vinculo.VINC_TELEFONO != data['VINC_TELEFONO']:
        Vinculo.objects.using('clientes').filter(CLIE_CODIGO = data['CLIE_CODIGO'], VINC_CODIGO = data['VINC_CODIGO']).update(VINC_TELEFONO = data['VINC_TELEFONO'])
        cambios += 1
    if vinculo.NACI_CODIGO != data['NACI_CODIGO']:
        Vinculo.objects.using('clientes').filter(CLIE_CODIGO = data['CLIE_CODIGO'], VINC_CODIGO = data['VINC_CODIGO']).update(NACI_CODIGO = data['NACI_CODIGO'])
        cambios += 1
    if vinculo.PROF_CODIGO != data['PROF_CODIGO']:
        Vinculo.objects.using('clientes').filter(CLIE_CODIGO = data['CLIE_CODIGO'], VINC_CODIGO = data['VINC_CODIGO']).update(PROF_CODIGO = data['PROF_CODIGO'])
        cambios += 1
    if vinculo.CIUD_CODIGO != data['CIUD_CODIGO']:
        Vinculo.objects.using('clientes').filter(CLIE_CODIGO = data['CLIE_CODIGO'], VINC_CODIGO = data['VINC_CODIGO']).update(CIUD_CODIGO = data['CIUD_CODIGO'])
        cambios += 1
    if vinculo.VINC_CARGO != data['VINC_CARGO']:
        Vinculo.objects.using('clientes').filter(CLIE_CODIGO = data['CLIE_CODIGO'], VINC_CODIGO = data['VINC_CODIGO']).update(VINC_CARGO = data['VINC_CARGO'])
        cambios += 1
    if vinculo.esci_codigo != data['esci_codigo']:
        Vinculo.objects.using('clientes').filter(CLIE_CODIGO = data['CLIE_CODIGO'], VINC_CODIGO = data['VINC_CODIGO']).update(esci_codigo = data['esci_codigo'])
        cambios += 1
        
    return cambios


def cedula_is_ok(cedula):
    if cedula.isdigit():
        if len(cedula)>=10:
            return True
        return False
    return False
