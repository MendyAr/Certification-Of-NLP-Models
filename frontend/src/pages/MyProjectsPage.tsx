import React, { useState, useEffect } from 'react';
import { Button, Flex } from "antd";
import MainTitle from "./MainTitle";
import { useNavigate } from "react-router-dom";
import axios from 'axios';
import { RootState } from '../redux/store';
import { useSelector } from 'react-redux';

export default function MyProjects() {
    const token = useSelector((state: RootState) => state.auth.token);
    const serverUrl = "http://127.0.0.1:5001"
    const [projects, setProjects] = useState<string[]>([]);
    const [loading, setLoading] = useState(true);
    const navigate = useNavigate();

    useEffect(() => {
        const fetchProjects = async () => {
            try {
                const response = await axios.get(`${serverUrl}/get-projects`, {
                    params: {
                        email: "user1@example.com"  // Replace with dynamic email if needed
                    },
                    headers: {
                        Authorization: `Bearer ${token}`, // Add the token to the request headers
                    },
                });
                console.log("Projects response data:", response.data); // Debugging line
                setProjects(response.data.projects);
                setLoading(false);
            } catch (error) {
                console.error("Error fetching projects");
                setLoading(false);
            }
        };
        fetchProjects();
    }, []);

    if (loading) {
        return <div>Loading...</div>;
    }

    return (
        <Flex
            vertical
            justify="center"
            align="center"
            gap={50}
            style={{ height: "100%" }}
        >
            <MainTitle title1="My Projects" title2="" />
            <Flex vertical gap={30}>
                {projects.map((project, index) => (
                    <Button
                        key={index}
                        type="primary"
                        onClick={() => navigate(`/my-projects/${project}`)}
                    >
                        {project}
                    </Button>
                ))}
            </Flex>
        </Flex>
    );
}
