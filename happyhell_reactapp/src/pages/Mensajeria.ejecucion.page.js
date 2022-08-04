import React from 'react';
import Clientes from '../components/clientes/clientes.component';
import Clientesvista_clientes from '../components/clientes/clientes.vista_clientes';
import Navmenopc from '../components/navmenuopc/navmenuopc';
import Navopciones from '../components/navopciones/navopciones';
import ForMensajeriEjecucion from '../components/mensajeria/mensajeria-ejecucion/mensajeria.main'

function MensajeriaEjecucionPage() {
    return (
        <div>
            <Navopciones></Navopciones>
            <Navmenopc></Navmenopc>
            <ForMensajeriEjecucion></ForMensajeriEjecucion>


        </div>
    );
}
export default MensajeriaEjecucionPage;