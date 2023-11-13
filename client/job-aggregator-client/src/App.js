import React, { useState, useEffect } from "react";
import axios from "axios";
import "./App.css";
import logo from "./jobhub_logo.png";

function App() {
  const [jobs, setJobs] = useState([]);

  useEffect(() => {
    axios
      .get("http://localhost:5000/jobs") // Adjust the URL as needed
      .then((response) => {
        setJobs(response.data);
      })
      .catch((error) => {
        console.error("There was an error fetching the jobs!", error);
      });
  }, []);

  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="JobHub" />
      </header>
      <main>
        <div className="table-container">
          <table>
            <thead>
              <tr>
                <th>Job Position</th>
                <th>Company</th>
                <th>Apply URL</th>
              </tr>
            </thead>
            <tbody>
              {jobs.map((job, index) => (
                <tr key={index}>
                  <td>{job.title}</td>
                  <td>{job.company}</td>
                  <td>
                    <a
                      href={job.job_url}
                      target="_blank"
                      rel="noopener noreferrer"
                    >
                      Apply
                    </a>
                  </td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      </main>
    </div>
  );
}

export default App;
