import { Content, Header } from "antd/es/layout/layout";
import { Outlet, createBrowserRouter } from "react-router-dom";
import { Layout, Result, theme } from "antd";
import CustomHeader from "../components/CustomHeader";
import PathBreadcrumbs from "../components/PathBreadcrumbs/PathBreadcrumbs";
import HomePage from "../pages/HomePage";
import EvalRequests from "../pages/EvalRequestsPage";

export default function Root() {
    const {
        token: { colorBgContainer, borderRadiusLG },
    } = theme.useToken();

    return (
        <Layout style={{ height: "100vh" }}>
            <Header style={{ display: "flex", alignItems: "center" }}>
                <CustomHeader />
            </Header>
            <Layout>
                <Layout style={{ padding: "0px 12px 12px 12px" }}>
                    <PathBreadcrumbs />
                    <Content
                        style={{
                            overflowY: "auto",
                            padding: 24,
                            margin: 0,
                            minHeight: 280,
                            background: colorBgContainer,
                            borderRadius: borderRadiusLG,
                        }}
                    >
                        <Outlet />
                    </Content>
                </Layout>
            </Layout>
        </Layout>
    );
}

export const router = createBrowserRouter([
  {
    path: "/",
    element: <Root />,
    errorElement: <Result status="404" title="404" subTitle="Sorry, the page you visited does not exist." />,
    children: [
      {
        path: "",
        element: <HomePage />,
      },
      {
        path: "my-account",
        element: <div>My Account</div>,
      },
      {
        path: "login",
        element: <div>Login</div>,
      },
      {
        path: "new-project",
        element: <div>new project</div>,
      },
      {
        path: "my-projects",
        element: <div>my rojects</div>,
      },
      {
        path: "EvalRequests",
        element: <EvalRequests />,
      },
    ],
  },
]);
