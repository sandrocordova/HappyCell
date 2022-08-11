import React from 'react';
import Clientesvista_clientes from '../components/clientes/clientes.vista_clientes';
import Direccionesvista_direcciones from '../components/Direcciones/direcciones.vista_direcciones';
import Direccionestelefono2 from '../components/Direcciones/direccionestelefono2';
import Navmenopc from '../components/navmenuopc/navmenuopc';
import Navopciones from '../components/navopciones/navopciones';

function Direccionestelefono2page() {
    return (
        <div>
            <Navopciones></Navopciones>
            <Navmenopc></Navmenopc>
            <Direccionestelefono2></Direccionestelefono2>

        </div>
    );
}
export default Direccionestelefono2page;