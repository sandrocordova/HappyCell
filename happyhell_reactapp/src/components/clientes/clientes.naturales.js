import 'bootstrap/dist/css/bootstrap.min.css';
import { Link } from 'react-router-dom';
import { Button, Table, Form, FormGroup, Label, Input, FormText, Col, Row, InputGroup, InputGroupAddon, InputGroupText } from 'reactstrap';
import React, { useEffect, useState, useRef } from 'react';

const Clientesnaturales = () => {
    const [opcs, setOpcs] = useState([]);
    useEffect(() => {
        obtainData()
    }, []);
    const obtainData = async () => {

        const data = await fetch('http://192.168.88.103:8080/api/cliente');
        const opc = await data.json()

        setOpcs(opc)

    }
    const validacion = Object.values(opcs);
    const validacion2 = validacion.filter(item => item.CLIE_CODIGO == "4578");
    console.log(validacion2);
    const array = [];

    for (var i in validacion2) {
        array.push([i, validacion2[i]]);
    }
    console.log("HOLA MUNDO")
    console.log(validacion2.find(item => item.CLIE_CODIGO))



    return (
        <div>
            <div className="headerClientesSub">


                <Label style={{ color: "#c7f900" }}>
                    Mantenimiento de Clientes/Clientes/ClientesNaturales
                </Label>
            </div>
            <div className="containerSearch">
                <FormGroup row className="rowStyleBar4">

                    <Col sm={2}>
                        <Label style={{ color: "#c7f900" }} for="Codigo Clientes" className="labelInputsStyle">Codigo cliente</Label>
                        <Col sm={4}>

                            <Input type="text" name="codigoCliente" placeholder={validacion2.CLIE_CODIGO} id="codigoCliente" style={{ border: '1px solid #003462' }} />

                        </Col>
                    </Col>
                    <Col sm={2}>
                        <Label for="exampleEmail" style={{ color: "#c7f900" }} className="labelInputsStyle">Tipo de Identificacion</Label>
                        <Col sm={8}>
                            <Input type="select" className="select" style={{ border: '1px solid #003462' }}>
                                <option selected></option>
                                <option>RUC</option>
                                <option>PASAPORTE</option>
                            </Input>
                        </Col>
                    </Col>
                    <Col sm={2}>
                        <Label for="exampleEmail" className="labelInputsStyle" style={{ color: "#c7f900" }}>Tipo de cliente</Label>
                        <Col sm={8}>
                            <Input type="select" name="select" className="select" style={{ border: '1px solid #003462' }}>
                                <option selected></option>
                                <option>JURIDICO</option>

                            </Input>
                        </Col>
                    </Col>
                    <Col sm={3}>
                        <Label for="exampleEmail" style={{ color: "#c7f900" }} className="labelInputsStyle">Identificacion</Label>
                        <Col sm={8}>
                            <Input type="text" name="Identificacion" id="identificacion" style={{ border: '1px solid #003462' }} />
                        </Col>

                    </Col>

                    <Col sm={3}>
                        <Label for="exampleEmail " style={{ color: "#c7f900" }} className="labelInputsStyle">Nombre</Label>
                        <Col sm={8}>
                            <Input type="text" name="Identificacion" id="identificacion" style={{ border: '1px solid #003462' }} />
                        </Col>

                    </Col>




                </FormGroup>
            </div>
            <div className='linkConfig'>

                <Link to="/clientes/direcciones" className="MenuEnlaces" >
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
            <div className="divFormClientes">
                <Form className="formSize">




                    <FormGroup row className="rowStyle">
                        <Row>
                            <Col sm={2}>
                                <Label className="labelInputsStyle">Nacionalidad</Label>
                                <Col sm={8}>

                                    <Input type="select" className="select" style={{ border: '1px solid #003462' }}>
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

                                    <Input type="select" className="select" style={{ border: '1px solid #003462' }}>
                                        <option selected>ACTIVO</option>
                                        <option>RUC</option>
                                        <option>PASAPORTE</option>
                                    </Input>
                                </Col>
                            </Col>
                        </Row>
                        <Row>
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

                                    <Input type="select" className="select" style={{ border: '1px solid #003462' }}>
                                        <option selected>NO APLICA</option>
                                        <option>RUC</option>
                                        <option>PASAPORTE</option>
                                    </Input>
                                </Col>
                            </Col>

                        </Row>
                    </FormGroup >


                    <FormGroup row className="rowStyle">
                        <Row>
                            <Col sm={2}>
                                <Label className="labelInputsStyle" >Primer Nombre</Label>
                                <Col sm={8}>

                                    <Input type="text" className="select" style={{ border: '1px solid #003462' }}>

                                    </Input>
                                </Col>
                            </Col>
                            <Col sm={2}>
                                <Label className="labelInputsStyle">Segundo Nombre</Label>
                                <Col sm={8}>

                                    <Input type="text" className="select" style={{ border: '1px solid #003462' }}>
                                        <option selected>CASTILLO</option>
                                        <option>RUC</option>
                                        <option>PASAPORTE</option>
                                    </Input>
                                </Col>
                            </Col>
                            <Col sm={2}>
                                <Label className="labelInputsStyle">Primer apellido</Label>
                                <Col sm={8}>

                                    <Input type="text" className="select" style={{ border: '1px solid #003462' }}>
                                        <option selected>CASTILLO</option>
                                        <option>RUC</option>
                                        <option>PASAPORTE</option>
                                    </Input>
                                </Col>

                            </Col>
                            <Col sm={2}>
                                <Label className="labelInputsStyle">Segundo apellido</Label>
                                <Col sm={8}>

                                    <Input type="text" className="select" style={{ border: '1px solid #003462' }}>

                                    </Input>
                                </Col>

                            </Col>
                        </Row>
                        <Row >
                            <Col sm={2}>
                                <Label className="labelInputsStyle">Sexo</Label>
                                <Col sm={8}>

                                    <Input type="select" className="select" style={{ border: '1px solid #003462' }}>
                                        <option selected>Masculino</option>
                                        <option>RUC</option>
                                        <option>PASAPORTE</option>
                                    </Input>
                                </Col>
                            </Col>
                            <Col sm={2}>
                                <Label className="labelInputsStyle">Profesion</Label>
                                <Col sm={8}>

                                    <Input type="select" className="select" style={{ border: '1px solid #003462' }}>


                                        <option selected>PROFESOR</option>
                                        <option>RUC</option>
                                        <option>PASAPORTE</option>
                                    </Input>
                                </Col>
                            </Col>
                            <Col sm={2}>
                                <Label className="labelInputsStyle">Estado Civil</Label>
                                <Col sm={8}>

                                    <Input type="select" className="select" style={{ border: '1px solid #003462' }}>
                                        <option selected>CASADO</option>
                                        <option>RUC</option>
                                        <option>PASAPORTE</option>
                                    </Input>
                                </Col>
                            </Col>
                            <Col sm={2}>
                                <Label className="labelInputsStyle">Situacion Laboral</Label>
                                <Col sm={8}>

                                    <Input type="select" className="select" style={{ border: '1px solid #003462' }}>
                                        <option selected>EMPLEADO</option>
                                        <option>RUC</option>
                                        <option>PASAPORTE</option>
                                    </Input>
                                </Col>
                            </Col>

                        </Row>
                        <Row >
                            <Col sm={2}>
                                <Label className="labelInputsStyle">Tipo de vivienda</Label>
                                <Col sm={8}>

                                    <Input type="select" className="select" style={{ border: '1px solid #003462' }}>
                                        <option selected>PROPIA</option>
                                        <option>RUC</option>
                                        <option>PASAPORTE</option>
                                    </Input>
                                </Col>
                            </Col>
                            <Col sm={2}>
                                <Label className="labelInputsStyle">Lugar de nacimiento</Label>
                                <Col sm={8}>

                                    <Input type="text" className="select" style={{ border: '1px solid #003462' }}>

                                    </Input>
                                </Col>
                            </Col>
                            <Col sm={2}>
                                <Label className="labelInputsStyle">Numero de cargas</Label>
                                <Col sm={8}>

                                    <Input type="text" className="select" style={{ border: '1px solid #003462' }}>

                                    </Input>
                                </Col>
                            </Col>
                            <Col sm={2}>
                                <Label className="labelInputsStyle">Fecha de nacimiento</Label>
                                <Col sm={8}>

                                    <Input type="date" className="select" style={{ border: '1px solid #003462' }}>

                                    </Input>
                                </Col>
                            </Col>

                        </Row>
                        <Row >
                            <Col sm={2}>
                                <Label className="labelInputsStyle">Empresa trabajo</Label>
                                <Col sm={8}>

                                    <Input type="text" className="select" style={{ border: '1px solid #003462' }}>

                                    </Input>
                                </Col>
                            </Col>
                            <Col sm={2}>
                                <Label className="labelInputsStyle">Exp.pasaporte</Label>
                                <Col sm={8}>

                                    <Input type="date" className="select" style={{ border: '1px solid #003462' }}>

                                    </Input>
                                </Col>
                            </Col>
                            <Col sm={2}>
                                <Label className="labelInputsStyle">Inicio ingresos</Label>
                                <Col sm={8}>

                                    <Input type="date" className="select" style={{ border: '1px solid #003462' }}>

                                    </Input>
                                </Col>
                            </Col>
                            <Col sm={2}>
                                <Label className="labelInputsStyle">Inicio residencia</Label>
                                <Col sm={8}>

                                    <Input type="date" className="select" style={{ border: '1px solid #003462' }}>

                                    </Input>
                                </Col>
                            </Col>

                        </Row>

                    </FormGroup>




                </Form>

                <div className="containerButtonStyleFooter">
                    <Link to="/clientes/vistaclientes/clientesnaturales">
                        <Button className="buttonStyleFooter"  >Grabar</Button>
                    </Link>
                    <Link to="/clientes/vistaclientes/clientesjuridicos">
                        <Button className="buttonStyleFooter" >Cerrar</Button>
                    </Link>
                </div>
            </div >

        </div >

    )
};
export default Clientesnaturales;