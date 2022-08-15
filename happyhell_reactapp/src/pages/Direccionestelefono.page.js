import React from 'react';
import Clientesvista_clientes from '../components/clientes/clientes.vista_clientes';
import Direccionesvista_direcciones from '../components/Direcciones/direcciones.vista_direcciones';
import Direccionestelefono from '../components/Direcciones/direccionestelefono';
import Navmenopc from '../components/navmenuopc/navmenuopc';
import Navopciones from '../components/navopciones/navopciones';

function Direccionestelefonopage() {
    return (
        <div>
            <Navopciones></Navopciones>
            <Navmenopc></Navmenopc>
            <Direccionestelefono></Direccionestelefono>

        </div>
    );
}
export default Direccionestelefonopage;