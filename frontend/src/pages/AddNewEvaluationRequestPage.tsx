import React from "react";
import { Checkbox, Col, Row, Button, Input, Form } from "antd";
import { Flex } from "antd";
import MainTitle from "./MainTitle";
import MainPageTable from "./MainPageTable";
import { CheckboxValueType } from "antd/es/checkbox/Group";

const onChange = (checkedValues: CheckboxValueType[]) => {
    console.log("checked = ", checkedValues);
};

const AddNewEvaluationRequest = () => {
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
                </div>
            </div>
            <Form
                layout="vertical"
                style={{ marginTop: "20px", width: "100%" }}
            >
                <Button type="primary" htmlType="submit">
                    Create Evaluation Request
                </Button>
            </Form>
        </div>
    );
};

export default AddNewEvaluationRequest;
