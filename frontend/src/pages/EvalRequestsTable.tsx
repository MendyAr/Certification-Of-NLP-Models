import { Button, Form, Select, Table, message } from "antd";
import React, { useState, useEffect, useMemo } from "react";
import axios, { AxiosError } from "axios";
import { RootState } from "../redux/store";
import { useSelector } from "react-redux";
import { useParams } from "react-router-dom";
import { DownloadOutlined, ReloadOutlined } from "@ant-design/icons";

interface Eval {
    questionnaire: string;
    model: string;
    result: string;
}

interface ErrorResponse {
    error: string;
}

export default function EvalRequestsTable() {
    const token = useSelector((state: RootState) => state.auth.token);
    const serverUrl = "http://132.73.84.52:5001"
    const { projectName } = useParams();
    const [data, setData] = useState<Eval[]>([]);
    const [loading, setLoading] = useState(true); // Ensure loading state is defined
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
            const response = await axios.get(`${serverUrl}/eval-requests`, {
                    params: {
                        project: projectName,
                    },
                    headers: {
                        Authorization: `${token}` // Add the token to the request headers
                    },
                }
            );
            console.log("Response data:", response.data); // Debugging line
            setData(response.data.evals);
            setLoading(false); // Update loading state
        } catch (error) {
            console.error("Error fetching data:", error);
            const axiosError = error as AxiosError<ErrorResponse>;
            const errorMessage = axiosError.response?.data?.error || 'Error fetching data';
            message.error(`Error: ${errorMessage}`);
            setLoading(false);
        }
    };

    // useEffect(() => {
    // }, [data]); // Log whenever `data` changes

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
                return text;
            },
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
                Download project results 
                <DownloadOutlined style={{ marginLeft: 10 }} />
            </Button>
        </>
    );
}
