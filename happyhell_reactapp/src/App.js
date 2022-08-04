import React, { useEffect, useState } from 'react';
import './App.css';
import NavBarHeader from './components/nav-menu/nav-header.component';
import Navbar from './components/navbar-menu';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Navopciones from './components/navopciones/navopciones'
import Navmenopc from './components/navmenuopc/navmenuopc'
import Formmain from './components/form-search/FormMain'
import ForMensajeriaCampos from './components/mensajeria/mensajeria-campos/mensajeria.main'
import ForMensajeriEjecucion from './components/mensajeria/mensajeria-ejecucion/mensajeria.main'
import ForMensajeriaPlantillas from './components/mensajeria/mensajeria-plantillas/mensajeria.main'

function App() {

    return (
        <>
            <Navopciones></Navopciones>
            <Navmenopc></Navmenopc>
            
            <ForMensajeriaPlantillas></ForMensajeriaPlantillas>
        </>

    );
}

export default App;