import React, { useEffect, useState } from 'react';
import './styles.css';
import 'bootstrap/dist/css/bootstrap.min.css';
import { Button, Form, Table, Label, Input, FormText, Col, Row, InputGroup, InputGroupAddon, InputGroupText, Container } from 'reactstrap';


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
            <Row>
                <Col sm={9}>
                    <Label for="exampleEmail" hidden>Buscar Plantilla</Label>
                    <Col sm={12}>
                        <div className="search">
                        <Input
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
                <Col sm={3}>
                    <Col sm={12}>
                    <Button color='primary'>Buscar</Button>{' '}
                    </Col>
                </Col>
            </Row>


            <Table border>
                <thead>
                    <tr>
                        <th>Nombre plantilla</th>
                        <th>Tipo</th>
                        <th>Fecha</th>
                    </tr>
                </thead>
                <tbody>
                    {
                        plantillas.map(item => (
                            <tr>
                                <td>{item.vent_descripcion}</td>
                                <td>{item.tipe_descripcion}</td>
                                <td>{item.vent_descripcion}</td>
                            </tr>
                        ))
                    }
                </tbody>
            </Table>



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