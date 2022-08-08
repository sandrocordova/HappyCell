import React from 'react';
import Clientes from '../components/clientes/clientes.component';
import Clientesvista_clientes from '../components/clientes/clientes.vista_clientes';
import Navmenopc from '../components/navmenuopc/navmenuopc';
import Navopciones from '../components/navopciones/navopciones';


import ForMensajeriaPlantillas from '../components/mensajeria/mensajeria-plantillas/mensajeria.main'
import ForArrastrar from '../components/mensajeria/mensajeria-plantillas/mensajeria.arrastrar'

function Clientespage() {
    return (
        <div>
            <Navopciones></Navopciones>
            <Navmenopc></Navmenopc>
            <ForMensajeriaPlantillas></ForMensajeriaPlantillas>


        </div>
    );
}
export default Clientespage;