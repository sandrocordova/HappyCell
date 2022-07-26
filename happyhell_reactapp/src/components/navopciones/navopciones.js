import React, { useEffect, useState } from 'react';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { faUserGear } from '@fortawesome/free-solid-svg-icons';
const Navopciones = () => {
    const [menu, setMenu] = useState([]);
    useEffect(() => {
        obtainData()
    }, []);
    const obtainData = async () => {
        const data = await fetch('http://192.168.88.103:8080/api/usernav');
        const menus = await data.json()
        setMenu(menus)
    }

    return (

        <div className='nav-header'>
            {
                menu.map(item => (
                    <div className='logo'>
                        <img className='image' src={item.empr_imagen} alt='Happy cel logo' />
                    </div>

                ))
            }
            <div className='titulo'>
                SISTEMA DE ADMINISTRACION DE CARTERA
            </div>
            {
                menu.map(item => (
                    <div className='locacion'>
                        Ciudad: {item.zona_descripcion}
                        <br/>
                        Agencia: {item.agen_descripcion} - {item.cetc_descripcion}
                    </div>

                ))
            }
            {
                menu.map(item => (
                    <div className='userSession'>
                        <FontAwesomeIcon icon={faUserGear} />
                        {item.usua_nombre}
                        <br/>
                        {item.tipe_descripcion}
                    </div>

                ))
            }
           
        </div>

    )

};

export default Navopciones;