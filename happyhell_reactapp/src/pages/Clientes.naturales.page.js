import React from 'react';
import Clientes from '../components/clientes/clientes.component';
import Clientesnaturales from '../components/clientes/clientes.naturales';
import Clientesvista_clientes from '../components/clientes/clientes.vista_clientes';
import Navmenopc from '../components/navmenuopc/navmenuopc';
import Navopciones from '../components/navopciones/navopciones';

function Clientesnaturalespage() {
    return (
        <div>
            <Navopciones></Navopciones>
            <Navmenopc></Navmenopc>
            <Clientesnaturales></Clientesnaturales>

        </div>
    );
}
export default Clientesnaturalespage;