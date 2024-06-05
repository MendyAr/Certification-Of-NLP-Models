import { configureStore } from "@reduxjs/toolkit";
import ThemeSlice from "./slices/ThemeSlice";
import authReducer from './slices/authSlice';

export const store = configureStore({
    reducer: {
        theme: ThemeSlice,
        auth: authReducer,
    },
    middleware: (getDefaultMiddleware) =>
        getDefaultMiddleware({
            serializableCheck: false,
        }),
});

export type RootState = ReturnType<typeof store.getState>;

// export {};
