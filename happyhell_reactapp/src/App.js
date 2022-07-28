import React, { useEffect, useState } from 'react';
import './App.css';
import NavBarHeader from './components/nav-menu/nav-header.component';
import Navbar from './components/navbar-menu';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
<<<<<<< HEAD

import Navopciones from './components/navopciones/navopciones'
import Navmenopc from './components/navmenuopc/navmenuopc'
=======
import Admin from './pages/admin';
import Documents from './pages/documents';
import Fabrica from './pages/fabrica';
import Massive from './pages/massive';
import Messages from './pages/messages';
import Paymen from './pages/paymen';
import Polit from './pages/polit';
import Process from './pages/process';
import Support from './pages/support';
import Consultas from './pages/consultas';
<<<<<<< HEAD
import *as menuServer from './menuServer'
>>>>>>> f184da835c9aa1ffc2a4bac88446703c5765d281
=======
<<<<<<< HEAD
import Navopciones from './components/navopciones/navopciones'
>>>>>>> 0d030cad3c7e0041a9e7faea721744727c997ee9

function App() {

    return (
        <>
            <Navopciones></Navopciones>
            <Navmenopc></Navmenopc>
        </>

    );
}

export default App;