import { API } from '../config';

/**
 * Ejemplo de metodo para obtener clientes
 * ! Eliminar o modificar el metodo 
 */
export const getClients = async (cedula, nombre) => {
    try {
        const res = await fetch(`${API}/cliente?cedula=${cedula}&nombre=${nombre}`);
        const data = await res.json();
        return data;
    } catch (error) {
        return error;
    }
}

export const getCatalogos = async () => {
    try {
        const response = await fetch(`${API}/cat/view`);
        const data = await response.json();
        return data;
    } catch (error) {
        return { error: "Error al obtener los catálogos" }
    }
}

export const updateClienteNatural = (values) => {
    // return fetch(
    //     `${API}/cat/view`,
    //     {
    //         method: 'GET'
    //     }
    // )
    //     .then(response => {
    //         return response.json()
    //     })
    //     .catch(err => console.log(err))
    const { NACI_CODIGO,
        ACTI_CODIGO,
        CLIE_NOMBRE_CORRESPONDENCIA,
        clie_estado,
        SEXO_CODIGO,
        PROF_CODIGO,
        ESCI_CODIGO,
        CLNA_NOMBRE1,
        CLNA_NOMBRE2,
        CLNA_APELLIDO1,
        CLNA_APELLIDO2,
        CLNA_FECHA_NACIMIENTO,
        CLNA_LUGAR_NACIMIENTO,
        CLIE_TIPO_VIVIENDA,
        CLIE_SITUACION_LABORAL,
        CLNA_EXPIRA_PASAPORTE,
        CLNA_INICIO_RESIDENCIA,
        CLNA_NUM_CARGAS,
        CLNA_EMPRESA_TRABAJA,
        CLNA_INICIO_INGRESOS, } = values

    const data = {
        cliente: {
            NACI_CODIGO,
            ACTI_CODIGO,
            CLIE_NOMBRE_CORRESPONDENCIA,
            clie_estado,
        },
        detalle: {
            SEXO_CODIGO,
            PROF_CODIGO,
            ESCI_CODIGO,
            CLNA_NOMBRE1,
            CLNA_NOMBRE2,
            CLNA_APELLIDO1,
            CLNA_APELLIDO2,
            CLNA_FECHA_NACIMIENTO,
            CLNA_LUGAR_NACIMIENTO,
            CLIE_TIPO_VIVIENDA,
            CLIE_SITUACION_LABORAL,
            CLNA_EXPIRA_PASAPORTE,
            CLNA_INICIO_RESIDENCIA,
            CLNA_NUM_CARGAS,
            CLNA_EMPRESA_TRABAJA,
            CLNA_INICIO_INGRESOS,
        }
    }
    console.log(data)
    //return true
}