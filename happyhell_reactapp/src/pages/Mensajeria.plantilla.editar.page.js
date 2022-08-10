import React from 'react';
import Navmenopc from '../components/navmenuopc/navmenuopc';
import Navopciones from '../components/navopciones/navopciones';
import ForMensajeriaEditar from '../components/mensajeria/mensajeria-plantillas/mensajeria.main.editar'
function Mensajeriapage() {
    return (
        <div>
            <Navopciones></Navopciones>
            <Navmenopc></Navmenopc>
            <ForMensajeriaEditar></ForMensajeriaEditar>

        </div>
    );
}
export default Mensajeriapage;