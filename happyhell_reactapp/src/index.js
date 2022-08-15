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
import MensajeriaPlantillasNuevaPage from './pages/Mensajeria.plantilla.nueva.page';
import Clientesnaturalespage from './pages/Clientes.naturales.page';
import Clientesjuridicospage from './pages/Clientes.juridicos';
import Direccionesvista2page from './pages/Direccionesvista2.page';
import Direccionestelefonopage from './pages/Direccionestelefono.page';
import Direccionestelefono2page from './pages/Direccionestelefono2.page';
import PruebasPage from './pages/Mensajeria.pruebas';



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
                <Route path="mensajeria/pruebas" element={<PruebasPage />} />
                <Route path="mensajeria/plantillas" element={<MensajeriaPlantillasPage />} />
                <Route path="mensajeria/plantillas/nueva" element={<MensajeriaPlantillasNuevaPage />} />
                <Route path="clientes/vistaclientes/clientesnaturales" element={<Clientesnaturalespage />} />
                <Route path="clientes/vistaclientes/clientesjuridicos" element={<Clientesjuridicospage />} />
                <Route path="clientes/direcciones/direcciones2" element={<Direccionesvista2page />} />
                <Route path="clientes/direcciones/direcciones2/telefono" element={<Direccionestelefonopage />} />
                <Route path="clientes/direcciones/direcciones2/telefono/telefono2" element={<Direccionestelefono2page />} />

            </Routes>
        </BrowserRouter>
    </React.StrictMode>
);
