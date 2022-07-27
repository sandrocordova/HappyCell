import React, { useEffect, useState } from 'react';
import './App.css';
import NavBarHeader from './components/nav-menu/nav-header.component';
import Navbar from './components/navbar-menu';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
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
import Navopciones from './components/navopciones/navopciones'
=======
import *as menuServer from './menuServer'
>>>>>>> f184da835c9aa1ffc2a4bac88446703c5765d281

function App() {

    return (
        <>
            <Navopciones></Navopciones>
            <Router>
                <Navbar />
                <Routes>
                    <Route path='/Administracion' component={Admin} />
                    <Route path='/Politicas' component={Polit} />
                    <Route path='/Pagos' component={Paymen} />
                    <Route path='/ProcesosECRE' component={Process} />
                    <Route path='/DocumentosC' component={Documents} />
                    <Route path='/FabricaDCRE' component={Fabrica} />
                    <Route path='/MotorMensajeria' component={Messages} />
                    <Route path='/Consultas' component={Consultas} />
                    <Route path='/ProcesosMA' component={Massive} />
                    <Route path='/Soporte' component={Support} />
                </Routes>
            </Router>
        </>

    );
}

export default App;