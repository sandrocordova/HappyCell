
import { Link } from 'react-router-dom';
import 'bootstrap/dist/css/bootstrap.min.css';
import { Button, Table, Form, FormGroup, Label, Input, FormText, Col, Row, InputGroup, InputGroupAddon, InputGroupText } from 'reactstrap';
const Direccionestelefono2 = () => {


    return (
        <div>
            <div className="headerClientesSub">

                <Link to="/clientes">
                    <Button className="buttonIcon" title="Clientes" size="large" variant="contained" alt="Clientes">
                        <img className="imgIcon" src="https://cdn-icons.flaticon.com/png/128/3936/premium/3936751.png?token=exp=1659593203~hmac=4b7dd15d13b93caf41c2566c56231078" alt="Clientes" />

                    </Button>

                </Link>
                <Label >
                    Clientes
                </Label>
                <br />
                <Label>
                    Mantenimiento de Direcciones/Telefono
                </Label>
            </div>

            <div className="opcionesCuadradas">
                <Form className="formSize">
                    <Row className="rowStyle">

                        <Col sm={2}>
                            <Label for="Codigo Clientes">Codigo cliente</Label>
                            <Col sm={4}>
                                <Input type="text" name="codigoCliente" id="codigoCliente" />
                            </Col>
                        </Col>
                        <Col sm={2}>
                            <Label for="exampleEmail">Tipo de Identificacion</Label>
                            <Col sm={8}>
                                <Input type="select" className="select">
                                    <option selected>CEDULA</option>
                                    <option>RUC</option>
                                    <option>PASAPORTE</option>
                                </Input>
                            </Col>
                        </Col>
                        <Col sm={3}>
                            <Label for="exampleEmail">Identificacion</Label>
                            <Col sm={8}>
                                <Input type="text" name="Identificacion" id="identificacion" />
                            </Col>

                        </Col>

                        <Col sm={3}>
                            <Label for="exampleEmail">Nombre</Label>
                            <Col sm={8}>
                                <Input type="text" name="Identificacion" id="identificacion" />
                            </Col>

                        </Col>
                        <Col sm={2}>
                            <Label for="exampleEmail">Tipo de Identificacion</Label>
                            <Col sm={8}>
                                <Input type="select" name="select" className="select">
                                    <option selected>NATURAL</option>
                                    <option>JURIDICO</option>

                                </Input>
                            </Col>
                        </Col>
                        <Row>
                            <Col sm={2}>
                                <Label >Secuencia</Label>
                                <Col sm={8}>

                                    <Input type="text" className="select" >

                                    </Input>
                                </Col>
                            </Col>
                            <Col sm={2}>
                                <Label >Ciudad</Label>
                                <Col sm={8}>

                                    <Input type="text" className="select" >

                                    </Input>
                                </Col>
                            </Col>
                            <Col sm={2}>
                                <Label >Direccion</Label>
                                <Col sm={8}>

                                    <Input type="text" className="select" >

                                    </Input>
                                </Col>
                            </Col>
                        </Row>


                    </Row>

              

                    <Row className="rowStyleDir">


                        <Row>
                            <Label >Tipo de telefono</Label>
                            <Col sm={8}>

                                <Input type="select" className="select" >
                                    <option selected>DOMICILIO</option>
                                </Input>
                            </Col>
                        </Row>
                        <Row>
                            <Label >nUMERO DE TELEFONO</Label>
                            <Col sm={8}>

                                <Input type="text" className="select" >

                                </Input>
                            </Col>
                        </Row>


                    </Row>





                </Form>

                <div className="buttomStyle">
                    <Link to="/clientes/vistaclientes/clientesnaturales">
                        <Button className="buttonStyleFooter" color="success">Grabar</Button>
                    </Link>
                    <Link to="/clientes/vistaclientes/clientesjuridicos">
                        <Button className="buttonStyleFooter" color="danger">Cerrar</Button>
                    </Link>
                </div>
            </div >

        </div >

    )
};
export default Direccionestelefono2;