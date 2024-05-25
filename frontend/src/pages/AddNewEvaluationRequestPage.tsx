import React, { useState, ChangeEvent } from "react";
import {
    Checkbox,
    Col,
    Row,
    Button,
    Input,
    Form,
    Modal,
    Select,
    Flex,
} from "antd";
import MainTitle from "./MainTitle";
import { CheckboxValueType } from "antd/es/checkbox/Group";
import MainPageTable from "./MainPageTable";

const { Option } = Select;

const onChange = (checkedValues: CheckboxValueType[]) => {
    console.log("checked = ", checkedValues);
};

const AddNewProject = () => {
    const [isModelModalVisible, setIsModelModalVisible] = useState(false);
    const [isQuestionnaireModalVisible, setIsQuestionnaireModalVisible] =
        useState(false);
    const [modelUrl, setModelUrl] = useState("");
    const [selectedQuestionnaire, setSelectedQuestionnaire] = useState("");

    const showModelModal = () => {
        setIsModelModalVisible(true);
    };

    const showQuestionnaireModal = () => {
        setIsQuestionnaireModalVisible(true);
    };

    const handleModelOk = () => {
        console.log("Model URL:", modelUrl);
        // Handle adding the model URL to the project here
        setIsModelModalVisible(false);
        setModelUrl("");
    };

    const handleQuestionnaireOk = () => {
        console.log("Selected Questionnaire:", selectedQuestionnaire);
        // Handle adding the selected questionnaire to the project here
        setIsQuestionnaireModalVisible(false);
        setSelectedQuestionnaire("");
    };

    const handleModelCancel = () => {
        setIsModelModalVisible(false);
        setModelUrl("");
    };

    const handleQuestionnaireCancel = () => {
        setIsQuestionnaireModalVisible(false);
        setSelectedQuestionnaire("");
    };

    const handleModelUrlChange = (e: ChangeEvent<HTMLInputElement>) => {
        setModelUrl(e.target.value);
    };

    const handleQuestionnaireChange = (value: string) => {
        setSelectedQuestionnaire(value);
    };

    return (
        <div style={{ padding: "20px" }}>
            <div
                style={{
                    display: "flex",
                    justifyContent: "space-between",
                    marginBottom: "20px",
                }}
            >
                <div style={{ width: "45%" }}>
                    <Flex align="left">
                        <MainTitle title1="Select Model" title2="" />
                    </Flex>
                    <Checkbox.Group
                        style={{ width: "100%" }}
                        onChange={onChange}
                    >
                        <Row>
                            <Col span={12}>
                                <Checkbox value="Model1">Model 1</Checkbox>
                            </Col>
                            <Col span={12}>
                                <Checkbox value="Model2">Model 2</Checkbox>
                            </Col>
                            <Col span={12}>
                                <Checkbox value="Model3">Model 3</Checkbox>
                            </Col>
                            <Col span={12}>
                                <Checkbox value="Model4">Model 4</Checkbox>
                            </Col>
                        </Row>
                    </Checkbox.Group>
                    <Button
                        type="dashed"
                        style={{ marginTop: "10px" }}
                        onClick={showModelModal}
                    >
                        Click to add more models
                    </Button>
                </div>
                <div style={{ width: "45%" }}>
                    <Flex align="left">
                        <MainTitle title1="Select Questionnaire" title2="" />
                    </Flex>
                    <Checkbox.Group
                        style={{ width: "100%" }}
                        onChange={onChange}
                    >
                        <Row>
                            <Col span={12}>
                                <Checkbox value="Questionnaire1">
                                    Questionnaire 1
                                </Checkbox>
                            </Col>
                            <Col span={12}>
                                <Checkbox value="Questionnaire2">
                                    Questionnaire 2
                                </Checkbox>
                            </Col>
                            <Col span={12}>
                                <Checkbox value="Questionnaire3">
                                    Questionnaire 3
                                </Checkbox>
                            </Col>
                            <Col span={12}>
                                <Checkbox value="Questionnaire4">
                                    Questionnaire 4
                                </Checkbox>
                            </Col>
                            <Col span={12}>
                                <Checkbox value="Questionnaire5">
                                    Questionnaire 5
                                </Checkbox>
                            </Col>
                            <Col span={12}>
                                <Checkbox value="Questionnaire6">
                                    Questionnaire 6
                                </Checkbox>
                            </Col>
                        </Row>
                    </Checkbox.Group>
                    <Button
                        type="dashed"
                        style={{ marginTop: "10px" }}
                        onClick={showQuestionnaireModal}
                    >
                        Click to add more Questionnaire
                    </Button>
                </div>
            </div>
            <Form
                layout="vertical"
                style={{ marginTop: "20px", width: "100%" }}
            >
                <Form.Item>
                    <Button type="primary" htmlType="submit">
                        Create Evaluation Request
                    </Button>
                </Form.Item>
            </Form>

            <Modal
                title="Add Model"
                visible={isModelModalVisible}
                onOk={handleModelOk}
                onCancel={handleModelCancel}
            >
                <Form layout="vertical">
                    <Form.Item label="Model URL">
                        <Input
                            placeholder="Enter model URL"
                            value={modelUrl}
                            onChange={handleModelUrlChange}
                        />
                    </Form.Item>
                    <Form.Item>
                        <Button type="primary" onClick={handleModelOk}>
                            Add to Project
                        </Button>
                    </Form.Item>
                </Form>
            </Modal>

            <Modal
                title="Add Questionnaire"
                visible={isQuestionnaireModalVisible}
                onOk={handleQuestionnaireOk}
                onCancel={handleQuestionnaireCancel}
            >
                <Form layout="vertical">
                    <Form.Item label="Select Questionnaire">
                        <Select
                            placeholder="Select a questionnaire"
                            onChange={handleQuestionnaireChange}
                            value={selectedQuestionnaire}
                        >
                            <Option value="Questionnaire1">
                                Questionnaire 1
                            </Option>
                            <Option value="Questionnaire2">
                                Questionnaire 2
                            </Option>
                            <Option value="Questionnaire3">
                                Questionnaire 3
                            </Option>
                            <Option value="Questionnaire4">
                                Questionnaire 4
                            </Option>
                            <Option value="Questionnaire5">
                                Questionnaire 5
                            </Option>
                            <Option value="Questionnaire6">
                                Questionnaire 6
                            </Option>
                        </Select>
                    </Form.Item>
                    <Form.Item>
                        <Button type="primary" onClick={handleQuestionnaireOk}>
                            Add to Project
                        </Button>
                    </Form.Item>
                </Form>
            </Modal>
        </div>
    );
};

export default AddNewProject;
