// App.js
import React, { useState, useEffect, Suspense, lazy } from 'react';
import Header from './components/Header';
import Footer from './components/Footer';
import { Routes, Route } from 'react-router-dom';
import './App.css';

// Lazy loaded components
const About = lazy(() => import('./components/About'));
const SavedJobs = lazy(() => import('./components/SavedJobs'));
const JobListings = lazy(() => import('./components/JobListings')); // Assuming you have a JobListings component

function App() {
  const [jobs, setJobs] = useState([]); // State for storing job listings
  const [filters, setFilters] = useState({}); // State for storing filters
  const [selectedJob, setSelectedJob] = useState(null); // State for storing the selected job

  // Function to fetch jobs from an API
  const fetchJobs = async () => {
    // Replace with your API endpoint
    const response = await fetch('your-api-endpoint');
    const data = await response.json();
    setJobs(data); // Update the state with the fetched jobs
  };

  useEffect(() => {
    fetchJobs(); // Fetch jobs when the component mounts
  }, []); // Empty dependency array ensures this only runs once on mount

  // Function to update filters
  const handleFilterChange = (newFilters) => {
    setFilters(newFilters);
    // Here you would probably refetch or filter the jobs based on the new filters
  };

  // Function to select a job
  const handleJobSelect = (job) => {
    setSelectedJob(job); // Update the state to the selected job
  };

  return (
    <div className="App">
      <Header />
      <main className="main-content">
        <Suspense fallback={<div>Loading...</div>}>
          <Routes>
            <Route path="/" element={
              <>
                <JobListings jobs={jobs} onJobSelect={handleJobSelect} filters={filters} />
              </>
            } />
            <Route path="/about" element={<About />} />
            <Route path="/saved-jobs" element={<SavedJobs />} />
            {/* Other routes as needed */}
          </Routes>
        </Suspense>
      </main>
      {selectedJob && (
        // Placeholder for JobDetails component
        <div>Job Details Component</div>
      )}
      <Footer />
    </div>
  );
}

export default App;
