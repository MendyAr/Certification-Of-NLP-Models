import React, { useState, ChangeEvent, useEffect } from "react";
import { Checkbox, Col, Row, Button, Input, Form, Modal, Select, Flex } from "antd";
import MainTitle from "./MainTitle";
import { CheckboxValueType } from "antd/es/checkbox/Group";
import axios from "axios";
import { useParams } from "react-router-dom";

const { Option } = Select;

const onChange = (checkedValues: CheckboxValueType[]) => {
    console.log("checked = ", checkedValues);
};

const AddNewEvaluationRequest = () => {
    const { projectName } = useParams();
    const [isModelModalVisible, setIsModelModalVisible] = useState(false);
    const [isQuestionnaireModalVisible, setIsQuestionnaireModalVisible] = useState(false);
    const [modelName, setModelName] = useState("");
    const [modelUrl, setModelUrl] = useState("");
    const [selectedQuestionnaire, setSelectedQuestionnaire] = useState("");
    
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
                const response = await axios.get("http://127.0.0.1:5001/project-info",
                    {
                        params: {
                            project: projectName,
                            email: "user1@example.com",
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
    }, [isModelModalVisible, isQuestionnaireModalVisible]);

    const getAllQuestionnaires = () => {
        const fetchData = async () => {
            try {
                const response = await axios.get("http://127.0.0.1:5001/get-all-ques", {});
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
            const response = await axios.post("http://127.0.0.1:5001/add-ques", { ques: selectedQuestionnaire }, 
            {params: {
                        project: projectName,
                        email: "user1@example.com",
                    }
            });   
            console.log("Add questionnaire response:", response.data); // Debugging line
        } catch (error) {
            console.error("Error adding questionnaire");
        }
    };

    const addModel = async () => {
        try {
            const response = await axios.post("http://127.0.0.1:5001/add-model", { name: modelName, url: modelUrl }, 
            {params: {
                        project: projectName,
                        email: "user1@example.com",
                    }
            });
            console.log("Add model response:", response.data); // Debugging line
        } catch (error) {
            console.error("Error adding model");
        }
    };

    return (
        <div style={{ padding: "20px" }}>
            <div style={{display: "flex", justifyContent: "space-between", marginBottom: "20px"}}>
                <div style={{ width: "45%" }}>
                    <Flex align="left">
                        <MainTitle title1="Select Model" title2="" />
                    </Flex>
                    <Checkbox.Group style={{ width: "100%" }} onChange={onChange}>
                    <Row>
                        {models && models.map((model, index) => (
                            <Col span={12} key={index}>
                                <Checkbox value={model.name}>{model.name}</Checkbox>
                            </Col>
                        ))}
                    </Row>
                    </Checkbox.Group>
                    <Button type="dashed" style={{ marginTop: "10px" }} onClick={showModelModal}>
                        Click to add more models
                    </Button>
                </div>
                <div style={{ width: "45%" }}> 
                    <Flex align="left">
                        <MainTitle title1="Select Questionnaire" title2="" />
                    </Flex>
                    <Checkbox.Group style={{ width: "100%" }} onChange={onChange}>
                        <Row>
                            {ques && ques.map((q,index) => (
                                <Col span={12} key={index}>
                                    <Checkbox value={q}>{q}</Checkbox>
                                </Col>
                            ))}
                        </Row>
                    </Checkbox.Group>
                    <Button type="dashed" style={{ marginTop: "10px" }} onClick={showQuestionnaireModal}>
                        Click to add more Questionnaire
                    </Button>
                </div>
            </div>
            <Form layout="vertical" style={{ marginTop: "20px", width: "100%" }}>
                {/* <Form.Item label="Project Name">
                    <Input placeholder="Enter project name" />
                </Form.Item> */}
                <Form.Item>
                    <Button type="primary" htmlType="submit">
                        Create Evaluation Request
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
        </div>
    );
};

export default AddNewEvaluationRequest;
