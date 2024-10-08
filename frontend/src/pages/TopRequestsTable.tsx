import { Button, Form, Select, Table, message } from "antd";
import React, { useState, useEffect, useMemo } from "react";
import axios, { AxiosError } from "axios";
import { DownloadOutlined, ReloadOutlined } from "@ant-design/icons";

interface Eval {
    questionnaire: string;
    model: string;
    result: string;
}

interface ErrorResponse {
    error: string;
}

export default function TopRequestsTable() {
    const serverUrl = "https://nlp-cetrification.cs.bgu.ac.il/api";
    const [data, setData] = useState<Eval[]>([]);
    const [loading, setLoading] = useState(true);
    const [selectedQuestionnaire, setSelectedQuestionnaire] = useState("All");
    const [allQues, setAllQues] = useState<string[]>([]);
    const { Option } = Select;

    useEffect(() => {
        fetchData();
        getAllQuestionnaires();
    }, []);

    const fetchData = async () => {
    setLoading(true);
        try {
            const response = await axios.get(`${serverUrl}/top-requests`);
            console.log("Response data top requests:", response.data);
            setData(response.data.evals);
            setLoading(false);
        } catch (error) {
            console.error("Error fetching data:", error);
            const axiosError = error as AxiosError<ErrorResponse>;
            const errorMessage = axiosError.response?.data?.error || 'Error fetching data';
            message.error(`Error: ${errorMessage}`);
            setLoading(false);
        }
    };

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
            const axiosError = error as AxiosError<ErrorResponse>;
            const errorMessage = axiosError.response?.data?.error || 'Error fetching questionnaires';
            message.error(`Error: ${errorMessage}`);
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
            render: (model: string) => {
            const url = `https://huggingface.co/${model}`;
            return <a href={url} target="_blank" rel="noopener noreferrer">{model}</a>;
            }
        },
        {
            title: "Result",
            dataIndex: "result",
            key: "result",
            render: (text: string | number) => {
                console.log("Result text:", text); // Debugging line
                if (text === -999) return "Evaluation failed";
                if (text === -9999) return "Model is not compatible, evaluation failed";
                if (text === -99999) return <span style={{ color: "blue" }}>Waiting for evaluation</span>;
                if (!text || text === "") return <span style={{ color: "blue" }}>Waiting for evaluation</span>;
                if (typeof text === "string") {
                    text = parseFloat(text);
                }

                if (typeof text === "number") {
                    text = text.toFixed(5);
                }
                return text;
            },
        },
    ];

    const extractCSV = async () => {
        try {
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
            const axiosError = error as AxiosError<ErrorResponse>;
            const errorMessage = axiosError.response?.data?.error || 'Error extracting CSV file';
            message.error(`Error: ${errorMessage}`);
        }
    };

    const extractCSVAll = async () => {
        try {
            const response = await axios.post(`${serverUrl}/download-csv-all`, { responseType: 'blob' });
            const url = window.URL.createObjectURL(new Blob([response.data]));
            const link = document.createElement('a');
            link.href = url;
            link.setAttribute('download', 'records.csv');
            document.body.appendChild(link);
            link.click();
            link.remove();
        } catch (error) {
            console.error("Error extracting CSV file", error);
            const axiosError = error as AxiosError<ErrorResponse>;
            const errorMessage = axiosError.response?.data?.error || 'Error extracting CSV file';
            message.error(`Error: ${errorMessage}`);
        }
    };

    return (
        <>
            <div style={{ display: "flex", justifyContent: "space-between", alignItems: "center", marginBottom: 20 }}>
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
                <Button type="primary" icon={<ReloadOutlined />} onClick={fetchData}>
                    Refresh
                </Button>
            </div>

            <Table
                key={selectedQuestionnaire} // Force re-render when selectedQuestionnaire changes
                columns={columns}
                dataSource={filteredData}
                loading={loading}
                rowKey="model"
                style={{ width: "100%", height: "100%" }}
            />

            <Button type="primary" htmlType="submit" onClick={extractCSV} style={{ marginTop: "20px" }}>
                Download top results 
                <DownloadOutlined style={{ marginLeft: 10 }} />
            </Button>
            <br/>
            <Button type="primary" htmlType="submit" onClick={extractCSVAll} style={{ marginTop: "20px" }}>
                Download all evaluations results 
                <DownloadOutlined style={{ marginLeft: 10 }} />
            </Button>
        </>
    );
}
