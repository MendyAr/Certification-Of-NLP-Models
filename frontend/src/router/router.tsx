import { Content, Header } from "antd/es/layout/layout";
import { Outlet, createBrowserRouter } from "react-router-dom";
import { Layout, Result, theme } from "antd";
import CustomHeader from "../components/CustomHeader";

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
                <Layout style={{ padding: "0px 24px 24px 24px" }}>
                    {/* <PathBreadcrumbs /> */}
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
        errorElement: (
            <Result
                status="404"
                title="404"
                subTitle="Sorry, the page you visited does not exist."
            />
        ),
        // children: [
        //     {
        //         path: "",
        //         element: <LandingPage />,
        //     },
        // ],
    },
]);
