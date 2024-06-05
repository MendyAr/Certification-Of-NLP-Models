import React, { useState } from 'react';
import { useGoogleLogin, TokenResponse } from '@react-oauth/google';
import axios from 'axios';

const clientId = "876377932534-j7to6fa1ssrk9lcq8ji83b90pkna8l8i.apps.googleusercontent.com";

const GoogleSignIn: React.FC = () => {
  const [user, setUser] = useState<string | null>(null);
  const [token, setToken] = useState<string | null>(null);

  const login = useGoogleLogin({
    onSuccess: async (tokenResponse: TokenResponse) => {
      try {
        const res = await axios.post('http://localhost:5000/login', { id_token: tokenResponse.access_token });
        setToken(tokenResponse.access_token);
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
      await axios.post('http://localhost:5000/logout');
      setUser(null);
      alert('Logout Successful');
    } catch (error) {
      console.error('Error logging out', error);
      alert('Logout Failed');
    }
  };

  return (
    <div>
      {user ? (
        <button onClick={handleLogout}>Logout</button>
      ) : (
        <button onClick={() => login()}>Login with Google</button>
      )}
    </div>
  );
};

export default GoogleSignIn;
