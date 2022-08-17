from .models import Agencia, Asesor, Banco, Canton, Ciudad, Cliente, ClienteAsesor, ClienteJuridico, ClienteNatural, CuentaBancariaCliente, Direccion, Empresa, EstadoCivil, GrupoEconomico, Nacionalidad, NivelInstruccion, Observacion, Pais, Parroquia, Profesion, Provincia, Secuencia, Sexo, SituacionLaboral, Telefono, TipoAsesor, TipoBanca, TipoCliente, TipoCuenta, TipoDireccion, TipoDocumento, TipoEmpresa, TipoObservacion, TipoProyecto, TipoRol, TipoTelefono, TipoVinculo, Usuario, Vinculo, Vivienda, Zona, ActividadEconomica # Modelos

def validarCliente(data):
    success = True
    log = {}
    indexLog = 0
    log[indexLog] = "==================================================================="
    indexLog += 1


    nacionalidad = Nacionalidad.objects.using('clientes').filter(NACI_CODIGO = data['NACI_CODIGO']).first()
    if nacionalidad:
        log[indexLog] = f"Nacionalidad válido: {data['NACI_CODIGO']}, DESCRIPCIÓN: {nacionalidad.NACI_DESCRIPCION}"
        indexLog += 1
    else:
        log[indexLog] = f"Nacionalidad no válido: {data['NACI_CODIGO']}. Revisar ficha técnica"
        indexLog += 1
        success = False

    tipoCliente = TipoCliente.objects.using('clientes').filter(TICL_CODIGO = data['TICL_CODIGO']).first()
    if tipoCliente:
        log[indexLog] = f"Tipo Cliente válido: {data['TICL_CODIGO']}, DESCRIPCIÓN: {tipoCliente.TICL_DESCRIPCION}"
        indexLog += 1
    else:
        log[indexLog] = f"Tipo Cliente no válido: {data['TICL_CODIGO']}. Revisar ficha técnica"
        indexLog += 1
        success = False

    tipoDocument = TipoDocumento.objects.using('clientes').filter(TIDO_CODIGO = data['TIDO_CODIGO']).first()
    if tipoDocument:
        log[indexLog] = f"Tipo Documento válido: {data['TIDO_CODIGO']}, DESCRIPCIÓN: {tipoDocument.TIDO_DESCRIPCION}"
        indexLog += 1
    else:
        log[indexLog] = f"Tipo Documento no válido: {data['TIDO_CODIGO']}. Revisar ficha técnica"
        indexLog += 1
        success = False

    actividadEconomica = ActividadEconomica.objects.using('clientes').filter(ACTI_CODIGO = data['ACTI_CODIGO']).first()
    if actividadEconomica:
        log[indexLog] = f"Actividad Económica válido: {data['ACTI_CODIGO']}, DESCRIPCIÓN: {actividadEconomica.ACTI_DESCRIPCION}"
        indexLog += 1
    else:
        log[indexLog] = f"Actividad Económica no válido: {data['ACTI_CODIGO']}. Revisar ficha técnica"
        indexLog += 1
        success = False

    asesor = Asesor.objects.using('clientes').filter(ASES_CODIGO = data['ASES_CODIGO']).first()
    if asesor:
        log[indexLog] = f"Asesor válido: {data['ASES_CODIGO']}, DESCRIPCIÓN: {asesor.ASES_NOMBRE}"
        indexLog += 1
    else:
        log[indexLog] = f"Asesor no válido: {data['ASES_CODIGO']}. Revisar ficha técnica"
        indexLog += 1
        success = False

    tipoRol = TipoRol.objects.using('clientes').filter(TIRO_CODIGO = data['CLIE_TIPO_ROL']).first()
    if tipoRol:
        log[indexLog] = f"Tipo Rol válido: {data['CLIE_TIPO_ROL']}, DESCRIPCIÓN: {tipoRol.TIROL_DESCRIPCIÒN}"
        indexLog += 1
    else:
        log[indexLog] = f"Tipo Rol no válido: {data['CLIE_TIPO_ROL']}. Revisar ficha técnica"
        indexLog += 1
        success = False

    return {'status': success, 'log': log }

def validarClienteNatural(data):
    success = True
    log = {}
    indexLog = 0
    log[indexLog] = "==================================================================="
    indexLog += 1


    profesion = Profesion.objects.using('clientes').filter(PROF_CODIGO = data['PROF_CODIGO']).first()
    if profesion:
        log[indexLog] = f"Profesion válido: {data['PROF_CODIGO']}, DESCRIPCIÓN: {profesion.PROF_DESCRIPCION}"
        indexLog += 1
    else:
        log[indexLog] = f"Profesion no válido: {data['PROF_CODIGO']}. Revisar ficha técnica"
        indexLog += 1
        success = False

    nivelInstruccion = NivelInstruccion.objects.using('clientes').filter(NIIN_CODIGO = data['NIIN_CODIGO']).first()
    if nivelInstruccion:
        log[indexLog] = f"Nivel de Instruccion válido: {data['NIIN_CODIGO']}, DESCRIPCIÓN: {nivelInstruccion.NIIN_DESCRIPCION}"
        indexLog += 1
    else:
        log[indexLog] = f"Nivel de Instruccion no válido: {data['NIIN_CODIGO']}. Revisar ficha técnica"
        indexLog += 1
        success = False

    sexo = Sexo.objects.using('clientes').filter(SEXO_CODIGO = data['SEXO_CODIGO']).first()
    if sexo:
        log[indexLog] = f"Sexo válido: {data['SEXO_CODIGO']}, DESCRIPCIÓN: {sexo.SEXO_DESCRIPCION}"
        indexLog += 1
    else:
        log[indexLog] = f"Sexo no válido: {data['SEXO_CODIGO']}. Revisar ficha técnica"
        indexLog += 1
        success = False

    estadoCivil = EstadoCivil.objects.using('clientes').filter(ESCI_CODIGO = data['ESCI_CODIGO']).first()
    if estadoCivil:
        log[indexLog] = f"Estado Civil válido: {data['ESCI_CODIGO']}, DESCRIPCIÓN: {estadoCivil.ESCI_DESCRIPCION}"
        indexLog += 1
    else:
        log[indexLog] = f"Estado Civil no válido: {data['ESCI_CODIGO']}. Revisar ficha técnica"
        indexLog += 1
        success = False

    tipoVivienda = Vivienda.objects.using('clientes').filter(VIVI_CODIGO = data['CLIE_TIPO_VIVIENDA']).first()
    if tipoVivienda:
        log[indexLog] = f"Vivienda válido: {data['CLIE_TIPO_VIVIENDA']}, DESCRIPCIÓN: {tipoVivienda.VIVI_DESCRIPCION}"
        indexLog += 1
    else:
        log[indexLog] = f"Vivienda no válido: {data['CLIE_TIPO_VIVIENDA']}. Revisar ficha técnica"
        indexLog += 1
        success = False

    situacionLaboral = SituacionLaboral.objects.using('clientes').filter(SITL_CODIGO = data['CLIE_SITUACION_LABORAL']).first()
    if situacionLaboral:
        log[indexLog] = f"Situación Laboral válido: {data['CLIE_SITUACION_LABORAL']}, DESCRIPCIÓN: {situacionLaboral.SITL_DESCRIPCION}"
        indexLog += 1
    else:
        log[indexLog] = f"Situación Laboral no válido: {data['CLIE_SITUACION_LABORAL']}. Revisar ficha técnica"
        indexLog += 1
        success = False

    return {'status': success, 'log': log }

def validarClienteJuridico(data):
    success = True
    log = {}
    indexLog = 0
    log[indexLog] = "==================================================================="
    indexLog += 1


    tipoEmpresa = TipoEmpresa.objects.using('clientes').filter(TIEM_CODIGO = data['TIEM_CODIGO']).first()
    if tipoEmpresa:
        log[indexLog] = f"Profesion válido: {data['TIEM_CODIGO']}, DESCRIPCIÓN: {tipoEmpresa.TIEM_DESCRIPCION}"
        indexLog += 1
    else:
        log[indexLog] = f"Profesion no válido: {data['TIEM_CODIGO']}. Revisar ficha técnica"
        indexLog += 1
        success = False

    grupoEconomico = GrupoEconomico.objects.using('clientes').filter(GREC_CODIGO = data['GREC_CODIGO']).first()
    if grupoEconomico:
        log[indexLog] = f"Nivel de Instruccion válido: {data['GREC_CODIGO']}, DESCRIPCIÓN: {grupoEconomico.GREC__DESCRIPCION}"
        indexLog += 1
    else:
        log[indexLog] = f"Nivel de Instruccion no válido: {data['GREC_CODIGO']}. Revisar ficha técnica"
        indexLog += 1
        success = False
    
    return {'status': success, 'log': log }

def validarDireccion(data):
    success = True
    log = {}
    indexLog = 0
    log[indexLog] = "==================================================================="
    indexLog += 1


    parroquia = Parroquia.objects.using('clientes').filter(PARR_CODIGO = data['parr_codigo']).first()
    if parroquia:
        canton = Parroquia.objects.using('clientes').filter(PARR_CODIGO = data['parr_codigo'], CANT_CODIGO = data['cant_codigo']).first()
        if canton:
            log[indexLog] = f"Parroquia y Cantón válidos: {data['parr_codigo']}"
            indexLog += 1
        else:
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
        if provincia:
            log[indexLog] = f"Cantón válido: {data['cant_codigo']}, DESCRIPCIÓN: {canton.CANT_NOMBRE}"
            indexLog += 1
        else:
            log[indexLog] = f"Provincia no válida: {data['prov_codigo']} para el Cantón: {canton.CANT_CODIGO}. Revisar ficha técnica"
            indexLog += 1
            success = False
    else:
        log[indexLog] = f"Cantón no válido: {data['cant_codigo']}. Revisar ficha técnica"
        indexLog += 1
        success = False

    return {'status': success, 'log': log }

def validarTelefono(data):
    success = True
    log = {}
    indexLog = 0
    log[indexLog] = "==================================================================="
    indexLog += 1


    tipo = TipoTelefono.objects.using('clientes').filter(TITE_CODIGO = data['TITE_CODIGO']).first()
    if tipo:
        log[indexLog] = f"Tipo de Teléfono válido: {data['TITE_CODIGO']}, DESCRIPCIÓN: {tipo.TITE_DESCRIPCION}"
        indexLog += 1
    else:
        log[indexLog] = f"Tipo de Teléfono no válido: {data['TITE_CODIGO']}. Revisar ficha técnica"
        indexLog += 1
        success = False

    return {'status': success, 'log': log }

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

    return {'status': success, 'log': log }

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

def validarObservacion(data):
    success = True
    log = {}
    indexLog = 0
    log[indexLog] = "==================================================================="
    indexLog += 1


    tipo = TipoObservacion.objects.using('clientes').filter(TIOC_CODIGO = data['TIOC_CODIGO']).first()
    if tipo:
        log[indexLog] = f"Tipo de Observacion válido: {data['TIOC_CODIGO']}, DESCRIPCIÓN: {tipo.TIOC_DESCRI}"
        indexLog += 1
    else:
        log[indexLog] = f"Tipo de Observacion no válido: {data['TIOC_CODIGO']}. Revisar ficha técnica"
        indexLog += 1
        success = False

    return {'status': success, 'log': log }

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

    return {'status': success, 'log': log }

def validarVinculo(data):
    success = True
    log = {}
    indexLog = 0
    log[indexLog] = "==================================================================="
    indexLog += 1

    tipo = TipoVinculo.objects.using('clientes').filter(TIVI_CODIGO = data['TIVI_CODIGO'], TICL_CODIGO = data['TICL_CODIGO']).first()
    if tipo:
        log[indexLog] = f"Tipo de Vínculo válido: {data['TIVI_CODIGO']}, DESCRIPCIÓN: {tipo.TIVI_DESCRIPCION}"
        indexLog += 1
    else:
        log[indexLog] = f"Tipo de Vínculo no válido o no corresponde con el Tipo de Cliente: {data['TIVI_CODIGO']}. Revisar ficha técnica"
        indexLog += 1
        success = False

    nacionalidad = Nacionalidad.objects.using('clientes').filter(NACI_CODIGO = data['NACI_CODIGO']).first()
    if nacionalidad:
        log[indexLog] = f"Nacionalidad válido: {data['NACI_CODIGO']}, DESCRIPCIÓN: {nacionalidad.NACI_DESCRIPCION}"
        indexLog += 1
    else:
        log[indexLog] = f"Nacionalidad no válido: {data['NACI_CODIGO']}. Revisar ficha técnica"
        indexLog += 1
        success = False

    profesion = Profesion.objects.using('clientes').filter(PROF_CODIGO = data['PROF_CODIGO']).first()
    if profesion:
        log[indexLog] = f"Profesion válido: {data['PROF_CODIGO']}, DESCRIPCIÓN: {profesion.PROF_DESCRIPCION}"
        indexLog += 1
    else:
        log[indexLog] = f"Profesion no válido: {data['PROF_CODIGO']}. Revisar ficha técnica"
        indexLog += 1
        success = False

    estadoCivil = EstadoCivil.objects.using('clientes').filter(ESCI_CODIGO = data['esci_codigo']).first()
    if estadoCivil:
        log[indexLog] = f"Estado Civil válido: {data['esci_codigo']}, DESCRIPCIÓN: {estadoCivil.ESCI_DESCRIPCION}"
        indexLog += 1
    else:
        log[indexLog] = f"Estado Civil no válido: {data['esci_codigo']}. Revisar ficha técnica"
        indexLog += 1
        success = False

    return {'status': success, 'log': log }

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
