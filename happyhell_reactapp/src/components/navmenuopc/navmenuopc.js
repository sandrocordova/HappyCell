import React, { useEffect, useState } from 'react';
import './styles.css';
import 'bootstrap/dist/css/bootstrap.min.css';
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

    return (

        <body className="body">

            <nav class='navegacion'>

                <ul className="menu">
                    <Link to="/">
                        <Button className="buttonIconOpciones" title="Clientes" size="large" variant="contained" alt="Clientes">
                            <img className="imgIcon" src="https://cdn-icons.flaticon.com/png/128/3936/premium/3936751.png?token=exp=1659593203~hmac=4b7dd15d13b93caf41c2566c56231078" alt="Clientes" align="left"/>

                        </Button>
                    </Link>
                    <li>

                        <Link to="/clientes">
                            <img className="imgIcon" src="https://cdn-icons-png.flaticon.com/128/3126/3126649.png" alt="Clientes"/>
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
        </body>

    )
};
export default Navmenopc;