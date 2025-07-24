// FRONTEND - React (Vite-based setup)
// Directory: frontend/src/App.jsx

import React, { useState } from 'react';
import axios from 'axios';
import './App.css';

function App() {
  const [text, setText] = useState('');
  const [summary, setSummary] = useState('');
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState('');

  const handleSummarize = async () => {
    if (!text.trim()) return;
    setLoading(true);
    setError('');
    setSummary('');
    try {
      const response = await axios.post('http://127.0.0.1:5000/summarize', { text });
      setSummary(response.data.summary);
    } catch (err) {
      setError('Failed to summarize. Please try again.');
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="app">
      <h1>Text Summarizer</h1>
      <textarea
        value={text}
        onChange={(e) => setText(e.target.value)}
        placeholder="Enter text here..."
        rows={10}
      />
      <button onClick={handleSummarize} disabled={loading}>
        {loading ? 'Summarizing...' : 'Summarize'}
      </button>
      {summary && (
        <div className="summary-box">
          <h3>Summary:</h3>
          <p>{summary}</p>
        </div>
      )}
      {error && <p className="error">{error}</p>}
    </div>
  );
}

export default App;
