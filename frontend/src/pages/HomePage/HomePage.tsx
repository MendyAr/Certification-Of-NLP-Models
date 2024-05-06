import { Flex } from "antd";
import MainTitle from "./MainTitle/MainTitle";
import MainPageTable from "./MainPageTable/MainPageTable";

export default function HomePage() {
  return (
    <Flex vertical justify="center" gap={50} style={{ height: "100%" }}>
      <MainTitle />
      <MainPageTable />
    </Flex>
  );
}
