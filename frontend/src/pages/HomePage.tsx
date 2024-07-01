import { Button, Flex, Form } from "antd";
import MainTitle from "./MainTitle";
import TopRequestsTable from "./TopRequestsTable";
import React, { useState } from 'react';
import { useSelector } from "react-redux";
import { RootState } from "../redux/store";
import axios from "axios";
import { useNavigate } from "react-router-dom";
import { DownloadOutlined } from "@ant-design/icons";

export default function HomePage() {
    const token = useSelector((state: RootState) => state.auth.token);
    const serverUrl = "http://132.73.84.52:5001"

    const extractCSV = async () => {
        try {
            const response = await axios.get(`${serverUrl}/download-csv`, { responseType: 'blob' });
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
        <Flex vertical justify="center" gap={50} style={{ height: "100%" }}>
            <MainTitle
                    title1="Top Evaluations"
                    title2="Evaluations most requested by users"
            />
            <TopRequestsTable />
            <Form.Item>
            <Button type="primary" htmlType="submit" onClick={extractCSV}>
                Download all results 
                <DownloadOutlined style={{ marginLeft: 10 }} /> {/* Move icon to the right of the text */}
            </Button>
            </Form.Item>
      
        </Flex>
    );
}
