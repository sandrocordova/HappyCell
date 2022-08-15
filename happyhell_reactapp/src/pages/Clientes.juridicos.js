import React from 'react';
import Clientes from '../components/clientes/clientes.component';
import Clientesjuridicos from '../components/clientes/clientes.juridicos';
import Clientesvista_clientes from '../components/clientes/clientes.vista_clientes';
import Navmenopc from '../components/navmenuopc/navmenuopc';
import Navopciones from '../components/navopciones/navopciones';

function Clientesjuridicospage() {
    return (
        <div>
            <Navopciones></Navopciones>
            <Navmenopc></Navmenopc>
            <Clientesjuridicos></Clientesjuridicos>


        </div>
    );
}
export default Clientesjuridicospage;