import React, { useEffect, useState } from 'react';
import './styles.css';
import { Link } from "react-router-dom";
import { Dropdown, DropdownItem, DropdownMenu, DropdownToggle } from 'reactstrap'
import {
    Bars, NavMenu,
    Nav,
    NavLink,
} from './../../components/navbar-menu/navbar-menu.component';
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

    const [dropdown, setDropdown] = useState(false);
    const abrirCerrarDropdown = () => {
        setDropdown(!dropdown);
    }

    return (
        <nav class='navegacion'>
            <ul className="menu">
                {
                opcs.map(item => (
                <li>
                    <a href='#'> 
                            {item.opme_descripcion}

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
        </nav>
    )

};

export default Navmenopc;