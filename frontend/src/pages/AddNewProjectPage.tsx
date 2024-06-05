import React, { useState, ChangeEvent } from "react";
import { Button, Input, Form } from "antd";
import { useNavigate } from "react-router-dom";
import axios from "axios";

const AddNewProject = () => {
    const serverUrl = "http://127.0.0.1:5001"
    const navigate = useNavigate();
    const [projectName, setProjectName] = useState("");
    const handleProjectNameChange = (e: ChangeEvent<HTMLInputElement>) => {
        setProjectName(e.target.value);
    };

    const addProject = async () => {
        try {
            const response = await axios.post(`${serverUrl}/add-new-project`, { name: projectName }, 
            {params: {
                        email: "user1@example.com",
                    }
            });   
            console.log("Add project response:", response.data); // Debugging line
            navigate(`/my-projects/${projectName}/new-eval-request`);
        } catch (error) {
            console.error("Error adding questionnaire");
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
