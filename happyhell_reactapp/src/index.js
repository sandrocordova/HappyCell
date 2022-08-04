import React from 'react'; // importamos react
import ReactDOM from 'react-dom/client'; // nos permite renderizar en el DOM
import './index.css';
import App from './App';
import { BrowserRouter, Route, Routes } from 'react-router-dom'
import Clientespage from './pages/Clientes.page';
import Mantenimientopage from './pages/Mantenimiento.page';
import Clientesvistapage from './pages/Clientesvista.page';

import Mensajeriapage from './pages/Mensajeria.page';



const root = ReactDOM.createRoot(document.getElementById('root'));


root.render(
    <React.StrictMode>

        <BrowserRouter>
            <Routes>
                <Route path="/" element={<App />} />
                <Route path="clientes" element={<Clientespage />} />
                <Route path="clientes/mantenimiento" element={<Mantenimientopage />} />
                <Route path="clientes/vistaclientes" element={<Clientesvistapage />} />

                <Route path="mensajeria" element={<Mensajeriapage />} />



            </Routes>
        </BrowserRouter>
    </React.StrictMode>
);
