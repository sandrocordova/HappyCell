import { createSlice } from '@reduxjs/toolkit'

const initialState = [{}]

export const catalogsSlice = createSlice({
    name: 'catalogs',
    initialState,
    reducers: {
        addCatalogos: (state, action) => {
            state[0] = action.payload
        },
        getNacionalidad: (state, action) => {
            //console.log(state)
            // const res = state.find(nac => nac === "nacionalidad")
            // console.log(res)
            //return { value: 1, laberl: "NO SE" }
        },
        incrementByAmount: (state, action) => {
            state.value += action.payload
        },
    },
})

// Action creators are generated for each case reducer function
export const { addCatalogos, getNacionalidad } = catalogsSlice.actions

export default catalogsSlice.reducer