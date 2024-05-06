import { Table, TableProps } from "antd";
import React from "react";

export default function MainPageTable() {
  function generateColumns() {
    //const columns: TableProps["columns"] = [];
    const columns: { title: string; dataIndex: string; key: string }[] = [];

    columns.push(
      {
        title: "Name",
        dataIndex: "name",
        key: "name",
      },
      {
        title: "Age",
        dataIndex: "age",
        key: "age",
      }
    );

    return columns;
  }

  return (
    <Table
      columns={generateColumns()}
      dataSource={[
        {
          age: 1,
          name: "John",
        },
      ]}
      style={{ width: "100%", height: "100%" }}
    />
  );
}
