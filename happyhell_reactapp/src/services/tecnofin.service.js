import axios from 'axios';

const TecnofinApi = () => {
    const baseUrl = process.env.REACT_APP_TECNOFIN_URL_API;
    const requestUrl = `user/mainteiner`;

    const promise = axios.get(`${baseUrl}${requestUrl}`);

    const dataPromise = promise.then((res) => res.data);

    return dataPromise;
}

export default TecnofinApi;