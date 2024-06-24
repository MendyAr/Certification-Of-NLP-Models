import React from 'react';
import { useParams } from 'react-router-dom';
import { Flex } from "antd";
import MainTitle from "./MainTitle";
import EvalRequestsTable from "./EvalRequestsTable";
import { useSelector } from 'react-redux';
import { RootState } from '../redux/store';

export default function EvalRequests() {
    const { projectName } = useParams();

    return (
        <Flex vertical justify="center" gap={50} style={{ height: "100%" }}>
            <MainTitle
                title1={`Project: ${projectName}`}
                title2="Previous Evaluation Requests"
            />
            <EvalRequestsTable />
        </Flex>
    );
}
