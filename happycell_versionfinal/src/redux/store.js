import { configureStore } from '@reduxjs/toolkit'
import themeOptionsReducer from '../features/themeOptions/themeOptions';
import clientsReducer from '../features/clients/clientsSlice';

export const store = configureStore({
    reducer: {
        themeOptions: themeOptionsReducer,
        client: clientsReducer
    },
})