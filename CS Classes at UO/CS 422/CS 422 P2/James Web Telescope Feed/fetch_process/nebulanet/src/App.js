import React, { Component } from 'react';
import NavBar from './components/NavBar';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import './App.css'
import Home from './components/pages/Home.js'
import About from './components/pages/About.js'
import Sources from './components/pages/Sources.js'



function App() {
  return (
    <>
    <Router>
      <NavBar/>
      <Routes>
        <Route path='/' exact Component={Home}/>
        <Route path='/about' exact Component={About}/>
        <Route path='/sources' exact Component={Sources}/>
      </Routes>
    </Router>
    </>
  );
}

export default App;
