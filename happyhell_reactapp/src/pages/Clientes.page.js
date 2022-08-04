import React from 'react';
import Clientes from '../components/clientes/clientes.component';
import Clientesvista_clientes from '../components/clientes/clientes.vista_clientes';
import Navmenopc from '../components/navmenuopc/navmenuopc';
import Navopciones from '../components/navopciones/navopciones';

function Clientespage() {
    return (
        <div>
            <Navopciones></Navopciones>
            <Navmenopc></Navmenopc>
            <Clientes></Clientes>


        </div>
    );
}
export default Clientespage;