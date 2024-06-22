import React from 'react';
import { Modal, Card, Button, Typography } from 'antd';
import { GoogleOutlined } from '@ant-design/icons';
import axios from 'axios';
import { sign } from 'crypto';

const { Text, Link } = Typography;

interface GoogleLoginModalProps {
    isVisible: boolean;
    onClose: () => void;
    loggedIn: boolean;
    username: string | null;
}

const serverUrl = "http://127.0.0.1:3000";
const signinUrl = `${serverUrl}/googlelogin`;

const GoogleLoginModal: React.FC<GoogleLoginModalProps> = ({ isVisible, onClose, loggedIn, username }) => {
    const handleRegisterClick = async () => {
        window.location.href =  `${serverUrl}/googlelogin`; 
    };

    return (
        <Modal
            title="Login"
            visible={isVisible}
            onCancel={onClose}
            footer={null}
        >
            <div style={{ display: 'flex', justifyContent: 'center' }}>
                <Card style={{ width: '100%', maxWidth: '400px' }}>
                    <div style={{ textAlign: 'center' }}>
                        {loggedIn ? (
                            <>
                                <Text>Welcome {username}</Text>
                                <br />
                                <Link href="/logout">Logout</Link>
                            </>
                        ) : (
                            <>
                                <Typography.Title level={4}>SignUp to Models Bias Derector</Typography.Title>
                                <Button
                                    type="default"
                                    icon={<GoogleOutlined />}
                                    onClick={handleRegisterClick}
                                    style={{ display: 'block', margin: 'auto' }}
                                >
                                    SignUp with Google
                                </Button>
                                <div style={{ display: 'flex', justifyContent: 'center', paddingTop: '1rem' }}>
                                    <Text type="secondary" style={{ textAlign: 'center' }}>
                                        <Link href={signinUrl}>Already have an account?</Link>
                                    </Text>
                                </div>
                            </>
                        )}
                    </div>
                </Card>
            </div>
        </Modal>
    );
};

export default GoogleLoginModal;
