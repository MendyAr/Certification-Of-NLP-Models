import React from 'react';
import { Button, Card, Typography } from 'antd';
import { GoogleOutlined } from '@ant-design/icons';
import 'antd/dist/reset.css';

const { Title, Text, Link } = Typography;

const GoogleLogin2: React.FC = () => {
    const handleRegisterClick = () => {
        window.location.href = "/googlelogin_callback";
    };

    return (
        <div style={{ marginTop: '50rem', display: 'flex', justifyContent: 'center' }}>
        <Card style={{ width: '100%', maxWidth: '400px' }}>
            <div style={{ textAlign: 'center' }}>
            <Title level={4} style={{ fontSize: '20px' }}>
                Welcome back, Log In to FlaskLogin
            </Title>
            <Button
                type="default"
                icon={<GoogleOutlined style={{ background: 'conic-gradient(from -45deg, #ea4335 110deg, #4285f4 90deg 180deg, #34a853 180deg 270deg, #fbbc05 270deg) 73% 55%/150% 150% no-repeat', WebkitBackgroundClip: 'text', color: 'transparent', WebkitTextFillColor: 'transparent' }} />}
                onClick={handleRegisterClick}
                style={{ padding: '1rem', display: 'block', margin: 'auto' }}
            >
                Continue with Google
            </Button>
            <div style={{ display: 'flex', justifyContent: 'center', paddingTop: '1rem' }}>
                <Text type="secondary" style={{ textAlign: 'center' }}>
                <Link href="/">Don't have an account?</Link>
                </Text>
            </div>
            </div>
        </Card>
        </div>
    );
};

export default GoogleLogin2;
