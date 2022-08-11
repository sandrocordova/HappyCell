import 'bootstrap/dist/css/bootstrap.min.css';
import { Link } from 'react-router-dom';
import './../../styled-components/styles_panelandbuttons.css';
import { Button, Table, Form, FormGroup, Label, Input, FormText, Col, Row, InputGroup, InputGroupAddon, InputGroupText } from 'reactstrap';

const Clientesnaturales = () => {


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
                    Mantenimiento de Clientes/Clientes/ClientesNaturales
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



                    </Row>

                    <div className='linkConfig'>

                        <Link to="/clientes/direcciones">
                            Direcciones 
                        </Link>

                        <Link to="nueva">
                            Asesor
                        </Link>

                        <Link to="nueva">
                            Documentos
                        </Link>
                        <Link to="nueva">
                            Referencias Comerciales
                        </Link>
                        <Link to="nueva">
                            Referencias Bancarias
                        </Link>
                        <Link to="nueva">
                            Situacion financiera
                        </Link>

                    </div>

                    <Row className="rowStyle">

                        <Col sm={2}>
                            <Label >Nacionalidad</Label>
                            <Col sm={8}>

                                <Input type="select" className="select" >
                                    <option selected>ECUATORIANA</option>
                                    <option>RUC</option>
                                    <option>PASAPORTE</option>
                                </Input>
                            </Col>
                        </Col>
                        <Col sm={2}>
                            <Label >Categoria cliente</Label>
                            <Col sm={8}>

                                <Input type="select" className="select" >
                                    <option selected>DEUDOR</option>
                                    <option>RUC</option>
                                    <option>PASAPORTE</option>
                                </Input>
                            </Col>
                        </Col>
                        <Col sm={2}>
                            <Label >Estado</Label>
                            <Col sm={8}>

                                <Input type="select" className="select" >
                                    <option selected>ECUATORIANA</option>
                                    <option>RUC</option>
                                    <option>PASAPORTE</option>
                                </Input>
                            </Col>
                        </Col>

                        <Row >
                            <Col sm={2}>
                                <Label >Actividad Economica</Label>
                                <Col sm={8}>

                                    <Input type="select" className="select" >
                                        <option selected>ARTESANIA</option>
                                        <option>RUC</option>
                                        <option>PASAPORTE</option>
                                    </Input>
                                </Col>
                            </Col>
                            <Col sm={2}>
                                <Label >Tipo de rol</Label>
                                <Col sm={8}>

                                    <Input type="select" className="select" >
                                        <option selected>NO APLICA</option>
                                        <option>RUC</option>
                                        <option>PASAPORTE</option>
                                    </Input>
                                </Col>
                            </Col>
               

                        </Row>

                    </Row>
                    <Row className="rowStyle">

                        <Col sm={2}>
                            <Label >Primer Nombre</Label>
                            <Col sm={8}>
                                
                                <Input type="text" className="select" >

                                </Input>
                            </Col>
                        </Col>
                        <Col sm={2}>
                            <Label >Segundo Nombre</Label>
                            <Col sm={8}>

                                <Input type="text" className="select" >
                                    <option selected>CASTILLO</option>
                                    <option>RUC</option>
                                    <option>PASAPORTE</option>
                                </Input>
                            </Col>
                        </Col>
                        <Col sm={2}>
                            <Label >Primer apellido</Label>
                            <Col sm={8}>

                                <Input type="text" className="select" >
                                    <option selected>CASTILLO</option>
                                    <option>RUC</option>
                                    <option>PASAPORTE</option>
                                </Input>
                            </Col>

                        </Col>
                        <Col sm={2}>
                            <Label >Segundo apellido</Label>
                            <Col sm={8}>

                                <Input type="text" className="select" >
                                   
                                </Input>
                            </Col>

                        </Col>

                        <Row >
                            <Col sm={2}>
                                <Label >Sexo</Label>
                                <Col sm={8}>

                                    <Input type="select" className="select" >
                                        <option selected>Masculino</option>
                                        <option>RUC</option>
                                        <option>PASAPORTE</option>
                                    </Input>
                                </Col>
                            </Col>
                            <Col sm={2}>
                                <Label >Profesion</Label>
                                <Col sm={8}>

                                    <Input type="select" className="select" >
                                        <option selected>PROFESOR</option>
                                        <option>RUC</option>
                                        <option>PASAPORTE</option>
                                    </Input>
                                </Col>
                            </Col>
                            <Col sm={2}>
                                <Label >Estado Civil</Label>
                                <Col sm={8}>

                                    <Input type="select" className="select" >
                                        <option selected>CASADO</option>
                                        <option>RUC</option>
                                        <option>PASAPORTE</option>
                                    </Input>
                                </Col>
                            </Col>
                            <Col sm={2}>
                                <Label >Situacion Laboral</Label>
                                <Col sm={8}>

                                    <Input type="select" className="select" >
                                        <option selected>EMPLEADO</option>
                                        <option>RUC</option>
                                        <option>PASAPORTE</option>
                                    </Input>
                                </Col>
                            </Col>

                        </Row>
                        <Row >
                            <Col sm={2}>
                                <Label >Tipo de vivienda</Label>
                                <Col sm={8}>

                                    <Input type="select" className="select" >
                                        <option selected>PROPIA</option>
                                        <option>RUC</option>
                                        <option>PASAPORTE</option>
                                    </Input>
                                </Col>
                            </Col>
                            <Col sm={2}>
                                <Label >Lugar de nacimiento</Label>
                                <Col sm={8}>

                                    <Input type="text" className="select" >
                                        
                                    </Input>
                                </Col>
                            </Col>
                            <Col sm={2}>
                                <Label >Numero de cargas</Label>
                                <Col sm={8}>

                                    <Input type="text" className="select" >

                                    </Input>
                                </Col>
                            </Col>
                            <Col sm={2}>
                                <Label >Fecha de nacimiento</Label>
                                <Col sm={8}>

                                    <Input type="date" className="select" >

                                    </Input>
                                </Col>
                            </Col>

                        </Row>
                        <Row >
                            <Col sm={2}>
                                <Label >Empresa trabajo</Label>
                                <Col sm={8}>

                                    <Input type="text" className="select" >

                                    </Input>
                                </Col>
                            </Col>
                            <Col sm={2}>
                                <Label >Exp.pasaporte</Label>
                                <Col sm={8}>

                                    <Input type="date" className="select" >

                                    </Input>
                                </Col>
                            </Col>
                            <Col sm={2}>
                                <Label >Inicio ingresos</Label>
                                <Col sm={8}>

                                    <Input type="date" className="select" >

                                    </Input>
                                </Col>
                            </Col>
                            <Col sm={2}>
                                <Label >Inicio residencia</Label>
                                <Col sm={8}>

                                    <Input type="date" className="select" >

                                    </Input>
                                </Col>
                            </Col>

                        </Row>

                    </Row>




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
export default Clientesnaturales;