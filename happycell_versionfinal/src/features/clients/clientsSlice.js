import { createSlice } from '@reduxjs/toolkit'

const initialState = [{}]

export const clientSlice = createSlice({
    name: 'client',
    initialState,
    reducers: {
        addClient: (state, action) => {
            state[0] = action.payload
        },
        decrement: (state) => {
            state.value -= 1
        },
        incrementByAmount: (state, action) => {
            state.value += action.payload
        },
    },
})

// Action creators are generated for each case reducer function
export const { addClient, decrement, incrementByAmount } = clientSlice.actions

export default clientSlice.reducer