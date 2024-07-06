import React from 'react';
import { useParams } from 'react-router-dom';
import { Flex, Form } from "antd";
import MainTitle from "./MainTitle";
import EvalRequestsTable from "./EvalRequestsTable";

export default function EvalRequests() {
    const { projectName } = useParams();

    return (
        <Flex vertical gap={50} style={{ height: "150%" }}>
            <Form.Item>
                <MainTitle
                    title1={`Project: ${projectName}`}
                    title2="Evaluations Results"
                />
                <EvalRequestsTable />
            </Form.Item>
        </Flex>
    );
}
