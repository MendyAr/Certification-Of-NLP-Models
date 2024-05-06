import { Flex, Typography } from "antd";

export default function MainTitle() {
  return (
    <Flex vertical align="center" gap={8}>
      <Typography.Title style={{ margin: 0 }}>Top Evaluations</Typography.Title>
      <Typography.Title level={5} style={{ margin: 0, color: "#588FCD" }}>
        All system evaluations requests
      </Typography.Title>
    </Flex>
  );
}
