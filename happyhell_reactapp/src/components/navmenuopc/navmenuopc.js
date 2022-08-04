import React, { useEffect, useState } from 'react';
import './styles.css';
import 'bootstrap/dist/css/bootstrap.min.css';
import { Link } from 'react-router-dom'
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

    return (


        <nav class='navegacion'>

            <ul className="menu">

                <li>

                    <Link to ="/clientes">
                        
                        Clientes
                    </Link>
                    
                    

                    <ul className="submenu">

                        < li >

                            <Link to="/clientes/mantenimiento" >
                                Mantenimiento
                            </Link>
                          

                        </li>

                    </ul>
                </li>
                <li>

                    <Link to="/mensajeria">
                        Mensajeria

                    </Link>


                    <ul className="submenu">

                        < li >

                            <Link to="parametros" >
                                Parametros
                            </Link>
                            <Link to="ejecucion" >
                                Ejecucion
                            </Link>

                        </li>

                    </ul>
                </li>
            </ul>

        </nav >

    )
};
export default Navmenopc;