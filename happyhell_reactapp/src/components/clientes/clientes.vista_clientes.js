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
                        <Button className="buttonIcon" title="Clientes" size="large" variant="contained" title="Clientes" alt="Clientes">
                            <img className="imgIcon" src="https://cdn-icons.flaticon.com/png/128/3936/premium/3936751.png?token=exp=1659593203~hmac=4b7dd15d13b93caf41c2566c56231078" alt="Clientes" />

                        </Button>
                    </Link>
                </div>

                <ul>
                    Identificacion
                    <li>
                        <input type="text" name="identificacion"></input>
                    </li>
                    Nombre
                    <li>


                    </li>

                </ul>


                <br />

                <Table striped bordered hover variant="table">
                    <thead>
                        <tr>
                            <th>
                                <input name="select" className="checkBoxButton" type="checkbox" />
                            </th>
                            <th>Codigo cliente</th>
                            <th>Identificacion</th>
                            <th>Nombre</th>
                            <th>Tipo Cliente</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr>
                            <td>1</td>
                            <td>Mark</td>
                            <td>Otto</td>
                            <td>@mdo</td>
                        </tr>
                        <tr>
                            <td>2</td>
                            <td>Jacob</td>
                            <td>Thornton</td>
                            <td>@fat</td>
                        </tr>
                        <tr>
                            <td>3</td>
                            <td colSpan={2}>Larry the Bird</td>
                            <td>@twitter</td>
                        </tr>
                    </tbody>
                </Table>




            </div >

        </div >

    )
};
export default Clientesvista_clientes;