import 'bootstrap/dist/css/bootstrap.min.css';
import { Link } from 'react-router-dom';
import { Button, Table, Form, FormGroup, Label, Input, FormText, Col, Row, InputGroup, InputGroupAddon, InputGroupText } from 'reactstrap';

const Clientesjuridicos = () => {




    return (
        <div>
            <div className="headerClientesSub">


                <Label style={{ color: "#c7f900" }}>
                    Mantenimiento de Clientes/Clientes/ClientesJuridicos
                </Label>
            </div>

            <div className="divFormClientes">
                <Form className="formSize">
                    <FormGroup row className="rowStyle">

                        <Col sm={2}>
                            <Label for="Codigo Clientes" className="labelInputsStyle">Codigo cliente</Label>
                            <Col sm={4}>
                                <Input style={{ border: '1px solid #003462' }} type="text" name="codigoCliente" id="codigoCliente" />
                            </Col>
                        </Col>
                        <Col sm={2}>
                            <Label for="exampleEmail" className="labelInputsStyle">Tipo de Identificacion</Label>
                            <Col sm={8}>
                                <Input style={{ border: '1px solid #003462' }} type="select" className="select">
                                    <option selected>RUC</option>
                                    <option>CEDULA</option>
                                    <option>PASAPORTE</option>
                                </Input>
                            </Col>
                        </Col>
                        <Col sm={3}>
                            <Label for="exampleEmail" className="labelInputsStyle">Identificacion</Label>
                            <Col sm={8}>
                                <Input type="text" name="Identificacion" style={{ border: '1px solid #003462' }} id="identificacion" />
                            </Col>

                        </Col>

                        <Col sm={3}>
                            <Label for="exampleEmail" className="labelInputsStyle">Nombre</Label>
                            <Col sm={8}>
                                <Input type="text" name="Identificacion" id="identificacion" style={{ border: '1px solid #003462' }} />
                            </Col>

                        </Col>
                        <Col sm={2}>
                            <Label for="exampleEmail" className="labelInputsStyle">Tipo de Identificacion</Label>
                            <Col sm={8}>
                                <Input style={{ border: '1px solid #003462' }} type="select" name="select" className="select">
                                    <option selected>JURIDICA</option>
                                    <option>NATURAL</option>

                                </Input>
                            </Col>
                        </Col>



                    </FormGroup>

                    <div className='linkConfig'>

                        <Link to="/clientes/direcciones" className="MenuEnlaces">
                            Direcciones
                        </Link>

                        <Link to="nueva" className="MenuEnlaces">
                            Asesor
                        </Link>

                        <Link to="nueva" className="MenuEnlaces">
                            Documentos
                        </Link>
                        <Link to="nueva" className="MenuEnlaces">
                            Referencias Comerciales
                        </Link>
                        <Link to="nueva" className="MenuEnlaces">
                            Referencias Bancarias
                        </Link>
                        <Link to="nueva" style={{ color: '#003462' }}>
                            Situacion financiera
                        </Link>

                    </div>
                    <FormGroup row className="rowStyle">
                        <Row >

                            <Col sm={2}>
                                <Label className="labelInputsStyle">Nacionalidad</Label>
                                <Col sm={8}>

                                    <Input style={{ border: '1px solid #003462' }} type="select" className="select" >
                                        <option selected>ECUATORIANA</option>
                                        <option>RUC</option>
                                        <option>PASAPORTE</option>
                                    </Input>
                                </Col>
                            </Col>
                            <Col sm={2}>
                                <Label className="labelInputsStyle">Categoria cliente</Label>
                                <Col sm={8}>

                                    <Input type="select" className="select" style={{ border: '1px solid #003462' }}>
                                        <option selected>DEUDOR</option>
                                        <option>RUC</option>
                                        <option>PASAPORTE</option>
                                    </Input>
                                </Col>
                            </Col>
                            <Col sm={2}>
                                <Label className="labelInputsStyle">Estado</Label>
                                <Col sm={8}>

                                    <Input style={{ border: '1px solid #003462' }} type="select" className="select" >
                                        <option selected>ACTIVO</option>
                                        <option>RUC</option>
                                        <option>PASAPORTE</option>
                                    </Input>
                                </Col>
                            </Col>
                        </Row>
                        <Row >
                            <Col sm={2}>
                                <Label className="labelInputsStyle">Actividad Economica</Label>
                                <Col sm={8}>

                                    <Input type="select" className="select" style={{ border: '1px solid #003462' }}>
                                        <option selected>ARTESANIA</option>
                                        <option>RUC</option>
                                        <option>PASAPORTE</option>
                                    </Input>
                                </Col>
                            </Col>
                            <Col sm={2}>
                                <Label className="labelInputsStyle">Tipo de rol</Label>
                                <Col sm={8}>

                                    <Input style={{ border: '1px solid #003462' }} type="select" className="select" >
                                        <option selected>NO APLICA</option>
                                        <option>RUC</option>
                                        <option>PASAPORTE</option>
                                    </Input>
                                </Col>
                            </Col>


                        </Row>



                    </FormGroup>
                    <FormGroup row className="rowStyle">
                        <Row>
                            <Col sm={2}>
                                <Label className="labelInputsStyle">Tipo empresa</Label>
                                <Col sm={8}>

                                    <Input style={{ border: '1px solid #003462' }} type="select" className="select" >
                                        <option selected>SOCIEDAD</option>
                                    </Input>
                                </Col>
                            </Col>
                            <Col sm={2}>
                                <Label className="labelInputsStyle">RAZON SOCIAL</Label>
                                <Col sm={8}>

                                    <Input type="text" className="select" style={{ border: '1px solid #003462' }}>
                                        <option selected>CASTILLO</option>
                                        <option>RUC</option>
                                        <option>PASAPORTE</option>
                                    </Input>
                                </Col>
                            </Col>
                            <Col sm={2}>
                                <Label className="labelInputsStyle">Nombre publicitario</Label>
                                <Col sm={8}>

                                    <Input style={{ border: '1px solid #003462' }} type="text" className="select" >

                                    </Input>
                                </Col>

                            </Col>
                        </Row>




                        <Row >
                            <Col sm={2}>
                                <Label className="labelInputsStyle">Capital suscrito</Label>
                                <Col sm={8}>

                                    <Input type="text" className="select" style={{ border: '1px solid #003462' }}>

                                    </Input>
                                </Col>
                            </Col>
                            <Col sm={2}>
                                <Label className="labelInputsStyle">Capital pagado</Label>
                                <Col sm={8}>

                                    <Input style={{ border: '1px solid #003462' }} type="text" className="select" >

                                    </Input>
                                </Col>
                            </Col>

                            <Col sm={2}>
                                <Label className="labelInputsStyle">Reserva legal: </Label>
                                <Col sm={8}>

                                    <Input type="text" className="select" style={{ border: '1px solid #003462' }}>

                                    </Input>
                                </Col>
                            </Col>

                        </Row>
                        <Row >
                            <Col sm={2}>
                                <Label className="labelInputsStyle">Grupo economico</Label>
                                <Col sm={8}>

                                    <Input type="select" className="select" style={{ border: '1px solid #003462' }}>
                                        <option selected>NINGUNO</option>
                                        <option>RUC</option>
                                        <option>PASAPORTE</option>
                                    </Input>
                                </Col>
                            </Col>

                            <Col sm={2}>
                                <Label className="labelInputsStyle">Fecha reforma estatutos</Label>
                                <Col sm={8}>

                                    <Input style={{ border: '1px solid #003462' }} type="date" className="select" >

                                    </Input>
                                </Col>
                            </Col>

                        </Row>


                    </FormGroup>




                </Form>

                <div className="containerButtonStyleFooter">
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
export default Clientesjuridicos;