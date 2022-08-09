import React from 'react';
import './styles.css';
import 'bootstrap/dist/css/bootstrap.min.css';
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
                                <Input type="number" name="email" id="exampleEmail" />
                            </Col><br></br>
                            <Link to=" s">
                                <Button color='secondary'>Probar Plantilla</Button>{' '}
                            </Link>
                            <br></br>
                            <a href='#Este es un ejemplo'> Ejemplo </a>
                            <br></br>
                            <a href=" https://web.whatsapp.com/"> Hola</a>
                            <p href="#">asd</p>
                            <ul>
                                <li><a href="ss:">1</a></li>

                                <p draggable="true">This is a draggable paragraph.</p>

                                <a draggable="true">This is a draggable paragraph.</a>

                                <a id='init1' key="12" draggable="true" >21231313</a>
                                
                            </ul>
                            <ul>
                                <div className="todos">

                                    <div id='ejemp1'
                                        key="1"
                                        draggable
                                        onDrag={(event) => this.onDrag(event)}
                                        value="Hola"
                                        onDragStar={(event) => this.onDragStar(event)}
                                    >
                                        Ejemplooooo
                                    </div>
                                </div>
                                <div id="div1" onDrop={event => this.onDrop(event)} draggable onDragOver={(event => this.onDragOver(event))}>
                                    --------<br>
                                    </br>
                                    <span id="drag1" onDrag={(event) => this.onDrag(event)} draggable="true"
                                        onDragStar={(event) => this.onDragStar(event)}>drag me to the other box</span>
                                    suelta aquí <br></br>----
                                </div>
                            </ul>
                            <ul>
                                <div id="div2" onDrop={event => this.onDrop(event)} draggable onDragOver={(event => this.onDragOver(event))}>------
                                    <br></br>suelta aquí <br></br>------------</div>
                                <div
                                    onDrop={event => this.onDrop(event)}
                                    onDragOver={(event => this.onDragOver(event))}
                                    className="done"
                                    id='div3'
                                    value="Hola"
                                >
                                    ...
                                    distdsa
                                    sda
                                </div>
                            </ul>
                        </Col>
                        <Col sm={6}>
                            <Label for="imput1">Modelo de Plantilla</Label>
                            <Col sm={12}>
                                <Input onDrop={event => this.onDrop(event)}
                                    onDragOver={(event => this.onDragOver(event))}
                                    id="imput1" type="textarea" placeholder='sdada' rows="10" name="email" />
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