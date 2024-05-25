import React from 'react';
import { Checkbox, Col, Row, Button, Input, Form } from 'antd';
import { Flex } from 'antd';
import MainTitle from './MainTitle';
import MainPageTable from './MainPageTable';
import { CheckboxValueType } from 'antd/es/checkbox/Group';

const onChange = (checkedValues: CheckboxValueType[]) => {
  console.log('checked = ', checkedValues);
};

const AddNewProject = () => {
  return  (
    <div style={{ padding: '20px' }}>
      <div style={{ display: 'flex', justifyContent: 'space-between', marginBottom: '20px' }}>
        <div style={{ width: '45%' }}>
          <MainTitle 
          title1="Select Model" 
          title2="" /> 
          
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
          <Button type="dashed" style={{ marginTop: '10px' }}>
            Click to add more models
          </Button>
        </div>
        <div  style={{ width: '45%' }}>
          <MainTitle title1="Select Questionnaire" title2=""></MainTitle>
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
          <Button type="dashed" style={{ marginTop: '10px' }}>
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
    </div>
  );
};

export default AddNewProject;
