import React, { useEffect, useState } from 'react';
import './styles.css';
import { Button, Form, Table, Label, Input, Col, Row, InputGroup, InputGroupAddon, InputGroupText, Container } from 'reactstrap';
import { Link } from 'react-router-dom';

function CargarJson() {
    const [opcs, setOpcs] = useState([]);

    const [plantillas, setPlantillas] = useState([]);
    const [tablaUsuarios, setTablaUsuarios] = useState([]);
    const [busqueda, setBusqueda] = useState("");

    const obtainData = async () => {

        const data = await fetch('http://192.168.88.103:8080/api/usernavdos');
        const opc = await data.json()
        setTablaUsuarios(opc);
        setPlantillas(opc)

    }

    const handleChange = e => {
        console.log("BUSQUEDA:  " + e.target.value)
        setBusqueda(e.target.value);
        filtrar(e.target.value);
    }

    const filtrar = (terminoBusqueda) => {
        var resultadosBusqueda = tablaUsuarios.filter((elemento) => {
            if (elemento.vent_descripcion.toString().toLowerCase().includes(terminoBusqueda.toLowerCase())
            ) {
                return elemento;
            }
        });
        setPlantillas(resultadosBusqueda);
    }

    useEffect(() => {
        obtainData();
    }, [])




    const validacion = Object.values(opcs.map(item => (item.opme_descripcion)))

    return (

        <div>
            <div className='contenedor-br-4'>
            <div className='contenedor-br-4-int'>
                <Row>
                    <Col sm={4}></Col>
                    <Col sm={3}>
                        <Label for="exampleEmail" hidden>Buscar Plantilla</Label>
                        <Col sm={12}>
                            <div className="search">
                                <Input size="sm"
                                    id="outlined-basic"
                                    onChange={handleChange}
                                    variant="outlined"
                                    value={busqueda}
                                    fullWidth
                                    label="Search"
                                    placeholder="Buscar Plantilla"
                                />
                            </div>
                        </Col>

                    </Col>
                    <Col sm={1}>
                        <Col sm={12}>
                            <Button size='sm' color='primary'>Buscar</Button>{' '}
                        </Col>
                    </Col>
                    <Col sm={2}></Col>
                    <Col sm={2}>
                    </Col>
                </Row>
            </div>
            </div>
            <div className="contenedor-tabla">
                <div className='contenedor-btn-crear'>
                    <Link to="nueva">
                        <a>Crear Plantilla</a>
                    </Link>
                </div>

                <Table hover bordered>
                    <thead>
                        <tr>
                            <th>Check</th>
                            <th>Nombre plantilla</th>
                            <th>Descripción</th>
                            <th>Tipo</th>
                            <th>Fecha</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr>
                            <td>
                                <Input type="checkbox" name="checkSelect" id="opc" />
                            </td>
                            <td>Plantilla cobrar</td>
                            <td>Plantilla para enviar mensajes a los clientes por cobrar</td>
                            <td>Cobros</td>
                            <td>21/07/2021</td>
                        </tr>
                        <tr>
                            <td>
                                <Input type="checkbox" name="checkSelect" id="opc" />
                            </td>
                            <td>Plantilla pago realizado</td>
                            <td>Plantilla para notificar a los clientes que los pagos han sido realizados</td>
                            <td>Pagos</td>
                            <td>21/07/2021</td>
                        </tr>
                        <tr>
                            <td>
                                <Input type="checkbox" name="checkSelect" id="opc" />
                            </td>
                            <td>Plantilla promociones</td>
                            <td>Plantilla para enviar promociones a los clientes</td>
                            <td>Cobros</td>
                            <td>21/07/2021</td>
                        </tr>
                        <tr>
                            <td>
                                <Input type="checkbox" name="checkSelect" id="opc" />
                            </td>
                            <td>Plantilla retrasos</td>
                            <td>Plantilla para notificar de retrasos a los clientes</td>
                            <td>Cobros</td>
                            <td>21/07/2021</td>
                        </tr>
                        {
                            plantillas.map(item => (
                                <tr>
                                    <td>
                                        <Input type="checkbox" name="checkSelect" id="opc" />
                                    </td>
                                    <td>{item.vent_descripcion}</td>
                                    <td>{item.tipe_descripcion}</td>
                                    <td>{item.vent_descripcion}</td>
                                    <td>21/07/2021</td>
                                </tr>
                            ))
                        }
                    </tbody>
                </Table>


            </div>
        </div>


    )
}



export default class SearchBar extends React.Component {
    constructor() {
        super()
    }
    render() {
        return (

            <div><CargarJson /></div>


        )
    }

};