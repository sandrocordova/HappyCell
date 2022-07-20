import React from 'react';
import './App.css';
import Navbar from './components/navbar-menu';
import { BrowserRouter as Router, Switch, Route } from 'react-router-dom';
import Admin from './pages/admin';
import Documents from './pages/documents';
import Fabrica from './pages/fabrica';
import Massive from './pages/massive';
import Messages from './pages/messages';
import Paymen from './pages/paymen';
import Polit from './pages/polit';
import Process from './pages/process';
import Support from './pages/support';
import Processm from './pages/processm';
import Consultas from './pages/consultas';

function App() {
    return (
        <Router>
            <Navbar />
            <switch>
                <Route path='/Administracion' component={Admin} />
                <Route path='/Politicas' component={Polit} />
                <Route path='/Pagos' component={Paymen} />
                <Route path='/ProcesosECRE' component={Process} />
                <Route path='/DocumentosC' component={Documents} />
                <Route path='/FabricaDCRE' component={Fabrica} />
                <Route path='/MotorMensajeria' component={Messages} />
                <Route path='/Consultas' component={Consultas} />
                <Route path='/ProcesosMA' component={Processm} />
                <Route path='/Soporte' component={Support} />
            </switch>
        </Router>
    );
}

export default App;
