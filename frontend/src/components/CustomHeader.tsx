import { Menu, Switch, Typography } from "antd";
import { useDispatch, useSelector } from "react-redux";
import { MoonFilled, SunFilled } from "@ant-design/icons";
import { RootState } from "../redux/store";
import { setTheme } from "../redux/slices/ThemeSlice";

function getSwitchBackroundColor(isLight: boolean) {
    return isLight ? "#dcb92b" : "#4469cb";
}

export default function CustomHeader() {
    const { isLight } = useSelector((state: RootState) => state.theme);
    const dispatch = useDispatch();

    return (
        <>
            <Typography.Title style={{ color: "white", paddingBottom: 10 }}>
                Talentflow
            </Typography.Title>
            <Menu
                theme="dark"
                mode="horizontal"
                style={{ flex: 1, minWidth: 0 }}
            />
            <Switch
                unCheckedChildren={<MoonFilled />}
                checkedChildren={<SunFilled />}
                defaultChecked={isLight}
                onChange={(checked) => dispatch(setTheme(checked))}
                style={{ backgroundColor: getSwitchBackroundColor(isLight) }}
            />
                
        </>
    );
}
