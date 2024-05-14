import { Table, TableProps } from "antd";
import React from "react";

export default function EvalRequestsTable() {
    function generateColumns() {
        //const columns: TableProps["columns"] = [];
        const columns: { title: string; dataIndex: string; key: string }[] = [];

        columns.push(
            {
                title: "Model",
                dataIndex: "model",
                key: "model",
            },
            {
                title: "Questionnaire",
                dataIndex: "questionnaire",
                key: "questionnaire",
            },
            {
                title: "Result",
                dataIndex: "result",
                key: "result",
            }
        );

        return columns;
    }

    return (
        <Table
            columns={generateColumns()}
            dataSource={[
                {
                    model: "NLP1",
                    questionnaire: "ASI",
                    result: "0.8",
                },
                {
                    model: "NLP2",
                    questionnaire: "BIG5",
                    result: "0.56",
                },
                {
                    model: "NLP3",
                    questionnaire: "ASI",
                    result: "0.9",
                },
            ]}
            style={{ width: "100%", height: "100%" }}
        />
    );
}
