import { configureStore } from "@reduxjs/toolkit";
import ThemeSlice from "./slices/ThemeSlice";

export const store = configureStore({
    reducer: {
        theme: ThemeSlice,
    },
    middleware: (getDefaultMiddleware) =>
        getDefaultMiddleware({
            serializableCheck: false,
        }),
});

export type RootState = ReturnType<typeof store.getState>;

// export {};
