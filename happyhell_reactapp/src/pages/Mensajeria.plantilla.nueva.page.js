import React from 'react';
import Navmenopc from '../components/navmenuopc/navmenuopc';
import Navopciones from '../components/navopciones/navopciones';
import ForMensajeriaNueva from '../components/mensajeria/mensajeria-plantillas/mensajeria.main.nueva'
function Mensajeriapage() {
    return (
        <div>
            <Navopciones></Navopciones>
            <Navmenopc></Navmenopc>
            <ForMensajeriaNueva></ForMensajeriaNueva>

        </div>
    );
}
export default Mensajeriapage;