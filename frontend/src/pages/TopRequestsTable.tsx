import { Table } from "antd";
import React, { useState, useEffect } from "react";
import axios from "axios";

export default function TopRequestsTable() {
    const serverUrl = "http://132.73.84.52:5001";
    const [data, setData] = useState([]);
    const [loading, setLoading] = useState(true); // Ensure loading state is defined

    useEffect(() => {
        const fetchData = async () => {
            try {
                const response = await axios.get(`${serverUrl}/top-requests`);
                console.log("Response data top requests:", response.data); // Debugging line
                setData(response.data.evals); 
                setLoading(false); 
            } catch (error) {
                console.error("Error fetching data:", error);
                setLoading(false);
            }
        };
        fetchData();
    }, []); 

    useEffect(() => {
    }, [data]); // Log whenever `data` changes

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
            loading={loading} 
            rowKey="model" 
            style={{ width: "100%", height: "100%" }}
        />
    );
}
