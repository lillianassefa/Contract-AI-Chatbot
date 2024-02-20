import React, { useState } from 'react';
import './App.css';

function App() {
  const [inputText, setInputText] = useState('');
  const [outputText, setOutputText] = useState('');
  const [ragEvaluation, setRagEvaluation] = useState(null);

  const handleTextChange = (e) => {
    setInputText(e.target.value);
  };

  const handleFileUpload = (e) => {
    const file = e.target.files[0];
    // Add logic to handle file upload and process the file content
  };

  const handleProcessText = () => {
    // Add logic to send inputText to the backend and receive the outputText and RAG evaluation
    const sampleRagEvaluation = {
      faithfulness: 'High',
      answerRelevancy: 'Medium',
      contextRelevancy: 'High',
      contextRecall: 'Low'
    };
    setOutputText('This is a sample output from the RAG system based on the input: ' + inputText);
    setRagEvaluation(sampleRagEvaluation);
  };

  return (
    <div className="app">
      <header>
        <h1>Contract Q&A RAG System</h1>
      </header>
      <div className="container">
        <div className="input-box">
          <h2>Input</h2>
          <textarea
            value={inputText}
            onChange={handleTextChange}
            placeholder="Paste your text here..."
            rows="8"
          ></textarea>
          <input type="file" onChange={handleFileUpload} />
          <button onClick={handleProcessText}>Process Text</button>
        </div>
        <div className="output-box">
          <h2>Output</h2>
          <p>{outputText}</p>
        </div>
      </div>
      <div className="rag-evaluation">
        <h2>RAG Evaluation</h2>
        <table>
          <thead>
            <tr>
              <th>Faithfulness</th>
              <th>Answer Relevancy</th>
              <th>Context Relevancy</th>
              <th>Context Recall</th>
            </tr>
          </thead>
          <tbody>
            {ragEvaluation && (
              <tr>
                <td>{ragEvaluation.faithfulness}</td>
                <td>{ragEvaluation.answerRelevancy}</td>
                <td>{ragEvaluation.contextRelevancy}</td>
                <td>{ragEvaluation.contextRecall}</td>
              </tr>
            )}
          </tbody>
        </table>
      </div>
    </div>
  );
}

export default App;
