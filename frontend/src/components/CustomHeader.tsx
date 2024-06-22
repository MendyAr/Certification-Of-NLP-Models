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
import React from 'react';
import GoogleLogin1 from '../pages/GoogleLogin1';
import GoogleLogin2 from '../pages/GoogleLogin2';
import GoogleLoginModal from "../pages/GoogleLogin1";

function getSwitchBackgroundColor(isLight: boolean) {
    return isLight ? "#dcb92b" : "#4469cb";
}

export default function CustomHeader() {
    const serverUrl = "http://127.0.0.1:3000"
    const { loggedIn, username } = useSelector((state: RootState) => state.user);
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
    
    
    const [user, setUser] = useState<string | null>(null);
    const login = useGoogleLogin({
    onSuccess: async (tokenResponse: TokenResponse) => {
        try {
        console.log(tokenResponse);
        const res = await axios.post(`${serverUrl}/login`, { id_token: tokenResponse.access_token });
        dispatch(setToken(tokenResponse.access_token));
        console.log(res.data.user_id);
        setUser(res.data.user_id);
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
        await axios.post(`${serverUrl}/logout`);
        setUser(null);
        dispatch(setToken(null));
        alert('Logout Successful');
    } catch (error) {
        console.error('Error logging out', error);
        alert('Logout Failed');
    }
    };

    const [isModalVisible, setIsModalVisible] = useState(false);

    const handleLoginClick = () => {
        setIsModalVisible(true);
    };

    const handleModalClose = () => {
        setIsModalVisible(false);
    };


    return (
        <Flex style={{ width: "100%" }} align="center" gap={8}>
            <Typography.Title
                style={{ color: "white", paddingBottom: 10, cursor: "pointer" }}
                onClick={() => navigate("/")}
            >
                Models Bias Detector
            </Typography.Title>
            <Menu
                theme="dark"
                mode="horizontal"
                items={items}
                style={{ flex: 1, minWidth: 0 }}
            />

            {user ? (
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
            ): (
            <br></br>)}


            {user ? (
                <Button icon={<GoogleOutlined />}
                    style={{ backgroundColor: "transparent", color: "white" }} onClick={handleLogout}>Logout
                </Button>
            ) : (
                <Button icon={<GoogleOutlined />}
                    style={{ backgroundColor: "transparent", color: "white" }} onClick={() => login()}>Login with Google
                </Button>
            )}

            {user ? (
                <Button icon={<GoogleOutlined />}
                    style={{ backgroundColor: "transparent", color: "white" }} onClick={handleLogout}>Logout2
                </Button>
            ) : (
                <Button icon={<GoogleOutlined />}
                    style={{ backgroundColor: "transparent", color: "white" }} onClick={handleLoginClick}>Login with Google2
                </Button>
            )}

            {/* <div style={{ padding: '20px' }}>
                <GoogleLogin1 loggedIn={loggedIn} username={username} />
                <GoogleLogin2 />
            </div> */}

            <Switch
                unCheckedChildren={<MoonFilled />}
                checkedChildren={<SunFilled />}
                defaultChecked={isLight}
                onChange={(checked) => dispatch(setTheme(checked))}
                style={{ backgroundColor: getSwitchBackgroundColor(isLight) }}
            />


            
            <GoogleLoginModal
                        isVisible={isModalVisible}
                        onClose={handleModalClose}
                        loggedIn={false}
                        username={null}
                        />

        </Flex>
    );
}


