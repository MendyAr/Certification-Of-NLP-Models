import React, { useState, useEffect } from 'react';
import { Button, Col, Modal, Row, Space, message } from "antd";
import MainTitle from "./MainTitle";
import { useNavigate } from "react-router-dom";
import axios, { AxiosError } from 'axios';
import { RootState } from '../redux/store';
import { useSelector } from 'react-redux';
import { MinusCircleOutlined } from '@ant-design/icons';

interface ErrorResponse {
    error: string;
}

export default function MyProjects() {
    const token = useSelector((state: RootState) => state.auth.token);
    // const serverUrl = "http://132.73.84.52:5001";
    const serverUrl = "http://127.0.0.1:5001";
    const [projects, setProjects] = useState<string[]>([]);
    const [loading, setLoading] = useState(true);
    const navigate = useNavigate();

    useEffect(() => {
        const fetchProjects = async () => {
            try {
                const response = await axios.get(`${serverUrl}/get-projects`, {
                    headers: {
                        Authorization: `${token}` // Add the token to the request headers
                    },
                });
                console.log("Projects response data:", response.data); // Debugging line
                setProjects(response.data.projects);
                setLoading(false);
            } catch (error) {
                console.error("Error fetching projects", error);
                const axiosError = error as AxiosError<ErrorResponse>;
                const errorMessage = axiosError.response?.data?.error || 'Error fetching projects';
                message.error(`Error: ${errorMessage}`);
                setLoading(false);
            }
        };
        fetchProjects();
    }, [token, serverUrl]);

    // State variables to manage the confirmation modals
    const [confirmDeleteProject, setConfirmDeleteProject] = useState(false);
    const [projectToDelete, setProjectToDelete] = useState("");

    // Function to set the project to delete and show the confirmation modal
    const handleProjectDelete = (projectNameToDelete: string) => {
        setProjectToDelete(projectNameToDelete);
        setConfirmDeleteProject(true);
    };

    // Function to delete project
    const deleteProjectAction = async () => {
        await deleteProject(projectToDelete);
        setConfirmDeleteProject(false); // Close the modal
    };

    // Function to delete a project by its name
    const deleteProject = async (projectNameToDelete: string) => {
        try {
            const response = await axios.delete(`${serverUrl}/delete-project`, {
                params: {
                    project: projectNameToDelete,
                },
                headers: {
                    Authorization: `${token}` // Add the token to the request headers
                },
            });
            console.log("Delete project response:", response.data); // Debugging line
            // Update the project state after successful deletion
            setProjects(projects.filter(project => project !== projectNameToDelete));
        } catch (error) {
            console.error("Error deleting project", error);
            const axiosError = error as AxiosError<ErrorResponse>;
            const errorMessage = axiosError.response?.data?.error || 'Error deleting project';
            message.error(`Error: ${errorMessage}`);
        }
    };

    if (loading) {
        return <div>Loading...</div>;
    }

    return (
        <Space
            direction="vertical"
            size="large"
            style={{ width: '100%', height: '100%', alignItems: 'center' }}
        >
            <MainTitle title1="My Projects" title2="" />

            <Space direction="vertical" size="middle" style={{ width: '100%' }}>
                {projects.map((project, index) => (
                    <Row key={index} gutter={16} style={{ width: '100%' }}>
                        <Col span={4}>
                            <Button
                                type="primary"
                                danger
                                icon={<MinusCircleOutlined />}
                                // block
                                style={{marginRight: "90px"}}
                                onClick={() => handleProjectDelete(project)}
                            />
                        </Col>
                        <Col span={20}>
                            <Button
                                type="primary"
                                block
                                onClick={() => navigate(`/my-projects/${project}`)}
                            >
                                {project}
                            </Button>
                        </Col>
                    </Row>
                ))}
            </Space>



            {/* delete project pop-up: */}
            <Modal
                title="Confirm Delete Project"
                visible={confirmDeleteProject}
                onCancel={() => setConfirmDeleteProject(false)} // Close the modal without deleting
                footer={[
                    <Button key="cancel" onClick={() => setConfirmDeleteProject(false)}>
                        Cancel
                    </Button>,
                    <Button key="delete" type="primary" onClick={deleteProjectAction}>
                        Delete
                    </Button>,
                ]}
            >
                <p>Are you sure you want to delete this project?</p>
            </Modal>
        </Space>
    );
}
