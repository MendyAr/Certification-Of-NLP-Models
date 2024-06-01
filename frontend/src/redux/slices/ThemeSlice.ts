import { PayloadAction, createSlice } from "@reduxjs/toolkit";

export type ThemeState = { isLight: boolean };

const initialState: ThemeState = { isLight: true };

export const ThemeSlice = createSlice({
    name: "theme",
    initialState,
    reducers: {
        setTheme: (state, action: PayloadAction<boolean>) => {
            state.isLight = action.payload;
        },
    },
});

export const { setTheme } = ThemeSlice.actions;

export default ThemeSlice.reducer;
