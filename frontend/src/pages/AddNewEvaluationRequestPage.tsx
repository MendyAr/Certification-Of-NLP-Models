import React, { useState, ChangeEvent, useEffect } from "react";
import { Checkbox, Col, Row, Button, Input, Form, Modal, Select, Flex } from "antd";
import MainTitle from "./MainTitle";
import { CheckboxValueType } from "antd/es/checkbox/Group";
import axios from "axios";
import { useNavigate, useParams } from "react-router-dom";
import { MinusCircleOutlined } from "@ant-design/icons";
import { RootState } from "../redux/store";
import { useSelector } from "react-redux";

const { Option } = Select;

const onChange = (checkedValues: CheckboxValueType[]) => {
    console.log("checked = ", checkedValues);
};

const AddNewEvaluationRequest = () => {
    const token = useSelector((state: RootState) => state.auth.token);
    const serverUrl = "http://127.0.0.1:5001"
    const { projectName } = useParams();
    const navigate = useNavigate();
    const [isModelModalVisible, setIsModelModalVisible] = useState(false);
    const [isQuestionnaireModalVisible, setIsQuestionnaireModalVisible] = useState(false);
    const [modelName, setModelName] = useState("");
    const [modelUrl, setModelUrl] = useState("");
    const [selectedQuestionnaire, setSelectedQuestionnaire] = useState("");

    // State variables to manage the confirmation modals
const [confirmDeleteModel, setConfirmDeleteModel] = useState(false);
const [confirmDeleteQuestionnaire, setConfirmDeleteQuestionnaire] = useState(false);
const [modelToDelete, setModelToDelete] = useState("");
const [questionnaireToDelete, setQuestionnaireToDelete] = useState("");

// Function to set the model to delete and show the confirmation modal
const handleModelDelete = (modelNameToDelete: string) => {
    setModelToDelete(modelNameToDelete);
    setConfirmDeleteModel(true);
};

// Function to set the questionnaire to delete and show the confirmation modal
const handleQuestionnaireDelete = (questionnaireToDelete: string) => {
    setQuestionnaireToDelete(questionnaireToDelete);
    setConfirmDeleteQuestionnaire(true);
};

// Function to delete model
const deleteModelAction = async () => {
    await deleteModel(modelToDelete);
    setConfirmDeleteModel(false); // Close the modal
};

// Function to delete questionnaire
const deleteQuestionnaireAction = async () => {
    await deleteQuestionnaire(questionnaireToDelete);
    setConfirmDeleteQuestionnaire(false); // Close the modal
};
    
    const showModelModal = () => {
        setIsModelModalVisible(true);
    };
    const showQuestionnaireModal = () => {
        getAllQuestionnaires();
        setIsQuestionnaireModalVisible(true);
    };
    const handleModelOk = () => {
        console.log("Model URL:", modelUrl);
        addModel();
        setIsModelModalVisible(false);
        setModelUrl("");
        setModelName("");
    };
    const handleQuestionnaireOk = () => {
        console.log("Selected Questionnaire:", selectedQuestionnaire);
        addQues();
        setIsQuestionnaireModalVisible(false);
        setSelectedQuestionnaire("");
    };
    const handleModelCancel = () => {
        setIsModelModalVisible(false);
        setModelUrl("");
        setModelName("");
    };
    const handleQuestionnaireCancel = () => {
        setIsQuestionnaireModalVisible(false);
        setSelectedQuestionnaire("");
    };
    const handleModelUrlChange = (e: ChangeEvent<HTMLInputElement>) => {
        setModelUrl(e.target.value);
    };
    const handleModelNameChange = (e: ChangeEvent<HTMLInputElement>) => {
        setModelName(e.target.value);
    };
    const handleQuestionnaireChange = (value: string) => {
        setSelectedQuestionnaire(value);
    };
    const [models, setModels] = useState<Model[]>([]);
    const [ques, setQues] = useState<string[]>([]);
    const [allQues, setAllQues] = useState<string[]>([]);

    type Model = {
        name: string;
        url: string;
    };

    useEffect(() => {
        const fetchData = async () => {
            try {
                const response = await axios.get(`${serverUrl}/project-info`,
                    {
                        params: {
                            project: projectName,
                            email: "user1@example.com",
                        },
                        headers: {
                            Authorization: `Bearer ${token}`, 
                        },
                    }
                );
                console.log("Response data:", response.data); // Debugging line
                setModels(response.data.models);
                setQues(response.data.ques)
            } catch (error) {
                console.error("Error fetching data:", error);
            }
        };
        fetchData();
    }, [isModelModalVisible, isQuestionnaireModalVisible, confirmDeleteQuestionnaire, confirmDeleteModel]);

    const getAllQuestionnaires = () => {
        const fetchData = async () => {
            try {
                const response = await axios.get(`${serverUrl}/get-all-ques`, {
                    headers: {
                        Authorization: `Bearer ${token}`, // Add the token to the request headers
                    },
                });
                console.log("Response data:", response.data); // Debugging line
                setAllQues(response.data);
            } catch (error) {
                console.error("Error fetching data:", error);
            }
        };
        fetchData();
    };

    const addQues = async () => {
        try {
            const response = await axios.post(`${serverUrl}/add-ques`, { ques: selectedQuestionnaire }, 
            {
                params: {
                    project: projectName,
                    email: "user1@example.com",
                },
                headers: {
                    Authorization: `Bearer ${token}`, // Add the token to the request headers
                },
            }
        );   
            console.log("Add questionnaire response:", response.data); // Debugging line
        } catch (error) {
            console.error("Error adding questionnaire");
        }
    };

    const addModel = async () => {
        try {
            const response = await axios.post(`${serverUrl}/add-model`, { name: modelName, url: modelUrl }, 
            {params: {
                        project: projectName,
                        email: "user1@example.com",
                    },
                    headers: {
                        Authorization: `Bearer ${token}`, // Add the token to the request headers
                    },
                });
            console.log("Add model response:", response.data); // Debugging line
        } catch (error) {
            console.error("Error adding model");
        }
    };

    // Function to delete a model by its name
const deleteModel = async (modelNameToDelete: string) => {
    try {
        const response = await axios.delete(`${serverUrl}/delete-model`, {
            params: {
                project: projectName,
                email: "user1@example.com",
                modelName: modelNameToDelete,
            },
            headers: {
                Authorization: `Bearer ${token}`, // Add the token to the request headers
            },
        });
        console.log("Delete model response:", response.data); // Debugging line
        // Update the models state after successful deletion
        setModels(models.filter(model => model.name !== modelNameToDelete));
    } catch (error) {
        console.error("Error deleting model");
    }
};

// Function to delete a questionnaire by its name
const deleteQuestionnaire = async (questionnaireToDelete: string) => {
    try {
        const response = await axios.delete(`${serverUrl}/delete-ques`, {
            params: {
                project: projectName,
                email: "user1@example.com",
                questionnaire: questionnaireToDelete,
            },
            headers: {
                Authorization: `Bearer ${token}`, // Add the token to the request headers
            },
        });
        console.log("Delete questionnaire response:", response.data); // Debugging line
        // Update the ques state after successful deletion
        setQues(ques.filter(q => q !== questionnaireToDelete));
    } catch (error) {
        console.error("Error deleting questionnaire");
    }
};

    return (
        <div style={{ padding: "20px" }}>
            <div style={{display: "flex", justifyContent: "space-between", marginBottom: "20px"}}>
                <div style={{ width: "45%" }}>
                    <Flex align="left">
                        <MainTitle title1="Select Model" title2="" />
                    </Flex>
                    <ul style={{ listStyleType: "none", padding: 0 }}>
                        {models && models.map((model, index) => (
                            <li key={index} style={{ display: "flex", alignItems: "center", marginBottom: "5px" }}>
                                <Button type="link" icon={<MinusCircleOutlined />} onClick={() => handleModelDelete(model.name)} />
                                <span>{model.name}</span>
                            </li>
                        ))}
                    </ul>
                    <Button type="dashed" style={{ marginTop: "10px" }} onClick={showModelModal}>
                        Click to add more models
                    </Button>
                </div>
                <div style={{ width: "45%" }}> 
                    <Flex align="left">
                        <MainTitle title1="Select Questionnaire" title2="" />
                    </Flex>
                    <ul style={{ listStyleType: "none", padding: 0 }}>
                        {ques && ques.map((q, index) => (
                            <li key={index} style={{ display: "flex", alignItems: "center", marginBottom: "5px" }}>
                                <Button type="link" icon={<MinusCircleOutlined />} onClick={() => handleQuestionnaireDelete(q)} />
                                <span>{q}</span>
                            </li>
                        ))}
                    </ul>
                    <Button type="dashed" style={{ marginTop: "10px" }} onClick={showQuestionnaireModal}>
                        Click to add more Questionnaire
                    </Button>
                </div>
            </div>
            <Form layout="vertical" style={{ marginTop: "20px", width: "100%" }}>
                <Form.Item>
                    <Button type="primary" htmlType="submit"  onClick={() => navigate(`/my-projects/${projectName}/eval-requests`)} >
                        Create Evaluation Requests
                    </Button>
                </Form.Item>
            </Form>


            {/* Add Model pop-up: */}
            <Modal title="Add Model" open={isModelModalVisible} onOk={handleModelOk} onCancel={handleModelCancel} okText="Add to Project">
                <Form layout="vertical">
                    <Form.Item label="Model Name">
                        <Input placeholder="Enter model name" value={modelName} onChange={handleModelNameChange}/>
                    </Form.Item>
                    <Form.Item label="Model URL">
                        <Input placeholder="Enter model URL" value={modelUrl} onChange={handleModelUrlChange}/>
                    </Form.Item>
                </Form>
            </Modal>

             {/* Add Questionnaire pop-up: */}
            <Modal title="Add Questionnaire" open={isQuestionnaireModalVisible} onOk={handleQuestionnaireOk} onCancel={handleQuestionnaireCancel} okText="Add to Project">
                <Form layout="vertical">
                    <Form.Item label="Select Questionnaire">
                        <Select placeholder="Select a questionnaire" onChange={handleQuestionnaireChange} value={selectedQuestionnaire}>
                            {allQues.map((q, index) => (
                                <Option value={q} key={index}>
                                {q}
                                </Option>
                            ))}
                        </Select>
                    </Form.Item>
                </Form>
            </Modal>

            
             {/* delete model pop-up: */}
            <Modal
                title="Confirm Delete Model"
                visible={confirmDeleteModel}
                onCancel={() => setConfirmDeleteModel(false)} // Close the modal without deleting
                footer={[
                    <Button key="cancel" onClick={() => setConfirmDeleteModel(false)}>
                        Cancel
                    </Button>,
                    <Button key="delete" type="primary" onClick={deleteModelAction}>
                        Delete
                    </Button>,
                ]}
            >
                <p>Are you sure you want to delete this model?</p>
            </Modal>
            
            {/* delete Questionnaire pop-up: */}
            <Modal
                title="Confirm Delete Questionnaire"
                visible={confirmDeleteQuestionnaire}
                onCancel={() => setConfirmDeleteQuestionnaire(false)} // Close the modal without deleting
                footer={[
                    <Button key="cancel" onClick={() => setConfirmDeleteQuestionnaire(false)}>
                        Cancel
                    </Button>,
                    <Button key="delete" type="primary" onClick={deleteQuestionnaireAction}>
                        Delete
                    </Button>,
                ]}
            >
                <p>Are you sure you want to delete this questionnaire?</p>
            </Modal>


        </div>
    );
};

export default AddNewEvaluationRequest;