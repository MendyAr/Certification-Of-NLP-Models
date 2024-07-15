import { Flex, Form } from "antd";
import MainTitle from "./MainTitle";
import TopRequestsTable from "./TopRequestsTable";

export default function HomePage() {

    return (
        <Flex vertical gap={50} style={{ height: "150%" }}>
            <Form.Item>
                <MainTitle
                        title1="Top Evaluations"
                        title2="All evaluations ordered by evaluation time"
                />
                <TopRequestsTable />
            </Form.Item>
        </Flex>
    );
}
