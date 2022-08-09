import React from 'react';
import Clientesvista_clientes from '../components/clientes/clientes.vista_clientes';
import Navmenopc from '../components/navmenuopc/navmenuopc';
import Navopciones from '../components/navopciones/navopciones';

function Clientesvistapage() {
    return (
        <div>
            <Navopciones></Navopciones>
            <Navmenopc></Navmenopc>
            <Clientesvista_clientes></Clientesvista_clientes>


        </div>
    );
}
export default Clientesvistapage;