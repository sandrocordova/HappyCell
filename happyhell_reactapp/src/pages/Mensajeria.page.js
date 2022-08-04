import React from 'react';
import Navmenopc from '../components/navmenuopc/navmenuopc';
import Navopciones from '../components/navopciones/navopciones';
import MenuMensajeria from '../components/mensajeria/mensajeria.component';

function Mensajeriapage() {
    return (
        <div>
            <Navopciones></Navopciones>
            <Navmenopc></Navmenopc>
            <MenuMensajeria></MenuMensajeria>

        </div>
    );
}
export default Mensajeriapage;