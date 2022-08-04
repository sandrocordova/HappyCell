import React from 'react'; // importamos react
import ReactDOM from 'react-dom/client'; // nos permite renderizar en el DOM
import './index.css';
import App from './App';
import { BrowserRouter, Route, Routes } from 'react-router-dom'
import Clientespage from './pages/Clientes.page';
import Mensajeriapage from './pages/Mensajeria.page';
import Mantenimientopage from './pages/Mantenimiento.page';
import Clientesvistapage from './pages/Clientesvista.page';



const root = ReactDOM.createRoot(document.getElementById('root'));


root.render(
    <React.StrictMode>

        <BrowserRouter>
            <Routes>
                <Route path="/" element={<App />} />
                <Route path="clientes" element={<Clientespage />} />
                <Route path="mensajeria" element={<Mensajeriapage />} />
                <Route path="clientes/mantenimiento" element={<Mantenimientopage />} />
                <Route path="clientes/vistaclientes" element={<Clientesvistapage />} />


            </Routes>
        </BrowserRouter>
    </React.StrictMode>
);
