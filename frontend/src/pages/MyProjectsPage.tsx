
import { Button, Dropdown, Flex, Menu, MenuProps, Switch, Typography } from "antd";
import MainPageTable from "./MainPageTable";
import MainTitle from "./MainTitle";

export default function MyProjects() {
    return (
      <Flex vertical justify="center" align="center" gap={50} style={{ height: "100%"}}>
        <MainTitle title1="My Projects" title2=""/>
        <Flex vertical gap={30}>
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
      </Flex>
    );
}
