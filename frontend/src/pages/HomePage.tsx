import { Flex } from "antd";
import MainTitle from "./MainTitle";
import MainPageTable from "./MainPageTable";

export default function HomePage() {
    return (
        <Flex vertical justify="center" gap={50} style={{ height: "100%" }}>
            <MainTitle
                title1="Top Evaluations"
                title2="All system evaluations requests"
            />
            <MainPageTable />
        </Flex>
    );
}
