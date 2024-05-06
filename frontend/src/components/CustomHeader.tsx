import { Button, Flex, Menu, Switch, Typography } from "antd";
import { useDispatch, useSelector } from "react-redux";
import { MoonFilled, SunFilled, UserOutlined } from "@ant-design/icons";
import { RootState } from "../redux/store";
import { setTheme } from "../redux/slices/ThemeSlice";
import { MenuItem } from "../utils/Types";
import { getMenuItem } from "../utils/Utils";
import { useNavigate } from "react-router-dom";

function getSwitchBackgroundColor(isLight: boolean) {
  return isLight ? "#dcb92b" : "#4469cb";
}

export default function CustomHeader() {
  const { isLight } = useSelector((state: RootState) => state.theme);
  const dispatch = useDispatch();
  const navigate = useNavigate();

  const items: MenuItem[] = [
    // getMenuItem({ key: "myAccount", label: "My Account", icon: <UserOutlined /> })
  ];

  return (
    <Flex style={{ width: "100%" }} align="center" gap={8}>
      <Typography.Title style={{ color: "white", paddingBottom: 10, cursor: "pointer" }} onClick={() => navigate("/")}>
        Modals Bias Detector
      </Typography.Title>
      <Menu theme="dark" mode="horizontal" items={items} style={{ flex: 1, minWidth: 0 }} />
      <Button
        onClick={() => navigate("my-account")}
        icon={<UserOutlined />}
        style={{ backgroundColor: "transparent", color: "white" }}
      >
        My Account
      </Button>
      <Switch
        unCheckedChildren={<MoonFilled />}
        checkedChildren={<SunFilled />}
        defaultChecked={isLight}
        onChange={(checked) => dispatch(setTheme(checked))}
        style={{ backgroundColor: getSwitchBackgroundColor(isLight) }}
      />
    </Flex>
  );
}
