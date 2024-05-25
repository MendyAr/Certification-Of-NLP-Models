import { Button, Flex } from "antd";
import MainTitle from "./MainTitle";
import { Outlet, useNavigate } from "react-router-dom";

export default function Project() {
    const navigate = useNavigate();

    return (
        <Flex
            vertical
            justify="center"
            align="center"
            gap={50}
            style={{ height: "100%" }}
        >
            <MainTitle title1="Project 1: ASI + NLP1 " title2="" />
            <Flex vertical gap={30}>
                <Button
                    type="primary"
                    onClick={() =>
                        navigate("/my-projects/project/new-eval-request")
                    }
                >
                    Add new evaluation request
                </Button>
                <Button
                    type="primary"
                    onClick={() =>
                        navigate("/my-projects/project/Eval-Requests")
                    }
                >
                    Show Previous evaluation requests
                </Button>
            </Flex>
        </Flex>
    );
}
