import React from 'react';
import './App.css';
<<<<<<< HEAD
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

function App() {
    return (
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
=======
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

function App() {
    return (
        <>
            <NavBarHeader></NavBarHeader>
            {/*<div class="sizeLetra">
                <div className="table-responsive">
                    <table className="table table-hover">
                        <thead>
                            <tr>
                                <th>Nro. Credito</th>
                                <th>Fecha Concesion</th>
                                <th>Monto Financiado</th>
                                <th>Saldo Adeudado</th>
                                <th>Estado</th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr>
                                <td>1234-00</td>
                                <td>31-12-2021</td>
                                <td>$400</td>
                                <td>$100</td>
                                <td>DESEMBOLSADO</td>
                            </tr>
                            <tr>
                                <td>1567-00</td>
                                <td>31-12-2021</td>
                                <td>$300</td>
                                <td>$100</td>
                                <td>DESEMBOLSADO</td>
                            </tr>
                        </tbody>
                    </table>
                </div>
    </div>*/}
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

>>>>>>> 95b371c66963429b8e1af53e66829053b321fa8c
    );
}

export default App;
