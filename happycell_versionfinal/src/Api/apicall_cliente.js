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

/* 
    Funcion para obtener los catalogos de la API
*/
export const getCatalogos = async () => {
    try {
        const response = await fetch(`${API}/cat/view`);
        const data = await response.json();
        return data;
    } catch (error) {
        return { error: "Error al obtener los catálogos" }
    }
}

/* 
    Funcion para actializar un cliente Natural
    * Se deve de enviar el token de autenticacion para validar al usuario
    TODO: implementar el token en el header del fetch. Utilizar Authorization: <tipo> <credenciales>
*/
export const updateClienteNatural = async (clientCodigo, values) => {
    const {
        TIDO_CODIGO,
        CLIE_TIPO_PROYECTO,
        NACI_CODIGO,
        ACTI_CODIGO,
        CLIE_NOMBRE_CORRESPONDENCIA,
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
            CLIE_CODIGO: clientCodigo,
            NACI_CODIGO,
            ACTI_CODIGO,
            CLIE_NOMBRE_CORRESPONDENCIA,
            TIDO_CODIGO,
            CLIE_TIPO_PROYECTO
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
    try {
        const response = await fetch(`${API}/cliente/cliente`, {
            method: 'PUT',
            headers: {
                Accept: 'application/json',
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(data)
        });
        return await response.json();
    } catch (err) {
        console.log(err);
    }
}

/* 
    Funcion para actializar un cliente Juridico
    * Se deve de enviar el token de autenticacion para validar al usuario
    TODO: implementar el token en el header del fetch. Utilizar Authorization: <tipo> <credenciales>
*/
export const updateClienteJuridico = async (clientCodigo, values) => {
    const {
        CLIE_NOMBRE_CORRESPONDENCIA,
        NACI_CODIGO,
        CLIE_NOMBRE,
        TIDO_CODIGO,
        ACTI_CODIGO,
        CLIE_TIPO_PROYECTO,
        TIEM_CODIGO,
        CLJU_RAZON_SOCIAL,
        CLJU_NOMBRE_PUBLICITARIO } = values

    const data = {
        cliente: {
            CLIE_CODIGO: clientCodigo,
            NACI_CODIGO,
            ACTI_CODIGO,
            CLIE_NOMBRE_CORRESPONDENCIA,
            TIDO_CODIGO,
            CLIE_TIPO_PROYECTO
        },
        detalle: {
            CLIE_NOMBRE,
            TIEM_CODIGO,
            CLJU_RAZON_SOCIAL,
            CLJU_NOMBRE_PUBLICITARIO
        }
    }
    try {
        const response = await fetch(`${API}/cliente/cliente`, {
            method: 'PUT',
            headers: {
                Accept: 'application/json',
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(data)
        });
        return await response.json();
    } catch (err) {
        console.log(err);
    }
}

/* 
    Funcion para actializar un cliente Juridico
    * Se deve de enviar el token de autenticacion para validar al usuario
    TODO: implementar el token en el header del fetch. Utilizar Authorization: <tipo> <credenciales>
*/
export const updateTelefono = async (data) => {
    try {
        const response = await fetch(`${API}/api-dir/v1/telefono`, {
            method: 'PUT',
            headers: {
                Accept: 'application/json',
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(data)
        });
        return await response.json();
    } catch (err) {
        console.log(err);
    }
}
/* 
    Funcion para actializar un cliente Juridico
    * Se deve de enviar el token de autenticacion para validar al usuario
    TODO: implementar el token en el header del fetch. Utilizar Authorization: <tipo> <credenciales>
*/
export const updateDirecciones = async (data) => {
    console.log(data)
    try {
        const response = await fetch(`${API}/api-dir/v1/direccion`, {
            method: 'PUT',
            headers: {
                Accept: 'application/json',
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(data)
        });
        return await response.json();
    } catch (err) {
        console.log(err);
    }
}