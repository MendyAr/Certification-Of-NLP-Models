import { Flex } from "antd";
import MainTitle from "./MainTitle";
import MainPageTable from "./MainPageTable";

export default function EvalRequests() {
    return (
        <Flex vertical justify="center" gap={50} style={{ height: "100%" }}>
            <MainTitle
                title1="Project1: aci + nlp"
                title2="Previous Evaluation Requests"
            />
            <MainPageTable />
        </Flex>
    );
}
