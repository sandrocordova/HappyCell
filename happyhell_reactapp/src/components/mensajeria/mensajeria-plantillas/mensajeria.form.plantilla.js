import React from 'react';
import './styles.css';
import 'bootstrap/dist/css/bootstrap.min.css';
import { Button, Form, FormGroup, Label, Input, FormText, Col, Row, InputGroup, InputGroupAddon, InputGroupText } from 'reactstrap';


export default class SearchBar extends React.Component {
    constructor() {
        super()
    }
    render() {
        return (
            <div>
                <Form name="datosPlantilla">
                    <div className='contenedor-titulo'>
                        <h2>Datos de Plantilla</h2>
                    </div>
                    <FormGroup row>
                        <Col sm={1}></Col>
                        <Col sm={4}>
                            <Label for="laberNombrePLantilla">Nombre de la plantilla</Label>
                            <Col sm={12}>
                                <Input type="email" name="laberNombrePLantilla" id="exampleEmail" placeholder="Nombre Plantilla" />
                            </Col>
                        </Col>
                        <Col sm={3}>
                            <Label for="exampleEmail">Tipo de plantilla</Label>
                            <Col sm={12}>
                                <Input type="email" name="email" id="exampleEmail" placeholder="Tipo" />
                            </Col>
                        </Col>
                        <Col sm={3}>
                            <Label for="exampleEmail">Fecha de creación</Label>
                            <Col sm={12}>
                                <Input type="date" name="email" id="exampleEmail" />
                            </Col>
                        </Col>
                    </FormGroup>
                    <FormGroup row>
                        <Col sm={1}></Col>
                        <Col sm={4}>
                            <Label for="exampleEmail">IMEI</Label>
                            <Col sm={12}>
                                <Input type="number" name="email" id="exampleEmail" />
                            </Col><br></br>
                            <Button color='secondary'>Probar Plantilla</Button>{' '}
                        </Col>
                        <Col sm={6}>
                            <Label for="exampleEmail">Modelo de Plantilla</Label>
                            <Col sm={12}>
                                <Input type="textarea" rows="10" name="email" id="exampleEmail" />
                            </Col>
                        </Col>
                    </FormGroup>
                    <div className='contenedor-botones'>
                        <Button color='primary'>Guardar</Button>{' '}
                        <Button color="danger">Cancelar</Button>

                    </div>

                </Form>


            </div>

        )
    }

};