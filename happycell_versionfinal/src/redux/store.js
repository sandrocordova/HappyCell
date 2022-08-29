import { configureStore } from '@reduxjs/toolkit'
import themeOptionsReducer from '../features/themeOptions/themeOptions';

export const store = configureStore({
    reducer: {
        themeOptions: themeOptionsReducer
    },
})