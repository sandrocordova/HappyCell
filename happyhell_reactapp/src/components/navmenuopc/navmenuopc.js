import React, { useEffect, useState } from 'react';
<<<<<<< HEAD
import { Link } from "react-router-dom";
import 'bootstrap/dist/css/bootstrap.min.css'
import { Dropdown, DropdownItem, DropdownMenu, DropdownToggle } from 'reactstrap'
import {
    Bars, NavMenu,
    Nav,
    NavLink,
} from './../../components/navbar-menu/navbar-menu.component';
=======
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { faUserGear } from '@fortawesome/free-solid-svg-icons';
import ScrollMenu from "react-horizontal-scrolling-menu";
import "./styles.css";
import PropTypes from "prop-types";
import { MdChevronLeft, MdChevronRight } from 'react-icons/md'
import ItemsCarousel from 'react-items-carousel';
import {
    Bars, NavMenu,
    Nav,
} from './../../components/navbar-menu/navbar-menu.component';

>>>>>>> 0d030cad3c7e0041a9e7faea721744727c997ee9
const Navmenopc = () => {
    const [opcs, setOpcs] = useState([]);
    useEffect(() => {
        obtainData()
    }, []);
    const obtainData = async () => {

        const data = await fetch('http://192.168.88.103:8080/api/usernavdos');
        const opc = await data.json()
<<<<<<< HEAD

=======
        console.log(opc)
>>>>>>> 0d030cad3c7e0041a9e7faea721744727c997ee9
        setOpcs(opc)

    }

<<<<<<< HEAD
    const [dropdown, setDropdown] = useState(false);
    const abrirCerrarDropdown = () => {
        setDropdown(!dropdown);
    }

    return (
        <Nav>
            <nav>
                <ul className="menus">






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
=======
    const [activeItemIndex, setActiveItemIndex] = useState(0);
    const chevronWidth = 40;
    return (

        <div className='menuopcs'>
            <Nav>
                <Bars />
                <NavMenu>
                    <ItemsCarousel
                        requestToChangeActive={setActiveItemIndex}
                        activeItemIndex={activeItemIndex}
                        numberOfCards={2}
                        gutter={20}
                        leftChevron={<button>{'<'}</button>}
                        rightChevron={<button>{'>'}</button>}
                        outsideChevron
                        chevronWidth={chevronWidth}>
                        {
                            opcs.map(item => (
                                <div className="menu-item">
                                    {item.opme_descripcion}
                                </div>

                            ))
                        }
                    </ItemsCarousel>

                </NavMenu>
            </Nav>

        </div>



>>>>>>> 0d030cad3c7e0041a9e7faea721744727c997ee9
    )

};

export default Navmenopc;