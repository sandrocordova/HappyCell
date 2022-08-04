import React from 'react';
import Clientes from '../components/clientes/clientes.component';
import Clientesvista_clientes from '../components/clientes/clientes.vista_clientes';
import Navmenopc from '../components/navmenuopc/navmenuopc';
import Navopciones from '../components/navopciones/navopciones';

import ForMensajeriaCampos from '../components/mensajeria/mensajeria-campos/mensajeria.main'

function Clientespage() {
    return (
        <div>
            <Navopciones></Navopciones>
            <Navmenopc></Navmenopc>
            <ForMensajeriaCampos></ForMensajeriaCampos>


        </div>
    );
}
export default Clientespage;