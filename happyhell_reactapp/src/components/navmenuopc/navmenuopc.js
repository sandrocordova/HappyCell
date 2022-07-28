import React, { useEffect, useState } from 'react';
import { Link } from "react-router-dom";
import 'bootstrap/dist/css/bootstrap.min.css'
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
        <Nav>
            <h1>Hola Mundo</h1>
            <nav class='navegacion'>
                <ul className="menu">
                    <li>
                        <a href='#'> Menú </a>
                        <ul className="submenus">
                            <li>
                                <a href='#'>
                                    {
                                    opcs.map(item => (
                                        item.opme_descripcion
                                        ))
                                    }
                                </a>
                                <a href='#'>
                                    {
                                    opcs.map(item => (

                                        <DropdownItem header>
                                            {item.vent_descripcion}
                                        </DropdownItem>
                                    ))
                                    }
                                </a>

                            </li>
                        </ul>
                    </li>
                </ul>
            </nav>
        </Nav>
    )

};

export default Navmenopc;