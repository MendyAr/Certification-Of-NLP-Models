
import React, { useState, ChangeEvent } from 'react';
import { Checkbox, Col, Row, Button, Input, Form, Modal, Flex } from 'antd';
import MainTitle from './MainTitle';
import { CheckboxValueType } from 'antd/es/checkbox/Group';
import MainPageTable from "./MainPageTable";


const onChange = (checkedValues: CheckboxValueType[]) => {
    console.log("checked = ", checkedValues);
};

const AddNewProject = () => {

  const [isModalVisible, setIsModalVisible] = useState(false);
  const [modelUrl, setModelUrl] = useState('');

  const showModal = () => {
    setIsModalVisible(true);
  };

  const handleOk = () => {
    console.log('Model URL:', modelUrl);
    // Handle adding the model URL to the project here
    setIsModalVisible(false); 
    setModelUrl('');
  };

  const handleCancel = () => {
    setIsModalVisible(false);
    setModelUrl('');
  };

  const handleUrlChange = (e: ChangeEvent<HTMLInputElement>) => {
    setModelUrl(e.target.value);
  };

  return (
    <div style={{ padding: '20px' }}>
      <div style={{ display: 'flex', justifyContent: 'space-between', marginBottom: '20px' }}>
        <div style={{ width: '45%' }}>
           <Flex align="left">
                        <MainTitle title1="Select Model" title2="" />
                    </Flex>

          <Checkbox.Group style={{ width: '100%' }} onChange={onChange}>
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
          <Button type="dashed" style={{ marginTop: '10px' }} onClick={showModal}>
            Click to add more models
          </Button>
        </div>
        <div style={{ width: '45%' }}>
           <Flex align="left">
                        <MainTitle title1="Select Questionnaire" title2="" />
                    </Flex>
          <Checkbox.Group style={{ width: '100%' }} onChange={onChange}>
            <Row>
              <Col span={12}>
                <Checkbox value="Questionnaire1">Questionnaire 1</Checkbox>
              </Col>
              <Col span={12}>
                <Checkbox value="Questionnaire2">Questionnaire 2</Checkbox>
              </Col>
              <Col span={12}>
                <Checkbox value="Questionnaire3">Questionnaire 3</Checkbox>
              </Col>
              <Col span={12}>
                <Checkbox value="Questionnaire4">Questionnaire 4</Checkbox>
              </Col>
              <Col span={12}>
                <Checkbox value="Questionnaire5">Questionnaire 5</Checkbox>
              </Col>
              <Col span={12}>
                <Checkbox value="Questionnaire6">Questionnaire 6</Checkbox>
              </Col>
            </Row>
          </Checkbox.Group>
          <Button type="dashed" style={{ marginTop: '10px' }} onClick={showModal}>
            Click to add more Questionnaire
          </Button>
        </div>
      </div>
      <Form layout="vertical" style={{ marginTop: '20px', width: '100%' }}>
        <Form.Item label="Project Name">
          <Input placeholder="Enter project name" />
        </Form.Item>
        <Form.Item>
          <Button type="primary" htmlType="submit">
            Create Project
          </Button>
        </Form.Item>
      </Form>

      <Modal
        title="Add Model"
        visible={isModalVisible}
        onOk={handleOk}
        onCancel={handleCancel}
      >
        <Form layout="vertical">
          <Form.Item label="Model URL">
            <Input placeholder="Enter model URL" value={modelUrl} onChange={handleUrlChange} />
          </Form.Item>
          <Form.Item>
            <Button type="primary" onClick={handleOk}>
              Add to Project
            </Button>
          </Form.Item>
        </Form>
      </Modal>
    </div>
  );
};

export default AddNewProject;
