import { API } from '../config';

// metodo para buscar clientes
export const searchClient = async (text, page) => {
    const mySearch = { data: text }
    try {
        const res = await fetch(`${API}/cliente/search?page=${page}`, {
            method: 'POST',
            headers: {
                Accept: 'application/json',
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(mySearch)
        });
        const data = await res.json();
        return data;
    } catch (error) {
        return error;
    }
}

// metodo para obtener el detalle del cliente
export const searchClientDetail = async (type, clieCodigo) => {
    const mySearch = {
        CLIE_CODIGO: clieCodigo,
        TICL_CODIGO: type
    }
    try {
        const res = await fetch(`${API}/cliente/detalle`, {
            method: 'POST',
            headers: {
                Accept: 'application/json',
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(mySearch)
        });
        const data = await res.json();
        return data;
    } catch (error) {
        return error;
    }
}