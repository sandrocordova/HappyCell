import { configureStore } from '@reduxjs/toolkit'
import { setupListeners } from '@reduxjs/toolkit/query/react';

import themeOptionsReducer from '../features/themeOptions/themeOptions';
import clientsReducer from '../features/clients/clientsSlice';
import catalogsSlice from '../features/catalogs/catalogsSlice';
import { apicall_catalogs } from '../Api/apicall_catalogs';

export const store = configureStore({
    reducer: {
        themeOptions: themeOptionsReducer,
        client: clientsReducer,
        catalogs: catalogsSlice,
        [apicall_catalogs.reducerPath]: apicall_catalogs.reducer
    },
    // Adding the api middleware enables caching, invalidation, polling,
    // and other useful features of `rtk-query`.
    middleware: (getDefaultMiddleware) =>
        getDefaultMiddleware().concat(apicall_catalogs.middleware),
})

// optional, but required for refetchOnFocus/refetchOnReconnect behaviors
// see `setupListeners` docs - takes an optional callback as the 2nd arg for customization
setupListeners(store.dispatch)