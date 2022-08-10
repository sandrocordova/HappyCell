import React from 'react';
import './styles.css';
import { Button, Form, FormGroup, Label, Input, FormText, Col, Row, InputGroup, InputGroupAddon, InputGroupText } from 'reactstrap';
import { Link } from 'react-router-dom';






export default class SearchBar extends React.Component {
    constructor() {
        super()
    }

    render() {
        return (
            <div>
                <div className='contenedor-br-4'>
                    <div className='contenedor-br-int'>
                        <Row>
                            <Col sm={2}></Col>
                            <Col sm={1}>
                                <Label size='sm' for="laberNombrePLantilla">Código</Label>
                                <Input size="sm" type="email" name="laberNombrePLantilla" id="exampleEmail" placeholder="1-002" disabled />
                            </Col>
                            <Col sm={1}>
                                <Label size='sm' for="laberNombrePLantilla">Tipo</Label>
                                <Input size="sm" type="email" name="laberNombrePLantilla" id="exampleEmail" placeholder="Cobros" disabled />
                            </Col>
                            <Col sm={2}>
                                <Label size='sm' for="laberNombrePLantilla">Nombre Plantilla</Label>
                                <Input size="sm" type="email" name="laberNombrePLantilla" id="exampleEmail" placeholder="Plantilla Cobros" disabled />
                            </Col>
                            <Col sm={2}>
                                <Label size='sm' for="laberNombrePLantilla">Creador</Label>
                                <Input size="sm" type="email" name="laberNombrePLantilla" id="exampleEmail" placeholder="Diana Cartuche" disabled />

                            </Col>
                            <Col sm={2}>
                                <Label size='sm' for="laberNombrePLantilla">Fecha creación</Label>
                                <Input size="sm" type="email" name="laberNombrePLantilla" id="exampleEmail" placeholder="21/07/2021" disabled />
                            </Col>
                            <Col sm={2}></Col>
                        </Row>
                    </div>
                </div>
                <div className="contenedor-tabla">
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
                                    <Input type="number" name="email" id="exampleEmail" placeholder='47891221456614' />
                                </Col>
                            </Col>
                            <Col sm={6}>
                                <Label for="imput1">Modelo de Plantilla</Label>
                                <Col sm={12}>
                                    <Input onDrop={event => this.onDrop(event)}
                                        onDragOver={(event => this.onDragOver(event))}
                                        id="imput1" type="textarea" placeholder='Plantilla desarrollada' rows="7" name="email" />
                                </Col>
                            </Col>
                        </FormGroup>
                        <div className='contenedor-botones'>
                            <Button color='primary'>Guardar</Button>{' '}
                            <Button color="danger">Cancelar</Button>
                        </div>
                        <br></br>
                    </Form>


                </div>
            </div>

        )
    }

};