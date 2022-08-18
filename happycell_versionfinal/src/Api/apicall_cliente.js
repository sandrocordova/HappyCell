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