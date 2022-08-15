
import { Link } from 'react-router-dom';
import 'bootstrap/dist/css/bootstrap.min.css';
import { Button, Table, Form, FormGroup, Label, Input, FormText, Col, Row, InputGroup, InputGroupAddon, InputGroupText } from 'reactstrap';
const Direccionestelefono = () => {


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

                    <div className='linkConfig'>

                        <Link to="/clientes/direcciones">
                            Crear
                        </Link>



                    </div>

                    <Table className="table" striped bordered hover>
                        <thead>
                            <tr>
                                <th>
                                    <Input type="checkbox" name="checkS" id="opc" />
                                </th>
                                <th>Tipo de telefono</th>
                                <th>Telefono</th>

                            </tr>
                        </thead>
                        <tbody>
                            <tr>
                                <td>
                                    <Input type="checkbox" name="checkSelect" id="opc" />
                                </td>
                                <td>CONVENCIONAL</td>
                                <td>1709337735</td>

                            </tr>
                            <tr>
                                <td>
                                    <Input type="checkbox" name="checkSelect" id="opc" />
                                </td>
                                <td>CELULAR</td>
                                <td>1711007276</td>

                            </tr>

                        </tbody>
                    </Table>





                </Form>

                <div className="containerButtonStyleFooter">
                    <Link to="/clientes/direcciones/direcciones2/telefono/telefono2">
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
export default Direccionestelefono;