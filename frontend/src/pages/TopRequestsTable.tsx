import { Button, Form, Select, Table } from "antd";
import React, { useState, useEffect, useMemo } from "react";
import axios from "axios";
import { DownloadOutlined } from "@ant-design/icons";

interface Eval {
    questionnaire: string;
    model: string;
    result: string;
}

export default function TopRequestsTable() {
    // const serverUrl = "http://132.73.84.52:5001";
    const serverUrl = "http://127.0.0.1:5001";
    const [data, setData] = useState<Eval[]>([]);
    const [loading, setLoading] = useState(true);
    const [selectedQuestionnaire, setSelectedQuestionnaire] = useState("All");
    const [allQues, setAllQues] = useState<string[]>([]);
    const { Option } = Select;

    useEffect(() => {
        const fetchData = async () => {
            await getAllQuestionnaires();
            try {
                const response = await axios.get(`${serverUrl}/top-requests`);
                console.log("Response data top requests:", response.data);
                setData(response.data.evals);
                setLoading(false);
            } catch (error) {
                console.error("Error fetching data:", error);
                setLoading(false);
            }
        };
        fetchData();
    }, []);

    const handleQuestionnaireChange = (value: string) => {
        console.log("Selected questionnaire:", value);
        setSelectedQuestionnaire(value);
    };

    const getAllQuestionnaires = async () => {
        try {
            const response = await axios.get(`${serverUrl}/get-all-ques`);
            console.log("Response data:", response.data);
            setAllQues(["All", ...response.data.questionnaires]);
        } catch (error) {
            console.error("Error fetching data:", error);
        }
    };

    const filteredData = useMemo(() => {
        const filtered = selectedQuestionnaire && selectedQuestionnaire !== "All"
            ? data.filter(item => item.questionnaire === selectedQuestionnaire)
            : data;
        console.log("Filtered data inside useMemo:", filtered);
        return filtered;
    }, [data, selectedQuestionnaire]);

    const columns = [
        {
            title: "Questionnaire",
            dataIndex: "questionnaire",
            key: "questionnaire",
        },
        {
            title: "Model",
            dataIndex: "model",
            key: "model",
        },
        {
            title: "Result",
            dataIndex: "result",
            key: "result",
        },
    ];

    const extractCSV = async () => {
        try {
            // const response = await axios.get(`${serverUrl}/download-csv`, { responseType: 'blob' });
            const response = await axios.post(`${serverUrl}/download-csv`, filteredData, { responseType: 'blob' });
            const url = window.URL.createObjectURL(new Blob([response.data]));
            const link = document.createElement('a');
            link.href = url;
            link.setAttribute('download', 'records.csv');
            document.body.appendChild(link);
            link.click();
            link.remove();
        } catch (error) {
            console.error("Error extracting CSV file", error);
        }
    };

    return (
        <>
            <Form.Item label="Select Questionnaire" style={{ width: "15%" }}>
                <Select
                    placeholder="Select a questionnaire"
                    onChange={handleQuestionnaireChange}
                    value={selectedQuestionnaire}
                >
                    {allQues.map((q, index) => (
                        <Option value={q} key={index}>
                            {q}
                        </Option>
                    ))}
                </Select>
            </Form.Item>

            <Table
                key={selectedQuestionnaire} // Force re-render when selectedQuestionnaire changes
                columns={columns}
                dataSource={filteredData}
                loading={loading}
                rowKey="model"
                style={{ width: "100%", height: "100%" }}
            />

            <Button type="primary" htmlType="submit" onClick={extractCSV} style={{ marginTop: "20px" }}>
                Download all results 
                <DownloadOutlined style={{ marginLeft: 10 }} />
            </Button>
        </>
    );
}
