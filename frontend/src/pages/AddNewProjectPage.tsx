import React, { useState, ChangeEvent } from "react";
import { Button, Input, Form, message } from "antd";
import { useNavigate } from "react-router-dom";
import axios, { AxiosError } from "axios";
import { RootState } from "../redux/store";
import { useSelector } from "react-redux";

interface ErrorResponse {
    error: string;
}

const AddNewProject = () => {
    const token = useSelector((state: RootState) => state.auth.token);
    // const serverUrl = "http://132.73.84.52:5001"
    const serverUrl = "http://127.0.0.1:5001";
    const navigate = useNavigate();
    const [projectName, setProjectName] = useState("");
    const handleProjectNameChange = (e: ChangeEvent<HTMLInputElement>) => {
        setProjectName(e.target.value);
    };

    const addProject = async () => {
        try {
            const response = await axios.post(`${serverUrl}/add-new-project`, { name: projectName }, 
            {
                headers: {
                    Authorization: `${token}` // Add the token to the request headers
                },
            });   
            console.log("Add project response:", response.data); // Debugging line
            navigate(`/my-projects/${projectName}/new-eval-request`);
        } catch (error) {
            console.error("Error adding project", error);
            const axiosError = error as AxiosError<ErrorResponse>;
            const errorMessage = axiosError.response?.data?.error || 'Error adding project';
            message.error(`Error: ${errorMessage}`);
        }
    };

    return (
            <Form layout="vertical" style={{ marginTop: "20px", width: "100%" }}>
                <Form.Item label="Project Name">
                    <Input onChange={handleProjectNameChange} placeholder="Enter project name" />
                </Form.Item>
                <Form.Item>
                    <Button type="primary" htmlType="submit" onClick={addProject}>
                        Create Project
                    </Button>
                </Form.Item>
            </Form>
    );
};

export default AddNewProject;
