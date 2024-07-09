import "./App.css";
import React from 'react';
import { RouterProvider } from "react-router-dom";
import { router } from "./router/router";
import { useSelector } from "react-redux";
import { RootState } from "./redux/store";
import { ConfigProvider as AntdTheme, theme } from "antd";
require('react-dotenv').config();

function App() {
  const { isLight } = useSelector((state: RootState) => state.theme);
  return (
    <AntdTheme
      theme={{
        algorithm: isLight ? undefined : theme.darkAlgorithm,
      }}
    >
      <RouterProvider router={router} />
    </AntdTheme>
  );
}

export default App;
