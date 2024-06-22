import { Table } from "antd";
import React, { useState, useEffect } from "react";
import axios from "axios";
import { RootState } from "../redux/store";
import { useSelector } from "react-redux";

export default function TopRequestsTable() {
    const token = useSelector((state: RootState) => state.auth.token);
    const serverUrl = "http://127.0.0.1:3000"
    const [data, setData] = useState([]);
    const [loading, setLoading] = useState(true); // Ensure loading state is defined

    useEffect(() => {
        const fetchData = async () => {
            try {
                const response = await axios.get(
                    `${serverUrl}/top-requests`);
                console.log("Response data top requests:", response.data); // Debugging line
                setData(response.data.evals);
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
