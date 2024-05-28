import { Table } from "antd";
import React, { useState, useEffect } from "react";
import axios from "axios";

export default function EvalRequestsTable() {
    const [data, setData] = useState([]);
    const [loading, setLoading] = useState(true); // Ensure loading state is defined

    useEffect(() => {
        const fetchData = async () => {
            try {
                const response = await axios.get(
                    "http://127.0.0.1:5001/eval-requests",
                    {
                        params: {
                            project: "ProjectA",
                            email: "user1@example.com",
                        },
                    }
                );
                console.log("Response data:", response.data); // Debugging line
                setData(response.data);
                setLoading(false); // Update loading state
            } catch (error) {
                console.error("Error fetching data:", error);
                setLoading(false); // Update loading state in case of error
            }
        };
        fetchData();
    }, []);

    const columns = [
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
        },
    ];

    return (
        <Table
            columns={columns}
            dataSource={data}
            loading={loading} // Pass loading state to Table component
            rowKey="model"
            style={{ width: "100%", height: "100%" }}
        />
    );
}
