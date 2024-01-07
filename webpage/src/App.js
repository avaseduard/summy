import React, { useEffect, useState } from "react";
import logo from "./logo.svg";
import "./App.css";

function App() {
  const [summary, setSummary] = useState("");

  const summarize = () => {
    fetch("http://127.0.0.1:5000/get_summary")
      .then((response) => response.json())
      .then((data) => {
        setSummary(data.summary);
        console.log("data.summary-->", data.summary);
      })
      .catch((error) => console.error("Error fetching summary:", error));
  };

  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>
          Edit <code>src/App.js</code> and save to reload.
        </p>
        <a
          className="App-link"
          href="https://reactjs.org"
          target="_blank"
          rel="noopener noreferrer"
        >
          Learn React
        </a>
        <button onClick={summarize}>Summarize</button>
        <p>{summary}</p>
      </header>
    </div>
  );
}

export default App;
