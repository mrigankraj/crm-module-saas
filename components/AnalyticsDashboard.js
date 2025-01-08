import React, { useEffect, useState } from 'react';
import axios from 'axios';
import {
    LineChart,
    Line,
    XAxis,
    YAxis,
    CartesianGrid,
    Tooltip,
    Legend
} from 'recharts';

export default function AnalyticsDashboard() {
    const [metrics, setMetrics] = useState({});

    useEffect(() => {
        fetchMetrics();
    }, []);

    const fetchMetrics = async () => {
        const response = await axios.get('/api/analytics/engagement');
        setMetrics(response.data);
    };

    return (
        <div className="container mx-auto p-4">
            <h2 className="text-2xl font-bold mb-4">Analytics Dashboard</h2>
            <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
                <div className="border p-4 rounded">
                    <h3 className="text-xl mb-2">Engagement Overview</h3>
                    <LineChart width={500} height={300} data={metrics.engagement_data}>
                        <CartesianGrid strokeDasharray="3 3" />
                        <XAxis dataKey="date" />
                        <YAxis />
                        <Tooltip />
                        <Legend />
                        <Line type="monotone" dataKey="interactions" stroke="#8884d8" />
                    </LineChart>
                </div>
            </div>
        </div>
    );
}
