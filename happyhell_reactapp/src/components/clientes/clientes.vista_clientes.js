import 'bootstrap/dist/css/bootstrap.min.css';
import { Link } from 'react-router-dom';
import './../../styled-components/styles_generales.css';
import { Button, Table, Form, FormGroup, Label, Input, FormText, Col, Row, InputGroup, InputGroupAddon, InputGroupText } from 'reactstrap';

const Clientesvista_clientes = () => {


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
                    Mantenimiento de Clientes/Clientes
                </Label>
            </div>

            <div className="opcionesCuadradas">
                <Form>
                    <Row>

                        <Col sm={3}>
                            <Label for="Identificacion">Identificacion</Label>
                            <Col sm={12}>
                                <Input type="id" name="identificacion" id="identificacion" />
                            </Col>
                        </Col>
                        <Col sm={3}>
                            <Label for="exampleEmail">Nombre</Label>
                            <Col sm={12}>
                                <Input type="nombre" name="nombre" id="nombre" />
                            </Col>

                        </Col>
                        
                        <Col sm={5}>

                                <Button className="buttonSearch" color="secondary">Buscar</Button>
                           
                        </Col>
                                


                    </Row>

                    <div className='contenedor-btn-crear'>
                        <Link to="nueva">
                            <a>Crear</a>
                        </Link>
                    </div>
                    <Table className="table" striped bordered hover>
                        <thead>
                            <tr>
                                <th>
                                    <Input type="checkbox" name="checkS" id="opc" />
                                </th>
                                <th>Codigo Cliente</th>
                                <th>Identificacion</th>
                                <th>Nombre</th>
                                <th>Tipo Cliente</th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr>
                                <td>
                                    <Input type="checkbox" name="checkSelect" id="opc" />
                                </td>
                                <td>001</td>
                                <td>1709337735</td>
                                <td>ALBERTO CASTILLO BRIONES</td>
                                <td>Natural</td>
                            </tr>
                            <tr>
                                <td>
                                    <Input type="checkbox" name="checkSelect" id="opc" />
                                </td>
                                <td>002</td>
                                <td>1711007276</td>
                                <td>COOPERATIVA AMAZONICA</td>
                                <td>Juridica</td>
                            </tr>

                        </tbody>
                    </Table>


                </Form>
                <div className="containerButtonStyleFooter">
                    <Link to="/clientes/vistaclientes/clientesnaturales">
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
export default Clientesvista_clientes;