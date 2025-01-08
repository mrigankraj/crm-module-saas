import React, { useState, useEffect } from 'react';
import axios from 'axios';
import { useAuth } from '../contexts/AuthContext';
import { CheckCircleIcon, XCircleIcon } from '@heroicons/react/solid';

const OnboardingProgress = () => {
  const [progress, setProgress] = useState(0);
  const [tasks, setTasks] = useState([]);
  const { token } = useAuth();

  useEffect(() => {
    fetchProgress();
  }, []);

  const fetchProgress = async () => {
    try {
      const response = await axios.get('/api/onboarding/progress', {
        headers: { Authorization: `Bearer ${token}` }
      });
      setProgress(response.data.progress);
      setTasks(response.data.tasks);
    } catch (error) {
      console.error('Error fetching progress:', error);
    }
  };

  const completeTask = async (taskId) => {
    try {
      await axios.put(`/api/onboarding/tasks/${taskId}/complete`, null, {
        headers: { Authorization: `Bearer ${token}` }
      });
      fetchProgress();
    } catch (error) {
      console.error('Error completing task:', error);
    }
  };

  return (
    <div className="max-w-4xl mx-auto">
      <h1 className="text-3xl font-bold mb-8">Onboarding Progress</h1>
      
      {/* Progress Bar */}
      <div className="mb-8">
        <div className="w-full bg-gray-200 rounded-full h-4">
          <div
            className="bg-blue-600 rounded-full h-4 transition-all duration-500"
            style={{ width: `${progress}%` }}
          />
        </div>
        <p className="text-center mt-2">{Math.round(progress)}% Complete</p>
      </div>

      {/* Task List */}
      <div className="space-y-4">
        {tasks.map((task) => (
          <div
            key={task.id}
            className="bg-white p-4 rounded-lg shadow flex items-center justify-between"
          >
            <div>
              <h3 className="font-semibold">{task.title}</h3>
              <p className="text-gray-600">{task.description}</p>
            </div>
            
            {task.status === 'completed' ? (
              <CheckCircleIcon className="h-8 w-8 text-green-500" />
            ) : (
