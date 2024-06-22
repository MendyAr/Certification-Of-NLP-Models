import { configureStore } from "@reduxjs/toolkit";
import ThemeSlice from "./slices/ThemeSlice";
import authReducer from './slices/authSlice';
import userReducer from './slices/userSlice';

export const store = configureStore({
    reducer: {
        theme: ThemeSlice,
        auth: authReducer,
        user: userReducer,
    },
    middleware: (getDefaultMiddleware) =>
        getDefaultMiddleware({
            serializableCheck: false,
        }),
});

export type RootState = ReturnType<typeof store.getState>;
export type AppDispatch = typeof store.dispatch;

// export {};
