import { Button, Dropdown, Flex, Form, Input, Menu, MenuProps, Switch, Typography} from "antd";
import { useDispatch, useSelector } from "react-redux";
import { GoogleOutlined, LoginOutlined, LogoutOutlined, MoonFilled, SolutionOutlined, SunFilled, UserOutlined } from "@ant-design/icons";
import React from 'react';
import { RootState } from "../redux/store";
import { setTheme } from "../redux/slices/ThemeSlice";
import { MenuItem } from "../utils/Types";
// import { getMenuItem } from "../utils/Utils";
import { useNavigate } from "react-router-dom";
import { useState } from "react";
// import { TokenResponse, useGoogleLogin } from "@react-oauth/google";
import axios from "axios";
import { selectToken, setToken } from "../redux/slices/authSlice";
import Modal from "antd/es/modal/Modal";

function getSwitchBackgroundColor(isLight: boolean) {
    return isLight ? "#dcb92b" : "#4469cb";
}

export default function CustomHeader() {
    const serverUrl = "http://132.73.84.52:5001"
    const dispatch = useDispatch();
    const navigate = useNavigate();
    const token = useSelector(selectToken);
    const { isLight } = useSelector((state: RootState) => state.theme);

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

    // const login = useGoogleLogin({
    // onSuccess: async (tokenResponse: TokenResponse) => {
    //     try {
    //     console.log(tokenResponse);
    //     const res = await axios.post(${serverUrl}/login, { id_token: tokenResponse.access_token });
    //     dispatch(setToken(tokenResponse.access_token));
    //     console.log(res.data.user_id);
    //     setUser(res.data.user_id);
    //     alert('Login Successful');

    //     } catch (error) {
    //     console.error('Error logging in', error);
    //     alert('Login Failed');
    //     }
    // },
    // onError: (error) => {
    //     console.error('Login failed', error);
    //     alert('Login Failed');
    // },
    // });

    // const handleLogout = async () => {
    // try {
    //     await axios.post(${serverUrl}/logout);
    //     setUser(null);
    //     dispatch(setToken(null));
    //     alert('Logout Successful');
    // } catch (error) {
    //     console.error('Error logging out', error);
    //     alert('Logout Failed');
    // }
    // };

    const [isLoginVisible, setIsLoginVisible] = useState(false);
    const [isRegisterVisible, setIsRegisterVisible] = useState(false);
    // const [user, setUser] = useState<string | null>(null);

    const handleOpenLoginModal = () => {
        setIsLoginVisible(true);
    };

    const handleOpenRegisterModal = () => {
        setIsRegisterVisible(true);
    };

    const handleCancel = (type: 'login' | 'register') => {
        if (type === 'login') {
            setIsLoginVisible(false);
        } else {
            setIsRegisterVisible(false);
        }
    };

    const handleLogin = async (values: any) => {
        try {
            const response = await axios.post(`${serverUrl}/login`, values);
            dispatch(setToken(response.data.token));
            // setUser(response.data.user_id);
            setIsLoginVisible(false);
            alert('Login Successful');
        } catch (error) {
            console.error('Error logging in', error);
            alert('Login Failed');
        }
    };

    const handleRegister = async (values: any) => {
        try {
            await axios.post(`${serverUrl}/register`, values);
            setIsRegisterVisible(false);
            alert('Registration Successful');
        } catch (error) {
            console.error('Error registering', error);
            alert('Registration Failed');
        }
    };

    const handleLogout = async () => {
        try {
            // Optional: Send a request to the backend to invalidate the token/session
            await axios.post(`${serverUrl}/logout`, {}, {
                headers: {
                    Authorization: `${token}`
                }
            });
            dispatch(setToken(null));
            // setUser(null);
            alert('Logout Successful');
        } catch (error) {
            console.error('Error logging out', error);
            alert('Logout Failed');
        }
    };

    return (
        <Flex style={{ width: "100%" }} align="center" gap={8}>
            <Typography.Title style={{ color: "white", paddingBottom: 10, cursor: "pointer" }} onClick={() => navigate("/")}>
                Models Bias Detector
            </Typography.Title>
            <Menu theme="dark" mode="horizontal" items={items} style={{ flex: 1, minWidth: 0 }}/>

            {/* <Dropdown menu={{ items: itemsMyAccount }} placement="bottomLeft" arrow>
                <Button style={{ backgroundColor: "transparent", color: "white" }} icon={<UserOutlined />}>
                    My Account
                </Button>
            </Dropdown> */}

            {token ? (
                <>
                    <Dropdown menu={{ items: itemsMyAccount }} placement="bottomLeft" arrow>
                            <Button style={{ backgroundColor: "transparent", color: "white" }} icon={<UserOutlined />}>
                                My Account
                            </Button>
                        </Dropdown>
                    <Button icon={<LogoutOutlined />} style={{ backgroundColor: "transparent", color: "white" }} onClick={handleLogout}>Logout</Button>
                </>
            ) : (
                <>
                    <Button icon={<SolutionOutlined />} style={{ backgroundColor: "transparent", color: "white" }} onClick={handleOpenRegisterModal}>Register</Button>
                    <Button icon={<LoginOutlined />} style={{ backgroundColor: "transparent", color: "white" }} onClick={handleOpenLoginModal}>Log-in</Button>
                </>
            )}

            <Switch
                unCheckedChildren={<MoonFilled />}
                checkedChildren={<SunFilled />}
                defaultChecked={isLight}
                onChange={(checked) => dispatch(setTheme(checked))}
                style={{ backgroundColor: getSwitchBackgroundColor(isLight) }}
            />

         {/* login modal    */}
        <Modal title="Log In" visible={isLoginVisible} onCancel={() => handleCancel('login')} footer={null}>
        <Form onFinish={handleLogin}>
            <Form.Item name="email" rules={[{ required: true, message: 'Please input your email!' }]}>
                <Input placeholder="Email" />
            </Form.Item>
            <Form.Item name="password" rules={[{ required: true, message: 'Please input your password!' }]}>
                <Input.Password placeholder="Password" />
            </Form.Item>
            <Button type="primary" htmlType="submit">Log In</Button>
        </Form>
        </Modal>
        
        {/* register modal   */}
        <Modal title="Register" visible={isRegisterVisible} onCancel={() => handleCancel('register')} footer={null}>
        <Form onFinish={handleRegister}>
            <Form.Item name="email" rules={[{ required: true, message: 'Please input your email!' }]}>
                <Input placeholder="Email" />
            </Form.Item>
            <Form.Item name="password" rules={[{ required: true, message: 'Please input your password!' }]}>
                <Input.Password placeholder="Password" />
            </Form.Item>
            <Button type="primary" htmlType="submit">Register</Button>
        </Form>
        </Modal>

        </Flex>
    );
}