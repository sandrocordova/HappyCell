import React from 'react';
import './styles.css';
import { Button, Form, FormGroup, Label, Input, FormText, Col, Row, InputGroup, InputGroupAddon, InputGroupText } from 'reactstrap';
import { Link } from 'react-router-dom';






export default class SearchBar extends React.Component {
    constructor() {
        super()



    }

    onDragOver = (event) => {
        event.stopPropagation();
        event.preventDefault();
        event.target.style.color = 'orange';
    }

    onDrag = (event) => {
        console.log("--------------entró")
        event.dataTransfer.setData("Text", event.target.id);
        event.target.style.color = 'red';
    }


    onDragStar = (event) => {
        event.dataTransfer.setData("text", event.target.id);
        event.target.style.color = 'green';
    }

    onDrop = (event, el) => {
        event.stopPropagation();
        event.preventDefault();
        const data = event.dataTransfer.getData("text");
        event.target.appendChild(document.getElementById(data));
        console.log("--------------" + data)
        document.getElementById("drag1").style.color = 'black';
        event.target.style.color = 'yellow';
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
                                <Input type="number" name="email" id="exampleEmail" placeholder='47891221456614'/>
                            </Col><br></br>
                            
                            <br></br>
                            <ul>
                                <a href="ss:">115023526</a>
                                <br></br>
                                <a draggable="true" href="Apellido:">Apellido</a>
                                <br></br>
                                <a draggable="true" href="Nombre:">Nombre</a>
                            </ul>
                            <br></br>
                            <div className='contenedor-botones'>
                            <Link to=" s">
                                <Button color='secondary'>Probar Plantilla</Button>{' '}
                            </Link></div>
                        </Col>
                        <Col sm={6}>
                            <Label for="imput1">Modelo de Plantilla</Label>
                            <Col sm={12}>
                                <Input onDrop={event => this.onDrop(event)}
                                    onDragOver={(event => this.onDragOver(event))}
                                    id="imput1" type="textarea" placeholder='Plantilla desarrollada' rows="10" name="email" />
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