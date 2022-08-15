
import { Link } from 'react-router-dom';
import 'bootstrap/dist/css/bootstrap.min.css';
import { Button, Table, Form, FormGroup, Label, Input, FormText, Col, Row, InputGroup, InputGroupAddon, InputGroupText } from 'reactstrap';
const Direccionesvista_direcciones = () => {


    return (
        <div>
            <div className="opcionesCuadradas">
                <div className="headerClientes">

                    <Link to="/clientes" >

                        <Button className="buttonIcon" title="Clientes" size="large" variant="contained" title="Clientes" alt="Clientes">
                            <img className="imgIcon" src="https://cdn-icons.flaticon.com/png/128/3936/premium/3936751.png?token=exp=1659593203~hmac=4b7dd15d13b93caf41c2566c56231078" alt="Clientes" />

                        </Button>

                    </Link>
                    <Label >
                        Direcciones
                    </Label>

                </div>

                <Form>
                    <div className='contenedor-titulo'>

                    </div>
                    <FormGroup row>
                        <Col sm={1}>
                            <Label for="Identificacion">Codigo: </Label>
                            <Col sm={10}>
                                <Input type="id" name="identificacion" id="identificacion" />
                            </Col>
                        </Col>
                        <Col sm={3}>
                            <Label for="exampleEmail">Tipo de identificacion</Label>
                            <Col sm={10}>
                                <Input type="nombre" name="nombre" id="nombre" />
                            </Col>
                        </Col>
                        <Col sm={3}>
                            <Label for="exampleEmail">Identificacion</Label>
                            <Col sm={10}>
                                <Input type="nombre" name="nombre" id="nombre" />
                            </Col>
                        </Col>
                        <Col sm={2}>
                            <Label for="exampleEmail">Nombre</Label>
                            <Col sm={10}>
                                <Input type="nombre" name="nombre" id="nombre" />
                            </Col>
                        </Col>
                        <Col sm={3}>
                            <Label for="exampleEmail">Tipo</Label>
                            <Col sm={10}>
                                <Input type="nombre" name="nombre" id="nombre" />
                            </Col>
                        </Col>

                    </FormGroup>

                    <div className='contenedor-btn-crear'>
                        <Link to="nueva">
                            <a>Crear</a>
                        </Link>
                    </div>
                    <Table className="tab" striped bordered hover>
                        <thead>
                            <tr>
                                <th>
                                    <Input type="checkbox" name="checkS" id="opc" />
                                </th>
                                <th>Tipo de direccion</th>
                                <th>Secuencia</th>
                                <th>Ciudad</th>
                                <th>Direccion</th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr>
                                <td>
                                    <Input type="checkbox" name="checkSelect" id="opc" />
                                </td>
                                <td>Domicilio</td>
                                <td>1</td>
                                <td>QUITO</td>
                                <td>Natural</td>
                            </tr>
                            <tr>
                                <td>
                                    <Input type="checkbox" name="checkSelect" id="opc" />
                                </td>
                                <td>Trabajo</td>
                                <td>1</td>
                                <td>QUITO</td>
                                <td>Juridica</td>
                            </tr>

                        </tbody>
                    </Table>


                </Form>
                <div className="containerButtonStyleFooter">
                    <Link to="/clientes/direcciones/direcciones2">
                        <Button className="buttonStyleFooter" color="success">Seleccionar</Button>
                    </Link>
                    <Link to="/clientes/vistaclientes/clientesjuridicos">
                        <Button className="buttonStyleFooter" color="danger">Cerrar</Button>
                    </Link>
                </div>

            </div >

        </div >

    )
};
export default Direccionesvista_direcciones;