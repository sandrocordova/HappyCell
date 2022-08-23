import React, { Fragment, useState, useEffect } from 'react';
// import {
//     useParams
// } from "react-router-dom";
import {
    Row,
    Col,
    Button,
    Container,
    Card,
    CardBody,
    Input,
    FormGroup,
    Label,
    Modal,
    Form,
    Collapse
} from "reactstrap";
import { catalogo } from './data';
import swal from 'sweetalert';
import Loader from "react-loaders";
import PageTitle from "../../Layout/AppMain/PageTitle";
import ClientInfo from '../../components/ClientInfo';
import { getCatalogos } from '../../Api/apicall_cliente';

const Index = () => {

    /**
     * TODO: crear el metodo fecht para actualizar datos
     */
    //let { id } = useParams();

    // state
    const [profesionList, setProfesionList] = useState(null);
    const [nacionalidadList, setNacionalidadList] = useState(null);
    const [actividadEcList, setActividadEcList] = useState(null);
    const [sexoList, setSexoList] = useState(null);
    const [viviendaList, setViviendaList] = useState(null);
    const [estadoCivilList, setEstadoCivilList] = useState(null);
    const [sitLaboralList, setSitLaboralList] = useState(null);
    const [isOpen, setIsOpen] = useState(false);
    const [loading, setLoading] = useState(false);
    // const [error, setError] = useState(false);
    const [values, setValues] = useState({
        nombreComercial: '',
        nacionalidad: '',
        categoriaCliente: '',
        estado: '',
        actividadEconomica: '',
        tipoRol: '',
        primerNombre: '',
        segundoNombre: '',
        primerApellido: '',
        segundoApellido: '',
        sexo: '',
        profesion: '',
        estadoCivil: '',
        situacionLaboral: '',
        tipoVivienda: '',
        lugarNacimiento: '',
        numeroCrgas: '',
        fechaNacimiento: '',
        empresaTrabajo: '',
        expPadaporte: '',
        inicioIngresos: '',
        inicioResidencia: '',
    });

    // Funcion que escucha los cambios en los formularios
    const handleChange = name => event => {
        setValues({ ...values, [name]: event.target.value });
    }

    // Funcion para actualizar datos del cliente en la API
    const clickSubmit = e => {
        e.preventDefault();
        //setValues({ ...values, error: false });
        swal({
            title: "¿Estas seguro?",
            text: "¡No podrás revertir esto!",
            icon: "info",
            buttons: ["Cancelar", "Si, actualizar!"],
            infoMode: true,
        })
            .then((value) => {
                if (value) {
                    setLoading(true)
                    // console.log("DATA")
                    // console.log(values)
                    setTimeout(function () {
                        setLoading(false)
                        swal("Actualización completada con éxito!", {
                            icon: "success",
                        });
                    }, 2000);
                }
            });
    }

    // Funcionalidad para obtener los datos de catalogos desde la API
    const loadCatalogos = () => {
        getCatalogos().then(res => {
            res.data?.forEach(cat => {
                if (cat.profesion) setProfesionList(cat.profesion)
                if (cat.nacionalidad) setNacionalidadList(cat.nacionalidad)
                if (cat.actividad_economica) setActividadEcList(cat.actividad_economica)
                if (cat.sexo) setSexoList(cat.sexo)
                if (cat.vivienda) setViviendaList(cat.vivienda)
                if (cat.estado_civil) setEstadoCivilList(cat.estado_civil)
                if (cat.situacion_laboral) setSitLaboralList(cat.situacion_laboral)
            })
        })
    }

    // Funcion inicializadora
    useEffect(() => {
        loadCatalogos();
    }, []);

    return (
        <Fragment>

            <Modal isOpen={loading} backdrop={'static'} centered className='shadow-none text-center' contentClassName={"bg-transparent shadow-none border border-0"}>
                <Loader type="ball-pulse" />
            </Modal>

            <PageTitle
                heading="Mantenimiento de Cliente Natural"
                icon="lnr-user icon-gradient bg-tempting-azure"
            />

            <Container fluid>

                <ClientInfo clientCode={"0978374"} typeClient={"NATURAL"} typeIdentification={"CEDULA"} identification={"1111111112"} nameClient={"ojdflakdflaksdflkasf"} className='bg-primary' />

                {/* <div className="card no-shadow rm-border bg-transparent widget-chart text-start mb-1">
                    Opciones
                </div> */}

                <Card className="mt-4 mb-4">
                    <CardBody>
                        <Form>
                            <Row>
                                <Col md={4}>
                                    <FormGroup row>
                                        <Label for="nationality" sm={4}>Nacionalidad</Label>
                                        <Col sm={8}>
                                            <Input type="select" id="nationality" name="nationality">
                                                <option value="">Select</option>
                                                {nacionalidadList?.map((data, i) => (
                                                    <option key={i} value={data.NACI_CODIGO}>
                                                        {data.NACI_DESCRIPCION}
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
                                                {/* <option>Value 1</option> */}
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
                                                {/* {catalogo[5]?.estado_civil?.map((data, i) => (
                                                    <option key={i} value={data.sci_codigo}>
                                                        {data.sci_descripcion}
                                                    </option>
                                                ))} */}
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
                                                {actividadEcList?.map((data, i) => (
                                                    <option key={i} value={data.ACTI_CODIGO}>
                                                        {data.ACTI_DESCRIPCION}
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
                                                {/* <option>Value 1</option> */}
                                            </Input>
                                        </Col>
                                    </FormGroup>
                                </Col>
                            </Row>

                            <Row>
                                <Collapse isOpen={isOpen}>
                                    <Card className='no-shadow border'>
                                        <CardBody>
                                            <Row>
                                                <Col md={4} className="mb-2">
                                                    <span className='fw-bold text-black-50 me-1'>Atraso promedio:</span>
                                                    <span>123</span>
                                                </Col>
                                                <Col md={4} className="mb-2">
                                                    <span className='fw-bold text-secondary me-1'>Atraso máximo:</span>
                                                    <span>123</span>
                                                </Col>
                                                <Col md={4} className="mb-2">
                                                    <span className='fw-bold text-secondary me-1'>N° de pagos totales:</span>
                                                    <span>123</span>
                                                </Col>
                                            </Row>
                                            <Row>
                                                <Col md={4} className="mb-2">
                                                    <span className='fw-bold text-secondary me-1'>Años de antiguedad:</span> <span>123</span>
                                                </Col>
                                            </Row>
                                            <Row>
                                                <Col md={4} className="mb-2">
                                                    <span className='fw-bold text-secondary me-1'>N° de operaciones vigentes:</span> <span>123</span>
                                                </Col>
                                                <Col md={4} className="mb-2">
                                                    <span className='fw-bold text-secondary me-1'>N° de operaciones canceladas:</span> <span>123</span>
                                                </Col>
                                                <Col md={4} className="mb-2">
                                                    <span className='fw-bold text-secondary me-1'>Cupo utilizado:</span> <span>123</span>
                                                </Col>
                                            </Row>
                                        </CardBody>
                                    </Card>
                                </Collapse>
                                <Row className="d-flex flex-column justify-content-center align-items-center">
                                    <div className="d-flex align-items-center">
                                        <div className="mx-auto">
                                            <Button outline className="mb-2 mt-2 me-2 btn-outline-2x btn-square" color="secondary" onClick={() => setIsOpen(!isOpen)}>
                                                {isOpen ? "Ocultar información" : "Más Información"}
                                            </Button>
                                        </div>
                                    </div>
                                </Row>
                            </Row>

                            <Row className='divider'></Row>

                            <Row >
                                <Col md={3}>
                                    <FormGroup row>
                                        <Label for="firstName" sm={4}>Primer nombre:</Label>
                                        <Col sm={8}>
                                            <Input type="text" name="firstName" id="firstName" value={values.primerNombre} onChange={handleChange('primerNombre')} />
                                        </Col>
                                    </FormGroup>
                                </Col>
                                <Col md={3}>
                                    <FormGroup row>
                                        <Label for="secondName" sm={4}>Segundo nombre:</Label>
                                        <Col sm={8}>
                                            <Input type="text" name="secondName" id="secondName" value={values.segundoNombre} onChange={handleChange('segundoNombre')} />
                                        </Col>
                                    </FormGroup>
                                </Col>
                                <Col md={3}>
                                    <FormGroup row>
                                        <Label for="firtsName" sm={4}>Primer apellido:</Label>
                                        <Col sm={8}>
                                            <Input type="text" name="firtsName" id="firtsName" value={values.primerApellido} onChange={handleChange('primerApellido')} />
                                        </Col>
                                    </FormGroup>
                                </Col>
                                <Col md={3}>
                                    <FormGroup row>
                                        <Label for="secondSurname" sm={4}>Segundo apellido:</Label>
                                        <Col sm={8}>
                                            <Input type="text" name="secondSurname" id="secondSurname" value={values.segundoApellido} onChange={handleChange('segundoApellido')} />
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
                                                {sexoList?.map((data, i) => (
                                                    <option key={i} value={data.SEXO_CODIGO}>
                                                        {data.SEXO_DESCRIPCION}
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
                                                {profesionList?.map((data, i) => (
                                                    <option key={i} value={data.PROF_CODIGO}>
                                                        {data.PROF_DESCRIPCION}
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
                                                {estadoCivilList?.map((data, i) => (
                                                    <option key={i} value={data.ESCI_CODIGO}>
                                                        {data.ESCI_DESCRIPCION}
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
                                                {sitLaboralList?.map((data, i) => (
                                                    <option key={i} value={data.SITL_CODIGO}>
                                                        {data.SITL_DESCRIPCION}
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
                                                {viviendaList?.map((data, i) => (
                                                    <option key={i} value={data.VIVI_CODIGO}>
                                                        {data.VIVI_DESCRIPCION}
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
                                            <Input type="text" name="placeBirth" id="placeBirth" />
                                        </Col>
                                    </FormGroup>
                                </Col>
                                <Col md={3}>
                                    <FormGroup row>
                                        <Label for="numberLoads" sm={4}>Número de cargas:</Label>
                                        <Col sm={8}>
                                            <Input type="number" name="numberLoads" id="numberLoads" />
                                        </Col>
                                    </FormGroup>
                                </Col>
                                <Col md={3}>
                                    <FormGroup row>
                                        <Label for="dateBirth" sm={4}>Fecha nacimiento:</Label>
                                        <Col sm={8}>
                                            <Input type="date" name="dateBirth" id="dateBirth" />
                                        </Col>
                                    </FormGroup>
                                </Col>
                            </Row>
                            <Row>
                                <Col md={3}>
                                    <FormGroup row>
                                        <Label for="workCompany" sm={4}>Empresa trabajo:</Label>
                                        <Col sm={8}>
                                            <Input type="text" name="workCompany" id="workCompany" />
                                        </Col>
                                    </FormGroup>
                                </Col>
                                <Col md={3}>
                                    <FormGroup row>
                                        <Label for="passportExp" sm={4}>Exp. pasaporte:</Label>
                                        <Col sm={8}>
                                            <Input type="date" name="passportExp" id="passportExp" />
                                        </Col>
                                    </FormGroup>
                                </Col>
                                <Col md={3}>
                                    <FormGroup row>
                                        <Label for="homeRevenues" sm={4}>Inicio ingresos:</Label>
                                        <Col sm={8}>
                                            <Input type="date" name="homeRevenues" id="homeRevenues" />
                                        </Col>
                                    </FormGroup>
                                </Col>
                                <Col md={3}>
                                    <FormGroup row>
                                        <Label for="startResidency" sm={4}>Inicio recidencia:</Label>
                                        <Col sm={8}>
                                            <Input type="date" name="startResidency" id="startResidency" />
                                        </Col>
                                    </FormGroup>
                                </Col>
                            </Row>
                            <Row className="d-flex flex-column justify-content-center align-items-center">
                                <div className="d-flex align-items-center">
                                    <div className="mx-auto">
                                        <Button onClick={clickSubmit} color="primary" className="mt-2" size="lg">
                                            Grabar
                                        </Button>
                                    </div>
                                </div>
                            </Row>
                        </Form>
                    </CardBody>
                </Card>
            </Container>
        </Fragment>
    );
}

export default Index;