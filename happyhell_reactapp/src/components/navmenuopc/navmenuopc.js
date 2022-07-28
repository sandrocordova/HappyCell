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
                    <li>
                        <a href='#'> Menú </a>
                        <ul class="submenu">
                            <li>
                                <a href='#'>
                                    {
                                    opcs.map(item => (
                                        item.opme_descripcion
                                        ))
                                    }
                                </a>
                            </li>
                            <li>
                                <a href='#'>
                                    {
                                    opcs.map(item => (
                                        item.vent_descripcion
                                    ))
                                    }
                                </a>

                            </li>
                        </ul>
                    </li>
                    <li>
                        <a href='#'> Menú 2 </a>
                            <ul class="submenu">
                                <li>
                                    <a href='#'>
                                        sub menu 1
                                    </a>
                                </li>
                                <li>
                                    <a href='#'>
                                        sub menu 2
                                    </a>

                                </li>
                            </ul>
                    </li>
                    <li>
                        <a href='#'> Menú 3 </a>
                    </li>
                </ul>
            </nav>
    )

};

export default Navmenopc;