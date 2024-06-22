import { createSlice, PayloadAction } from '@reduxjs/toolkit';

interface UserState {
    loggedIn: boolean;
    username: string | null;
}

const initialState: UserState = {
    loggedIn: false,
    username: null,
};

const userSlice = createSlice({
    name: 'user',
    initialState,
    reducers: {
        login: (state, action: PayloadAction<string>) => {
        state.loggedIn = true;
        state.username = action.payload;
        },
        logout: (state) => {
        state.loggedIn = false;
        state.username = null;
        },
    },
});

export const { login, logout } = userSlice.actions;
export default userSlice.reducer;
