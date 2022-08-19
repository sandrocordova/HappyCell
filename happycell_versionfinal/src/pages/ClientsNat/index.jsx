import React, { Fragment, useState } from 'react';
import {
    useParams
} from "react-router-dom";
import PageTitle from "../../Layout/AppMain/PageTitle";
/**
 * ! eliminar librerias que no se utilize
 */
import {
    Row,
    Col,
    Button,
    CardHeader,
    Container,
    Card,
    CardBody,
    Progress,
    ListGroup,
    ListGroupItem,
    CardFooter,
    Input,
    Dropdown,
    DropdownItem,
    DropdownToggle,
    DropdownMenu,
    UncontrolledButtonDropdown,
    Form,
    FormGroup,
    Label
} from "reactstrap";
import { catalogo } from './data';

const Index = () => {

    /**
     * TODO: crear la funcionalidad de obtener datos del cliente y asignarlos a los estados
     * Important para asignar los valores por defecto en los inpus, utilizar: 
     *      value={values.CLIE_NOMBRE} onChange={handleChange('CLIE_NOMBRE')}
     * TODO: crear el componente de spinner para el loading de los datos
     * TODO: crear el componente de las alertas
     * TODO: crear el metodo fecht a la a api
     */
    let { id } = useParams();

    // state
    const [loading, setLoading] = useState(false);
    const [error, setError] = useState(false);
    const [success, setSuccess] = useState(false);
    const [values, setValues] = useState({
        NACI_CODIGO: '',
        TICL_CODIGO: '',
        TIDO_CODIGO: '',
        ACTI_CODIGO: '',
        ASES_CODIGO: '',
        CLIE_NOMBRE: 'Jonnathan',
        CLIE_FECHA_CREACION: '',
        CLIE_NOMBRE_CORRESPONDENCIA: '',
        clie_estado: '',
        TISB_CODIGO: '',
        clie_tipo: '',
        CLIE_CLAVE: '',
        CLIE_TIPO_ROL: '',
        CLIE_TIPO_PROYECTO: '',
        comodin: '',
        ASES: '',
        CLIE_FECHA_INACTIVACION: '',
        CLIE_FECHA_DESAFILIACION: '',
        sect_codigo: '',
        pais_codigo: '',
        prov_codigo: '',
        cant_codigo: '',
        parr_codigo: '',
    });

    const { TIDO_CODIGO, CLIE_NOMBRE } = values;

    console.log(TIDO_CODIGO)
    console.log(CLIE_NOMBRE)

    const handleChange = name => event => {
        setValues({ ...values, [name]: event.target.value });
    }

    const clickSubmit = e => {
        e.preventDefault();
        //setValues({ ...values, error: false });
        console.log("DATA")
        console.log(values)
    }

    return (
        <Fragment>
            <PageTitle
                heading="Mantenimiento de Cliente Natural"
                icon="pe-7s-graph text-success"
            />
            <Container fluid>

                <div className="card no-shadow rm-border  widget-chart text-start mb-2">
                    <CardBody>
                        <Row>
                            <Col md={2}>
                                <FormGroup>
                                    <Label for="clientCode">Código cliente:</Label>
                                    <Input type="text" name="clientCode" id="clientCode" placeholder="2654" />
                                </FormGroup>
                            </Col>
                            <Col md={2}>
                                <FormGroup>
                                    <Label for="clientTipe">Tipo:</Label>
                                    <Input type="select" onChange={handleChange('TIDO_CODIGO')} id="clientTipe" name="clientTipe" defaultValue={"DEFAULT"}>
                                        <option value="SELECT" selected>Select</option>
                                        <option value="UNO">Value 1</option>
                                    </Input>
                                </FormGroup>
                            </Col>
                            <Col md={3}>
                                <FormGroup>
                                    <Label for="typeIdentification">Tipo de identificación:</Label>
                                    <Input type="select" id="typeIdentification" name="typeIdentification" onChange={handleChange('TIDO_CODIGO')}>
                                        <option value="">Select</option>
                                        <option>Value 1</option>
                                    </Input>
                                </FormGroup>
                            </Col>
                            <Col md={2}>
                                <FormGroup>
                                    <Label for="identification">Identificación:</Label>
                                    <Input type="text" name="identification" id="identification" placeholder="" />
                                </FormGroup>
                            </Col>
                            <Col md={3}>
                                <FormGroup>
                                    <Label for="clientName">Nombre:</Label>
                                    <Input type="text" onChange={handleChange('name')} name="clientName" id="clientName" placeholder="" />
                                </FormGroup>
                            </Col>
                        </Row>
                    </CardBody>
                </div>

                <div className="card no-shadow rm-border bg-transparent widget-chart text-start mb-1">
                    Opciones
                </div>

                <Card className="mb-3">
                    <CardBody>
                        <Row>
                            <Col md={4}>
                                <FormGroup row>
                                    <Label for="nationality" sm={4}>Nacionalidad</Label>
                                    <Col sm={8}>
                                        <Input type="select" id="nationality" name="nationality">
                                            <option value="">Select</option>
                                            {catalogo[1]?.nacionalidad?.map((data, i) => (
                                                <option key={i} value={data.naci_codigo}>
                                                    {data.naci_descripcion}
                                                </option>
                                            ))}
                                        </Input>
                                    </Col>
                                </FormGroup>
                            </Col>
                            <Col md={4}>
                                <FormGroup row>
                                    <Label for="category" sm={4}>Categoría cliente:</Label>
                                    <Col sm={8}>
                                        <Input type="select" id="category" name="category">
                                            <option value="">Select</option>
                                            <option>Value 1</option>
                                            <option>Value 2</option>
                                            <option>Value 3</option>
                                            <option>Value 4</option>
                                            <option>Value 5</option>
                                        </Input>
                                    </Col>
                                </FormGroup>
                            </Col>
                            <Col md={4}>
                                <FormGroup row>
                                    <Label for="state" sm={4}>Estado:</Label>
                                    <Col sm={8}>
                                        <Input type="select" id="state" name="state">
                                            <option value="">Select</option>
                                            {catalogo[5]?.estado_civil?.map((data, i) => (
                                                <option key={i} value={data.sci_codigo}>
                                                    {data.sci_descripcion}
                                                </option>
                                            ))}
                                        </Input>
                                    </Col>
                                </FormGroup>
                            </Col>
                        </Row>
                        <Row>
                            <Col md={4}>
                                <FormGroup row>
                                    <Label for="economicActivity" sm={4}>Actividad Económica:</Label>
                                    <Col sm={8}>
                                        <Input type="select" id="economicActivity" name="economicActivity">
                                            <option value="">Select</option>
                                            {catalogo[2]?.actividad_economica?.map((data, i) => (
                                                <option key={i} value={data.acti_codigo}>
                                                    {data.acti_descripcion}
                                                </option>
                                            ))}
                                        </Input>
                                    </Col>
                                </FormGroup>
                            </Col>
                            <Col md={4}>
                                <FormGroup row>
                                    <Label for="rol" sm={4}>Tipo rol:</Label>
                                    <Col sm={8}>
                                        <Input type="select" id="rol" name="rol">
                                            <option value="">Select</option>
                                            <option>Value 1</option>
                                            <option>Value 2</option>
                                            <option>Value 3</option>
                                            <option>Value 4</option>
                                            <option>Value 5</option>
                                        </Input>
                                    </Col>
                                </FormGroup>
                            </Col>
                        </Row>

                        <hr className="bg-secondary border-2 border-top border-secondary"></hr>

                        <Row>
                            <Col md={3}>
                                <FormGroup row>
                                    <Label for="firstName" sm={4}>Primer nombre:</Label>
                                    <Col sm={8}>
                                        <Input type="text" name="firstName" id="firstName" value={values.CLIE_NOMBRE} onChange={handleChange('CLIE_NOMBRE')} />
                                    </Col>
                                </FormGroup>
                            </Col>
                            <Col md={3}>
                                <FormGroup row>
                                    <Label for="secondName" sm={4}>Segundo nombre:</Label>
                                    <Col sm={8}>
                                        <Input type="text" name="secondName" id="secondName" placeholder="with a placeholder" />
                                    </Col>
                                </FormGroup>
                            </Col>
                            <Col md={3}>
                                <FormGroup row>
                                    <Label for="firtsName" sm={4}>Primer apellido:</Label>
                                    <Col sm={8}>
                                        <Input type="text" name="firtsName" id="firtsName" placeholder="with a placeholder" />
                                    </Col>
                                </FormGroup>
                            </Col>
                            <Col md={3}>
                                <FormGroup row>
                                    <Label for="secondSurname" sm={4}>Segundo apellido:</Label>
                                    <Col sm={8}>
                                        <Input type="text" name="secondSurname" id="secondSurname" placeholder="with a placeholder" />
                                    </Col>
                                </FormGroup>
                            </Col>
                        </Row>
                        <Row>
                            <Col md={3}>
                                <FormGroup row>
                                    <Label for="sex" sm={4}>Sexo:</Label>
                                    <Col sm={8}>
                                        <Input type="select" id="sex" name="sex">
                                            <option value="">Select</option>
                                            {catalogo[3]?.sexo?.map((data, i) => (
                                                <option key={i} value={data.sexo_codigo}>
                                                    {data.sexo_descripcion}
                                                </option>
                                            ))}
                                        </Input>
                                    </Col>
                                </FormGroup>
                            </Col>
                            <Col md={3}>
                                <FormGroup row>
                                    <Label for="profession" sm={4}>Profesion:</Label>
                                    <Col sm={8}>
                                        <Input type="select" id="profession" name="profession">
                                            <option value="">Select</option>
                                            {catalogo[0]?.profesion?.map((data, i) => (
                                                <option key={i} value={data.prof_codigo}>
                                                    {data.prof_descripcion}
                                                </option>
                                            ))}
                                        </Input>
                                    </Col>
                                </FormGroup>
                            </Col>
                            <Col md={3}>
                                <FormGroup row>
                                    <Label for="maritalStatus" sm={4}>Estado civil:</Label>
                                    <Col sm={8}>
                                        <Input type="select" id="maritalStatus" name="maritalStatus">
                                            <option value="">Select</option>
                                            {catalogo[5]?.estado_civil?.map((data, i) => (
                                                <option key={i} value={data.sci_codigo}>
                                                    {data.sci_descripcion}
                                                </option>
                                            ))}
                                        </Input>
                                    </Col>
                                </FormGroup>
                            </Col>
                            <Col md={3}>
                                <FormGroup row>
                                    <Label for="employmentSituation" sm={4}>Situación laboral:</Label>
                                    <Col sm={8}>
                                        <Input type="select" id="employmentSituation" name="employmentSituation">
                                            <option value="">Select</option>
                                            {catalogo[6]?.situacion_laboral?.map((data, i) => (
                                                <option key={i} value={data.sitl_codigo}>
                                                    {data.sitl_descripcion}
                                                </option>
                                            ))}
                                        </Input>
                                    </Col>
                                </FormGroup>
                            </Col>
                        </Row>
                        <Row>
                            <Col md={3}>
                                <FormGroup row>
                                    <Label for="typeHousing" sm={4}>Tipo de vivienda:</Label>
                                    <Col sm={8}>
                                        <Input type="select" id="typeHousing" name="typeHousing">
                                            <option value="">Select</option>
                                            {catalogo[4]?.vivienda?.map((data, i) => (
                                                <option key={i} value={data.vivi_codigo}>
                                                    {data.vivi_descripcion}
                                                </option>
                                            ))}
                                        </Input>
                                    </Col>
                                </FormGroup>
                            </Col>
                            <Col md={3}>
                                <FormGroup row>
                                    <Label for="placeBirth" sm={4}>Lugar de nacimiento:</Label>
                                    <Col sm={8}>
                                        <Input type="text" name="placeBirth" id="placeBirth" placeholder="with a placeholder" />
                                    </Col>
                                </FormGroup>
                            </Col>
                            <Col md={3}>
                                <FormGroup row>
                                    <Label for="numberLoads" sm={4}>Número de cargas:</Label>
                                    <Col sm={8}>
                                        <Input type="text" name="numberLoads" id="numberLoads" placeholder="with a placeholder" />
                                    </Col>
                                </FormGroup>
                            </Col>
                            <Col md={3}>
                                <FormGroup row>
                                    <Label for="dateBirth" sm={4}>Fecha nacimiento:</Label>
                                    <Col sm={8}>
                                        <Input type="date" name="dateBirth" id="dateBirth" placeholder="with a placeholder" />
                                    </Col>
                                </FormGroup>
                            </Col>
                        </Row>
                        <Row>
                            <Col md={3}>
                                <FormGroup row>
                                    <Label for="workCompany" sm={4}>Empresa trabajo:</Label>
                                    <Col sm={8}>
                                        <Input type="text" name="workCompany" id="workCompany" placeholder="with a placeholder" />
                                    </Col>
                                </FormGroup>
                            </Col>
                            <Col md={3}>
                                <FormGroup row>
                                    <Label for="passportExp" sm={4}>Exp. pasaporte:</Label>
                                    <Col sm={8}>
                                        <Input type="date" name="passportExp" id="passportExp" placeholder="with a placeholder" />
                                    </Col>
                                </FormGroup>
                            </Col>
                            <Col md={3}>
                                <FormGroup row>
                                    <Label for="homeRevenues" sm={4}>Inicio ingresos:</Label>
                                    <Col sm={8}>
                                        <Input type="date" name="homeRevenues" id="homeRevenues" placeholder="with a placeholder" />
                                    </Col>
                                </FormGroup>
                            </Col>
                            <Col md={3}>
                                <FormGroup row>
                                    <Label for="startResidency" sm={4}>Inicio recidencia:</Label>
                                    <Col sm={8}>
                                        <Input type="date" name="startResidency" id="startResidency" placeholder="with a placeholder" />
                                    </Col>
                                </FormGroup>
                            </Col>
                        </Row>
                    </CardBody>
                </Card>

                <div className="card no-shadow rm-border bg-transparent widget-chart text-start mb-1">
                    <Button onClick={clickSubmit} color="primary" className="mt-2">
                        Grabar
                    </Button>
                </div>
            </Container>
        </Fragment>
    );
}

export default Index;