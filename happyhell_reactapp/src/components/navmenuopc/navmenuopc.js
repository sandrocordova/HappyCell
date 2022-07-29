import React, { useEffect, useState } from 'react';
import './styles.css';
import { Link } from "react-router-dom";
import { Dropdown, DropdownItem, DropdownMenu, DropdownToggle } from 'reactstrap'
import {
    Bars, NavMenu,
    Nav,
    NavLink,
} from './../../components/navbar-menu/navbar-menu.component';
import { text } from '@fortawesome/fontawesome-svg-core';
const Navmenopc = () => {
    const [opcs, setOpcs] = useState([]);
    useEffect(() => {
        obtainData()
    }, []);
    const obtainData = async () => {

        const data = await fetch('http://192.168.88.103:8080/api/usernavdos');
        const opc = await data.json()

        setOpcs(opc)

    }

  

    const validacion = Object.values(opcs.map(item => (item.opme_descripcion)))
    const validacion2 = [...new Set(validacion)]
    console.log(validacion2)


    return (
<<<<<<< HEAD
        <div>
    
        <nav class='navegacion'>
            <ul className="menu">
                <li>
                    <a href='#'>
                        <b >{'<'}
                        </b>
                    </a>
                </li>
                {
                opcs.map(item => (
                <li>
                    <a href='#'> 
                            {item.opme_descripcion}

                    </a>
                    <ul class="submenu">
                        {

                            validacion2.map(item => (
                                <li>

                                    <a href='#'>
                                        {item}

                                    </a>

                                    <ul class="submenu">




                                        {
                                            opcs.map(item => (
                                                <li>
                                                    <a href='#'>
                                                        {item.vent_descripcion}
                                                    </a>
                                                </li>
                                            ))
                                        }



                                    </ul>
                                </li>
                            ))


                        }


                    </ul>
<<<<<<< HEAD
                </li>
                ))
                }
                <li>
                    <a href='#'>
                        <b >{'>'}
                        </b>
                    </a>
                </li>
            </ul>
        </nav>
        </div>

=======

                </nav>
        
>>>>>>> a21adb55950794a79a6e3109c3b7fb5a1490b3d4
    )

};

export default Navmenopc;