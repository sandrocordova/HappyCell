import 'bootstrap/dist/css/bootstrap.min.css';
import { Link } from 'react-router-dom';
import './../../styled-components/styles_generales.css';
import { Button, Table, Form, FormGroup, Label, Input, FormText, Col, Row, InputGroup, InputGroupAddon, InputGroupText } from 'reactstrap';

const Clientesvista_clientes = () => {


    return (
        <div>
            <div className="headerClientesSub">

                <Label style={{ color: '#c7f900' }}>
                    Mantenimiento de Clientes/Clientes
                </Label>
            </div>
            <div className="containerSearch">
                <Button className="buttonSearch" style={{ background: '#003462', color: "#ffffff" }}>Buscar</Button>
            </div>
            <div className="divTable">
                <Form>
                    <Row>

                        <Col sm={3}>
                            <Label for="Identificacion">Identificacion</Label>
                            <Col sm={12}>
                                <Input style={{ border: '1px solid #003462' }} type="id" name="identificacion" id="identificacion" />
                            </Col>
                        </Col>
                        <Col sm={3}>
                            <Label for="exampleEmail">Nombre</Label>
                            <Col sm={12}>
                                <Input style={{ border: '1px solid #003462' }} type="nombre" name="nombre" id="nombre" />
                            </Col>

                        </Col>






                    </Row>

                    <div className='contenedorEstiloEnlaces'>
                        <Link to="nueva" style={{color:'#c7f900'}}>
                        <a >Crear</a>
                        </Link>
                    </div>
                    <Table className="table" style={{ border: '1px solid #003462' }} striped bordered hover>
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
                        <Button className="buttonStyleFooter"  >Seleccionar</Button>
                    </Link>
                    <Link to="/clientes/vistaclientes/clientesjuridicos">
                        <Button className="buttonStyleFooter" >Cerrar</Button>
                    </Link>
                </div>

            </div >

        </div >

    )
};
export default Clientesvista_clientes;