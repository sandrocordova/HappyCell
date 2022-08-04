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
            <div className='contenedor-form'>
                <Form>
                    <div className='contenedor-titulo'>
                        <h2>Ejecución</h2>
                    </div>
                    <FormGroup row>
                        <Col sm={3}>
                            <Col sm={12}>
                                <legend>Ocurre</legend>
                                <FormGroup check>
                                    <Label check>
                                        <Input type="radio" name="radio1" />{' '}
                                        Diario
                                    </Label>
                                </FormGroup>
                                <FormGroup check>
                                    <Label check>
                                        <Input type="radio" name="radio1" />{' '}
                                        Semanal
                                    </Label>
                                </FormGroup>
                                <FormGroup check disabled>
                                    <Label check>
                                        <Input type="radio" name="radio1" />{' '}
                                        Mensual
                                    </Label>
                                </FormGroup>
                            </Col>
                        </Col>
                        <Col sm={3}>
                            <Col sm={12}>
                                <legend>Frecuencia</legend>
                                <FormGroup check>
                                    <Label check>
                                        <Input type="radio" name="radio1" />{' '}
                                        Una vez
                                    </Label>
                                </FormGroup>
                                <FormGroup check>
                                    <Label check>
                                        <Input type="radio" name="radio1" />{' '}
                                        Cada x horas
                                    </Label>
                                </FormGroup>
                            </Col>
                        </Col>
                        <Col sm={3}>
                            <Label for="exampleEmail">Hora de envío</Label>
                            <Col sm={12}>
                                <Input type='time' />{' '}

                            </Col>
                            <Label for="exampleEmail">Repetir</Label>
                            <Col sm={12}>
                                <InputGroup size='sm'>
                                    <InputGroupText>Cada</InputGroupText>
                                    <Input type='number' />

                                </InputGroup>
                            </Col>
                        </Col>
                        <Col sm={3}>
                            <Label for="exampleEmail">Comienza</Label>
                            <Col sm={12}>
                                <Input type="date" name="email" id="exampleEmail" />
                            </Col>
                            <Label for="exampleEmail">Finaliza</Label>
                            <Col sm={12}>
                                <Input type="date" name="email" id="exampleEmail" />
                            </Col>
                        </Col>
                    </FormGroup>
                    <FormGroup row>
                    </FormGroup>
                    <h2>
                        Criterios de ejecución
                    </h2>
                    <FormGroup row>
                        <Col sm={3}>
                            <Col sm={12}>
                                <legend>Score</legend>
                                <FormGroup check>
                                    <Label check>
                                        <Input type="checkbox" name="checkbox" />{' '}
                                        A
                                    </Label>
                                </FormGroup>
                                <FormGroup check>
                                    <Label check>
                                        <Input type="checkbox" name="checkbox" />{' '}
                                        B
                                    </Label>
                                </FormGroup>
                                <FormGroup check>
                                    <Label check>
                                        <Input type="checkbox" name="checkbox" />{' '}
                                        C
                                    </Label>
                                </FormGroup>
                                <FormGroup check>
                                    <Label check>
                                        <Input type="checkbox" name="checkbox" />{' '}
                                        D
                                    </Label>
                                </FormGroup>
                                <FormGroup check>
                                    <Label check>
                                        <Input type="checkbox" name="checkbox" />{' '}
                                        E
                                    </Label>
                                </FormGroup>
                            </Col>
                        </Col>
                        <Col sm={3}>
                            <Col sm={12}>
                                <legend>Frecuencia</legend>
                                <FormGroup check>
                                    <Label check>
                                        <Input type="checkbox" name="radio1" />{' '}
                                        13
                                    </Label>
                                </FormGroup>
                                <FormGroup check>
                                    <Label check>
                                        <Input type="checkbox" name="radio1" />{' '}
                                        26
                                    </Label>
                                </FormGroup>
                                <FormGroup check>
                                    <Label check>
                                        <Input type="checkbox" name="radio1" />{' '}
                                        33
                                    </Label>
                                </FormGroup>
                            </Col>
                        </Col>
                        <Col sm={3}>
                            <Col sm={12}>
                                <legend>Frecuencia</legend>
                                <FormGroup check>
                                    <Label check>
                                        <Input type="checkbox" name="radio1" />{' '}
                                        Vencida
                                    </Label>
                                </FormGroup>
                                <FormGroup check>
                                    <Label check>
                                        <Input type="checkbox" name="radio1" />{' '}
                                        Al día
                                    </Label>
                                </FormGroup>
                            </Col>
                        </Col>
                        <Col sm={3}>
                            <legend>Fecha de facturación</legend>
                            <Label for="exampleEmail">Fecha desde</Label>
                            <Col sm={12}>
                                <Input type='date' />{' '}

                            </Col>
                            <Label for="exampleEmail">Fecha hasta</Label>
                            <Col sm={12}>
                                <Input type='date' />
                            </Col>
                        </Col>
                    </FormGroup>
                    <FormGroup row>
                        <Col sm={3}>
                            <Col sm={12}>
                                <legend>Estado Civil</legend>
                                <FormGroup check>
                                    <Label check>
                                        <Input type="checkbox" name="checkbox" />{' '}
                                        Soltero
                                    </Label>
                                </FormGroup>
                                <FormGroup check>
                                    <Label check>
                                        <Input type="checkbox" name="checkbox" />{' '}
                                        Casado
                                    </Label>
                                </FormGroup>
                                <FormGroup check>
                                    <Label check>
                                        <Input type="checkbox" name="checkbox" />{' '}
                                        Divorciado
                                    </Label>
                                </FormGroup>
                                <FormGroup check>
                                    <Label check>
                                        <Input type="checkbox" name="checkbox" />{' '}
                                        Unión libre
                                    </Label>
                                </FormGroup>
                            </Col>
                        </Col>
                        <Col sm={3}>
                            <Col sm={12}>
                                <legend>Edad</legend>
                                <FormGroup check>
                                    <Label check>
                                        <Input type="checkbox" name="radio1" />{' '}
                                        18-25 Años
                                    </Label>
                                </FormGroup>
                                <FormGroup check>
                                    <Label check>
                                        <Input type="checkbox" name="radio1" />{' '}
                                        26-30 Años
                                    </Label>
                                </FormGroup>
                                <FormGroup check>
                                    <Label check>
                                        <Input type="checkbox" name="radio1" />{' '}
                                        31-41 Años
                                    </Label>
                                </FormGroup>
                                <FormGroup check>
                                    <Label check>
                                        <Input type="checkbox" name="radio1" />{' '}
                                        42 años en adelante
                                    </Label>
                                </FormGroup>
                            </Col>
                        </Col>
                        <Col sm={3}>
                            <Col sm={12}>
                                <legend>Sexo</legend>
                                <FormGroup check>
                                    <Label check>
                                        <Input type="checkbox" name="radio1" />{' '}
                                        Masculino
                                    </Label>
                                </FormGroup>
                                <FormGroup check>
                                    <Label check>
                                        <Input type="checkbox" name="radio1" />{' '}
                                        Femenino
                                    </Label>
                                </FormGroup>
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