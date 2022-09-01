import { createApi, fetchBaseQuery } from '@reduxjs/toolkit/query/react'
import { API } from '../config';

export const apicall_catalogs = createApi({
    reducerPath: 'getCatalogs',
    baseQuery: fetchBaseQuery({ baseUrl: API }),
    endpoints: (builder) => ({
        getAllCatologs: builder.query({
            query: () => `/cat/view`,
        }),
    }),
})

export const { useGetAllCatologsQuery, useLazyGetAllCatologsQuery } = apicall_catalogs;