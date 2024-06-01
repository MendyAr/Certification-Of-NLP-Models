import { Flex, Typography } from "antd";

export default function MainTitle({
    title1,
    title2,
}: {
    title1: string;
    title2: string;
}) {
    return (
        <Flex vertical align="center" gap={8}>
            <Typography.Title style={{ margin: 0 }}>{title1}</Typography.Title>
            <Typography.Title level={5} style={{ margin: 0, color: "#588FCD" }}>
                {title2}
            </Typography.Title>
        </Flex>
    );
}
