import './../../styled-components/nav-bar/nav-bar.css';
import { responseMessages } from '../..//utils/enums/tecnofin-service.enum';
import { useState, useEffect } from 'react';
import { User } from '../../models/User/user-data.model';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { faUserGear } from '@fortawesome/free-solid-svg-icons';
import TecnofinApi from '../../services/tecnofin.service';

const NavBarHeader = () => {
   

    return (
        <>
        <div className='nav-header'>
            <div className='logo'>
                <img className='image' src={user.EMPR_IMAGEN} alt='Happy cel logo'/>
            </div>
            <div className='title'>
                <span>SISTEMA DE ADMINISTRACIÓN DE CARTERA</span>
            </div>
            <div className='location'>
                <span>{user.ZONA_DESCRIPCION} </span>
                <span>{user.AGEN_DESCRIPCION} - {user.CETC_CODIGO_DESCRIPCION}</span>
            </div>
            <div className='userSession'>
                <div className='userData'>
                    <span>{user.USUA_NOMBRE} </span>
                    <span className='userRole'>{user.TIPE_DESCRIPCION}</span>
                </div>
                <br/>
                <div className='userIcon'>
                    <FontAwesomeIcon icon={faUserGear} />
                </div>
            </div>
        </div>
        </>
    )
}

export default NavBarHeader;