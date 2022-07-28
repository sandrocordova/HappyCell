import React, { useEffect, useState } from 'react';
import './App.css';
import NavBarHeader from './components/nav-menu/nav-header.component';
import Navbar from './components/navbar-menu';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';

import Navopciones from './components/navopciones/navopciones'
import Navmenopc from './components/navmenuopc/navmenuopc'

function App() {

    return (
        <>
            <Navopciones></Navopciones>
            <Navmenopc></Navmenopc>
        </>

    );
}

export default App;