import React from 'react';
import './styles.css';
import 'bootstrap/dist/css/bootstrap.min.css';
import { Button, Form, FormGroup, Label, Input, FormText, Col, Row } from 'reactstrap';


export default class SearchBar extends React.Component {
    constructor() {
        super()
    }
    render() {
        return (
            <div className='contenedor-form'>
                <Form>
                    <div className='contenedor-titulo'>
                        <h2>Registro de campos</h2>
                    </div>
                    <FormGroup row>
                        <Col sm={3}>
                            <Label for="exampleEmail">Nombres</Label>
                            <Col sm={12}>
                                <Input type="email" name="email" id="exampleEmail" placeholder="Nombres" />
                            </Col>
                        </Col>
                        <Col sm={3}>
                            <Label for="exampleEmail">Apellidos</Label>
                            <Col sm={12}>
                                <Input type="email" name="email" id="exampleEmail" placeholder="Apellidos" />
                            </Col>
                        </Col>
                        <Col sm={3}>
                            <Label for="exampleEmail">Telefono</Label>
                            <Col sm={12}>
                                <Input type="email" name="email" id="exampleEmail" placeholder="Telefono" />
                            </Col>
                        </Col>
                        <Col sm={3}>
                            <Label for="exampleEmail">Cédula</Label>
                            <Col sm={12}>
                                <Input type="number" name="email" id="exampleEmail" placeholder="Cédula" />
                            </Col>
                        </Col>
                    </FormGroup>
                    <FormGroup row>
                        <Col sm={3}>
                            <Label for="exampleEmail">Dirección</Label>
                            <Col sm={12}>
                                <Input type="textarea" name="email" id="exampleEmail" placeholder="Dirección" />
                            </Col>
                        </Col>
                        <Col sm={3}>
                            <Label for="exampleEmail">Correo Electrónico</Label>
                            <Col sm={12}>
                                <Input type="email" name="email" id="exampleEmail" placeholder="Correo Electrónico" />
                            </Col>
                        </Col>
                        <Col sm={3}>
                            <Label for="exampleEmail">Fecha de nacimiento</Label>
                            <Col sm={12}>
                                <Input type="date" name="email" id="exampleEmail" placeholder="Correo Electrónico" />
                            </Col>
                        </Col>
                        <Col sm={3}>
                            <Label for="exampleSelect">Sexo</Label>
                            <Col sm={12}>
                                <Input type="select" name="select" id="exampleSelect">
                                    <option selected>Masculino</option>
                                    <option>Femenino</option>
                                </Input>
                            </Col>
                        </Col>
                    </FormGroup>
                    <FormGroup row>
                        <Col sm={3}>
                            <Label for="exampleEmail">Score</Label>
                            <Col sm={12}>
                                <Input type="email" name="email" id="exampleEmail" placeholder="Score" />
                            </Col>
                        </Col>
                        <Col sm={3}>
                            <Label for="exampleEmail">Estado de operación</Label>
                            <Col sm={12}>
                                <Input type="email" name="email" id="exampleEmail" placeholder="Estado de operación" />
                            </Col>
                        </Col>
                        <Col sm={3}>
                            <Label for="exampleEmail">Estado del Cliente</Label>
                            <Col sm={12}>
                                <Input type="email" name="email" id="exampleEmail" placeholder="Estado del Cliente" />
                            </Col>
                        </Col>
                        <Col sm={3}>
                            <Label for="exampleEmail">Campo extra</Label>
                            <Col sm={12}>
                                <Input type="email" name="email" id="exampleEmail" placeholder="Campo extra" />
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