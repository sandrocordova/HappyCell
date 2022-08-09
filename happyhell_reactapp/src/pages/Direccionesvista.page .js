import React from 'react';
import Clientesvista_clientes from '../components/clientes/clientes.vista_clientes';
import Direccionesvista_direcciones from '../components/Direcciones/direcciones.vista_direcciones';
import Navmenopc from '../components/navmenuopc/navmenuopc';
import Navopciones from '../components/navopciones/navopciones';

function Direccionesvistapage() {
    return (
        <div>
            <Navopciones></Navopciones>
            <Navmenopc></Navmenopc>
            <Direccionesvista_direcciones></Direccionesvista_direcciones>

        </div>
    );
}
export default Direccionesvistapage;