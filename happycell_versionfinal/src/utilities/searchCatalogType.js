
export const buscarNacionalidad = (id, nacionalidadLista) => {
    const res = nacionalidadLista.find(n => n.NACI_CODIGO === id)
    return { value: res?.NACI_CODIGO, label: res?.NACI_DESCRIPCION }
}

export const buscarTipoClase = (id, tipoLista) => {
    const res = tipoLista.find(n => n.CLIE_TIPO === id)
    return { value: res?.CLIE_TIPO, label: res?.DESC_TIPO }
}

export const buscarActividadEconomica = (id, actividadLista) => {
    const res = actividadLista.find(n => n.ACTI_CODIGO === id)
    return { value: res?.ACTI_CODIGO, label: res?.ACTI_DESCRIPCION }
}

export const buscarCategoriaCliente = (id, categoriaLista) => {
    const res = categoriaLista.find(n => n.COD_TIPO_PROYECTO === id)
    return { value: res?.COD_TIPO_PROYECTO, label: res?.DESC_TIPO_PROYECTO }
}

export const buscarTipoRol = (id, tipoLista) => {
    const res = tipoLista.find(n => n.TIRO_CODIGO === id)
    return { value: res?.TIRO_CODIGO, label: res?.TIROL_DESCRIPCION }
}

export const buscarTipoEmpresa = (id, tipoLista) => {
    const res = tipoLista.find(n => n.TIEM_CODIGO === id)
    return { value: res?.TIEM_CODIGO, label: res?.TIEM_DESCRIPCION }
}

export const buscarTipoSexo = (id, tipoLista) => {
    const res = tipoLista.find(n => n.SEXO_CODIGO === id)
    return { value: res?.SEXO_CODIGO, label: res?.SEXO_DESCRIPCION }
}

export const buscarProfesion = (id, tipoLista) => {
    const res = tipoLista.find(n => n.PROF_CODIGO === id)
    return { value: res?.PROF_CODIGO, label: res?.PROF_DESCRIPCION }
}

export const buscarEstadoCivil = (id, tipoLista) => {
    const res = tipoLista.find(n => n.ESCI_CODIGO === id)
    return { value: res?.ESCI_CODIGO, label: res?.ESCI_DESCRIPCION }
}

export const buscarSituLaboral = (id, tipoLista) => {
    const res = tipoLista.find(n => n.SITL_CODIGO === id)
    return { value: res?.SITL_CODIGO, label: res?.SITL_DESCRIPCION }
}

export const buscarTipoVivienda = (id, tipoLista) => {
    const res = tipoLista.find(n => n.VIVI_CODIGO === id)
    return { value: res?.VIVI_CODIGO, label: res?.VIVI_DESCRIPCION }
}