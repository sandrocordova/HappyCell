import React, { useEffect, useState } from 'react';
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

const Navmenopc = () => {
    const [opcs, setOpcs] = useState([]);
    useEffect(() => {
        obtainData()
    }, []);
    const obtainData = async () => {

        const data = await fetch('http://192.168.88.103:8080/api/usernavdos');
        const opc = await data.json()
        console.log(opc)
        setOpcs(opc)

    }

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



    )

};

export default Navmenopc;