import { configureStore, combineReducers } from '@reduxjs/toolkit'
import { setupListeners } from '@reduxjs/toolkit/query/react';
import {
    persistStore,
    persistReducer,
    FLUSH,
    REHYDRATE,
    PAUSE,
    PERSIST,
    PURGE,
    REGISTER,
} from "redux-persist";
import storage from "redux-persist/lib/storage";


import themeOptionsReducer from '../features/themeOptions/themeOptions';
import clientsReducer from '../features/clients/clientsSlice';
import catalogsSlice from '../features/catalogs/catalogsSlice';
import { apicall_catalogs } from '../Api/apicall_catalogs';

const persistConfig = {
    key: "root",
    version: 1,
    storage,
    blacklist: ['getCatalogs'],
};

const rootReducer = combineReducers({
    themeOptions: themeOptionsReducer,
    client: clientsReducer,
    catalogs: catalogsSlice,
    [apicall_catalogs.reducerPath]: apicall_catalogs.reducer
});

const persistedReducer = persistReducer(persistConfig, rootReducer);

export const store = configureStore({
    reducer: persistedReducer,
    // Adding the api middleware enables caching, invalidation, polling,
    // and other useful features of `rtk-query`.
    middleware: (getDefaultMiddleware) =>
        getDefaultMiddleware({
            serializableCheck: {
                ignoredActions: [FLUSH, REHYDRATE, PAUSE, PERSIST, PURGE, REGISTER],
            },
        }).concat(apicall_catalogs.middleware),
})

export let persistor = persistStore(store)
// optional, but required for refetchOnFocus/refetchOnReconnect behaviors
// see `setupListeners` docs - takes an optional callback as the 2nd arg for customization
setupListeners(store.dispatch)