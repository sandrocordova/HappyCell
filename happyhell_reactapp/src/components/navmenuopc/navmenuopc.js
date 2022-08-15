import React, { useEffect, useState, useRef } from 'react';
import './styles.css';
import { Link } from 'react-router-dom'
import { Button, Table, Form, FormGroup, Label, Input, FormText, Col, Row, InputGroup, InputGroupAddon, InputGroupText } from 'reactstrap';


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
    const ref = useRef(null);
    const scroll = (scrollOffset) => {
        ref.current.scrollLeft += scrollOffset;
    };
    return (
        <div class='navegacion'>
            <ul className="containerul">
                <li>
                    <Link to="/clientes">
                        <img className="imgIcon" src="https://cdn-icons-png.flaticon.com/128/3126/3126649.png" alt="Clientes" />
                        <label>
                            Clientes
                        </label>
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
                        <img className="imgIcon" src="https://cdn-icons-png.flaticon.com/128/134/134808.png" alt="Clientes" />
                        <label>
                            Mensajeria
                        </label>

                    </Link>

<<<<<<< HEAD

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

        </div >
=======
                    <h1>Hola Mundo</h1>
>>>>>>> 6fcb387e4b55b71d6910b727309e2180412b30de


    )
};
export default Navmenopc;