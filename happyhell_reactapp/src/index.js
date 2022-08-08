import React from 'react'; // importamos react
import ReactDOM from 'react-dom/client'; // nos permite renderizar en el DOM
import './index.css';
import App from './App';
import { BrowserRouter, Route, Routes } from 'react-router-dom'
import Clientespage from './pages/Clientes.page';
import Mantenimientopage from './pages/Mantenimiento.page';
import Clientesvistapage from './pages/Clientesvista.page';
import Mensajeriapage from './pages/Mensajeria.page';
import Direccionesvistapage from './pages/Direccionesvista.page ';
import MensajeriaEjecucionPage from './pages/Mensajeria.ejecucion.page';
import MensajeriaParametrosPage from './pages/Mensajeria.parametros.page';
import MensajeriaPlantillasPage from './pages/Mensajeria.plantilla.page';



const root = ReactDOM.createRoot(document.getElementById('root'));


root.render(
    <React.StrictMode>

        <BrowserRouter>
            <Routes>
                <Route path="/" element={<App />} />
                <Route path="clientes" element={<Clientespage />} />
                <Route path="clientes/mantenimiento" element={<Mantenimientopage />} />
                <Route path="clientes/vistaclientes" element={<Clientesvistapage />} />
                <Route path="clientes/direcciones" element={<Direccionesvistapage />} />
                <Route path="mensajeria" element={<Mensajeriapage />} />
                <Route path="mensajeria/ejecucion" element={<MensajeriaEjecucionPage />} />
                <Route path="mensajeria/parametros" element={<MensajeriaParametrosPage />} />
                <Route path="mensajeria/plantillas" element={<MensajeriaPlantillasPage />} />



            </Routes>
        </BrowserRouter>
    </React.StrictMode>
);
