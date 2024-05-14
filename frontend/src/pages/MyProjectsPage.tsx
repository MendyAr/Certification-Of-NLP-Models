import { Button, Flex } from "antd";
import MainTitle from "./MainTitle";
import { useLocation, useNavigate } from "react-router-dom";

export default function MyProjects() {
    const navigate = useNavigate();
    const location = useLocation();

    return (
        <Flex
            vertical
            justify="center"
            align="center"
            gap={50}
            style={{ height: "100%" }}
        >
            <MainTitle title1="My Projects" title2="" />
            <Flex vertical gap={30}>
                <Button
                    type="primary"
                    onClick={() => navigate("/my-projects/project")}
                >
                    Project 1: ASI + NLP1
                </Button>

                <Button
                    type="primary"
                    onClick={() => navigate("/my-projects/project")}
                >
                    Project 2: ASI + NLP1
                </Button>

                <Button
                    type="primary"
                    onClick={() => navigate("/my-projects/project")}
                >
                    Project 3: ASI + NLP1
                </Button>
            </Flex>
        </Flex>
    );
}

// export {};
