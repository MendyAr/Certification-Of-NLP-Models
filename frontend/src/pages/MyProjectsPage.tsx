import MainTitle from "./HomePage/MainTitle/MainTitle";
import MainPageTable from "./HomePage/MainPageTable/MainPageTable";
import { Button, Dropdown, Flex, Menu, MenuProps, Switch, Typography } from "antd";

export default function MyProjects() {
    return (
      <Flex vertical justify="center" gap={50} style={{ height: "100%" }}>
        <MainTitle title1="My Projects" title2=""/>
        <Flex vertical gap={10}>
          <Button type="primary" onClick={() => {/* handle project 1 click */}}>
            Project 1: ASI + NLP1
          </Button>
          <Button type="primary" onClick={() => {/* handle project 2 click */}}>
            Project 2: ASI + NLP1
          </Button>
          <Button type="primary" onClick={() => {/* handle project 3 click */}}>
            Project 3: ASI + NLP1
          </Button>
        </Flex>
        <MainPageTable />
      </Flex>
    );
}
