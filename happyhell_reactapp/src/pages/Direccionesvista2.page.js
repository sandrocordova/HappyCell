import React from 'react';
import Direccionesvista2_direcciones from '../components/Direcciones/direcciones.vista2_direcciones';
import Navmenopc from '../components/navmenuopc/navmenuopc';
import Navopciones from '../components/navopciones/navopciones';

function Direccionesvista2page() {
    return (
        <div>
            <Navopciones></Navopciones>
            <Navmenopc></Navmenopc>
            <Direccionesvista2_direcciones></Direccionesvista2_direcciones>

        </div>
    );
}
export default Direccionesvista2page;