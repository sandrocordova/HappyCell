import './styles_clientes.css'
import { Link } from 'react-router-dom';
import 'bootstrap/dist/css/bootstrap.min.css';
import { Button, Table, Form, FormGroup, Label, Input, FormText, Col, Row, InputGroup, InputGroupAddon, InputGroupText } from 'reactstrap';

const Clientesvista_clientes = () => {


    return (
        <div>
            <div className="opcionesCuadradas">
                <div className="headerClientes">
                    <Link to="/clientes">
                        <Button className="buttonIcon" title="Clientes" size="large" variant="contained" alt="Clientes">
                            <img className="imgIcon" src="https://cdn-icons.flaticon.com/png/128/3936/premium/3936751.png?token=exp=1659593203~hmac=4b7dd15d13b93caf41c2566c56231078" alt="Clientes" />

                        </Button>

                    </Link>
                    <Label >
                        Clientes
                    </Label>

                </div>

                <Form>
                    <div className='contenedor-titulo'>

                    </div>
                    <FormGroup row>
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

                    </FormGroup>
                    <Table striped bordered hover>
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
                    <div className='contenedor-botones'>
                        <Button color='primary'>Seleccionar</Button>{' '}
                        <Button color="danger">Cerrar</Button>





                    </div>

                </Form>


            </div >

        </div >

    )
};
export default Clientesvista_clientes;