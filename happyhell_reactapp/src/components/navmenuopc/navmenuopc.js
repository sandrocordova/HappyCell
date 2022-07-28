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
            <nav>
                <ul className="menus">



                    <h1>Hola Mundo</h1>


                    <Dropdown isOpen={dropdown} toggle={abrirCerrarDropdown} size='sm'>
                        <DropdownToggle caret>
                            {
                                opcs.map(item => (

                                    item.opme_descripcion
                                ))
                            }
                        </DropdownToggle>
                        <DropdownMenu>
                            
                                {
                                opcs.map(item => (
                                        
                                        <DropdownItem header>
                                            {item.vent_descripcion}
                                        </DropdownItem>
                                    ))
                                }
                           

                        </DropdownMenu>
                    </Dropdown>


                </ul>
            </nav>
        </Nav>
    )

};

export default Navmenopc;