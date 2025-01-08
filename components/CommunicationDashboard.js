import React, { useState } from 'react';
import axios from 'axios';

export default function CommunicationDashboard() {
    const [message, setMessage] = useState('');
    const [communications, setCommunications] = useState([]);

    const sendMessage = async () => {
        await axios.post('/api/communication/send', {
            type: 'email',
            content: message
        });
        setMessage('');
        fetchCommunications();
    };

    return (
        <div className="container mx-auto p-4">
            <h2 className="text-2xl font-bold mb-4">Communication Dashboard</h2>
            <div className="mb-4">
                <textarea
                    value={message}
                    onChange={(e) => setMessage(e.target.value)}
                    className="w-full p-2 border rounded"
                />
                <button
                    onClick={sendMessage}
                    className="bg-blue-500 text-white px-4 py-2 rounded"
                >
                    Send Message
                </button>
            </div>
            <div className="mt-4">
                {communications.map(comm => (
                    <div key={comm.id} className="border p-4 mb-2 rounded">
                        <p>{comm.content}</p>
                        <small>{new Date(comm.created_at).toLocaleString()}</small>
                    </div>
                ))}
            </div>
        </div>
    );
}
