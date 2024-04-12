// frontend/src/App.js

import React from 'react';
import './App.css';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import AppLayout from './AppLayout';
import { UserProvider } from './UserContext';
// Import other components you want to route to

function App() {
  return (
    <Router>
      <UserProvider>
        <div className="App">
          <AppLayout></AppLayout>
        </div>
      </UserProvider>
    </Router>
  );
}

export default App;
