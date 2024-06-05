import {
    Button,
    Dropdown,
    Flex,
    Menu,
    MenuProps,
    Switch,
    Typography,
} from "antd";
import { useDispatch, useSelector } from "react-redux";
import {
    GoogleOutlined,
    MoonFilled,
    SunFilled,
    UserOutlined,
} from "@ant-design/icons";
import { RootState } from "../redux/store";
import { setTheme } from "../redux/slices/ThemeSlice";
import { MenuItem } from "../utils/Types";
import { getMenuItem } from "../utils/Utils";
import { useNavigate } from "react-router-dom";
import { useState } from "react";
import { TokenResponse, useGoogleLogin } from "@react-oauth/google";
import axios from "axios";
import { selectToken, setToken } from "../redux/slices/authSlice";

function getSwitchBackgroundColor(isLight: boolean) {
    return isLight ? "#dcb92b" : "#4469cb";
}

export default function CustomHeader() {
    const { isLight } = useSelector((state: RootState) => state.theme);
    const dispatch = useDispatch();
    const navigate = useNavigate();
    const token = useSelector(selectToken);

    const items: MenuItem[] = [
        // getMenuItem({ key: "myAccount", label: "My Account", icon: <UserOutlined /> })
    ];

    const itemsMyAccount: MenuProps["items"] = [
        {
            key: "1",
            label: "Add New Project",
            onClick: () => navigate("/new-project"),
        },
        {
            key: "2",
            label: "My Projects",
            onClick: () => navigate("/my-projects"),
        },
    ];
    
    const clientId = "876377932534-j7to6fa1ssrk9lcq8ji83b90pkna8l8i.apps.googleusercontent.com";
      const [user, setUser] = useState<string | null>(null);
      const login = useGoogleLogin({
        onSuccess: async (tokenResponse: TokenResponse) => {
          try {
            const res = await axios.post('http://localhost:5000/login', { id_token: tokenResponse.access_token });
            dispatch(setToken(tokenResponse.access_token));
            console.log(tokenResponse.access_token);
            setUser(res.data.user_id);
            console.log(tokenResponse.access_token);
            alert('Login Successful');

          } catch (error) {
            console.error('Error logging in', error);
            alert('Login Failed');
          }
        },
        onError: (error) => {
          console.error('Login failed', error);
          alert('Login Failed');
        },
      });
    
      const handleLogout = async () => {
        try {
          await axios.post('http://localhost:5000/logout');
          setUser(null);
          dispatch(setToken(null));
          alert('Logout Successful');
        } catch (error) {
          console.error('Error logging out', error);
          alert('Logout Failed');
        }
      };


    return (
        <Flex style={{ width: "100%" }} align="center" gap={8}>
            <Typography.Title
                style={{ color: "white", paddingBottom: 10, cursor: "pointer" }}
                onClick={() => navigate("/")}
            >
                Modals Bias Detector
            </Typography.Title>
            <Menu
                theme="dark"
                mode="horizontal"
                items={items}
                style={{ flex: 1, minWidth: 0 }}
            />
            {/* <Button
        onClick={() => navigate("my-account")}
        icon={<UserOutlined />}
        style={{ backgroundColor: "transparent", color: "white" }}
      >
        My Account
      </Button> */}

            <Dropdown
                menu={{ items: itemsMyAccount }}
                placement="bottomLeft"
                arrow
            >
                <Button
                    style={{ backgroundColor: "transparent", color: "white" }}
                    icon={<UserOutlined />}
                >
                    My Account
                </Button>
            </Dropdown>


            {user ? (
                <Button icon={<GoogleOutlined />}
                    style={{ backgroundColor: "transparent", color: "white" }} onClick={handleLogout}>Logout</Button>
            ) : (
                <Button icon={<GoogleOutlined />}
                    style={{ backgroundColor: "transparent", color: "white" }} onClick={() => login()}>Login with Google</Button>
            )}

            {/* <Button
                onClick={() => navigate("login")}
                icon={<GoogleOutlined />}
                style={{ backgroundColor: "transparent", color: "white" }}
            >
                Login
            </Button> */}
            <Switch
                unCheckedChildren={<MoonFilled />}
                checkedChildren={<SunFilled />}
                defaultChecked={isLight}
                onChange={(checked) => dispatch(setTheme(checked))}
                style={{ backgroundColor: getSwitchBackgroundColor(isLight) }}
            />
        </Flex>
    );
}
