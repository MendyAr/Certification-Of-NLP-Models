import { Button, Flex } from "antd";
import MainTitle from "./MainTitle";
import { useNavigate, useParams } from "react-router-dom";
import React from 'react';

export default function Project() {
    const navigate = useNavigate();
    const { projectName } = useParams();

    return (
        <Flex
            vertical
            justify="center"
            align="center"
            gap={50}
            style={{ height: "100%" }}
        >
            <MainTitle title1={`Project: ${projectName}`} title2="" />
            <Flex vertical gap={30}>
                <Button
                    type="primary"
                    onClick={() =>
                        navigate(`/my-projects/${projectName}/new-eval-request`)
                    }
                >
                    Add new evaluation request
                </Button>
                <Button
                    type="primary"
                    onClick={() =>
                        navigate(`/my-projects/${projectName}/eval-requests`)
                    }
                >
                    Show Previous evaluation requests
                </Button>
            </Flex>
        </Flex>
    );
}
