import './../../styled-components/nav-bar/nav-bar.css';
import { responseMessages } from '../..//utils/enums/tecnofin-service.enum';
import { useState, useEffect } from 'react';
import { User } from '../../models/User/user-data.model';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { faUserGear } from '@fortawesome/free-solid-svg-icons';
import TecnofinApi from '../../services/tecnofin.service';

const NavBarHeader = () => {
    const [user, setUser] = useState(new User());

    const defaultUser = () => {
        setUser({
            USUA_LOGIN: "edisaa", 
            USUA_NOMBRE: "Edison Saavedraa", 
            EMPR_IMAGEN: "https://i.pinimg.com/originals/29/47/9b/29479ba0435741580ca9f4a467be6207.png",
            TIPE_DESCRIPCION: "Admin",
            ZONA_DESCRIPCION: "Quito, Ecuador",
            AGEN_DESCRIPCION: "0001 cam internacional km 23",
            CETC_CODIGO_DESCRIPCION: "Centro de costos"
        });
    }

    const handleGetUser = async (e) => {
        const response = await TecnofinApi();
        console.log(response);
        setUser({...response});
    };

    useEffect(() => {
      }, []);

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