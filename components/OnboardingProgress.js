import React, { useState, useEffect } from 'react';
import axios from 'axios';

export default function OnboardingProgress() {
    const [progress, setProgress] = useState(0);
    const [tasks, setTasks] = useState([]);

    useEffect(() => {
        fetchProgress();
    }, []);

    const fetchProgress = async () => {
        const response = await axios.get('/api/onboarding/progress');
        setProgress(response.data.progress);
        setTasks(response.data.tasks);
    };

    return (
        <div className="container mx-auto p-4">
            <h2 className="text-2xl font-bold mb-4">Onboarding Progress</h2>
            <div className="w-full bg-gray-200 rounded-full h-2.5">
                <div 
                    className="bg-blue-600 h-2.5 rounded-full"
                    style={{ width: `${progress}%` }}
                ></div>
            </div>
            <div className="mt-4">
                {tasks.map(task => (
                    <div key={task.id} className="border p-4 mb-2 rounded">
                        <h3>{task.title}</h3>
                        <p>{task.description}</p>
                    </div>
                ))}
            </div>
        </div>
    );
}
