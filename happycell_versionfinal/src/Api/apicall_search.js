import { API } from '../config';

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