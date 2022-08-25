import React, { Fragment, useState, useEffect } from 'react';
import Select from "react-select";
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
    Alert
} from "reactstrap";
import swal from 'sweetalert';
import Loader from "react-loaders";
import PageTitle from "../../Layout/AppMain/PageTitle";
import ClientInfo from '../../components/ClientInfo';
import ClientMoreInfo from '../../components/ClientMoreInfo';
import { getCatalogos, updateClienteNatural } from '../../Api/apicall_cliente';

/* import { catalogo } from './data';
import { clientNatural } from './data'; */

const Index = () => {

    // statados para almacenar las listas de los catalogos
    const [tipoRolList, setTipoRolList] = useState(null);
    const [tipoProyectoList, setTipoProyectoList] = useState(null);
    const [tipoClaseList, setTipoClaseList] = useState(null);
    const [profesionList, setProfesionList] = useState(null);
    const [nacionalidadList, setNacionalidadList] = useState(null);
    const [actividadEcList, setActividadEcList] = useState(null);
    const [sexoList, setSexoList] = useState(null);
    const [viviendaList, setViviendaList] = useState(null);
    const [estadoCivilList, setEstadoCivilList] = useState(null);
    const [sitLaboralList, setSitLaboralList] = useState(null);
    // estados de utilidad
    const [isOpen, setIsOpen] = useState(false);
    const [loading, setLoading] = useState(false);
    const [error, setError] = useState(false);
    // estado para guardar los datos del formulario
    const [values, setValues] = useState({
        NACI_CODIGO: '',
        ACTI_CODIGO: '',
        CLIE_NOMBRE_CORRESPONDENCIA: "Ratter Bee",
        TIDO_CODIGO: '',
        CLIE_TIPO_PROYECTO: '',

        SEXO_CODIGO: '',
        PROF_CODIGO: '',
        ESCI_CODIGO: '',
        CLNA_NOMBRE1: 'Jonnathan',
        CLNA_NOMBRE2: 'Damian',
        CLNA_APELLIDO1: 'Espinoza',
        CLNA_APELLIDO2: 'Erraez',
        CLNA_FECHA_NACIMIENTO: '',
        CLNA_LUGAR_NACIMIENTO: '',
        CLIE_TIPO_VIVIENDA: '',
        CLIE_SITUACION_LABORAL: '',
        CLNA_EXPIRA_PASAPORTE: '',
        CLNA_INICIO_RESIDENCIA: '',
        CLNA_NUM_CARGAS: '',
        CLNA_EMPRESA_TRABAJA: '',
        CLNA_INICIO_INGRESOS: '',
    });
    /**
     * Estado para almacenar los datos del cliente
     * * El estado debe de guardar los datos que vienen de la busqueda o simplemente utilizar axios
     * TODO: obtener los datos de la busqueda por axios
     */
    const [client, setClient] = useState({
        CLIE_CODIGO: 4578,
        CLIE_IDENTIFICACION: "2367894621",

        "TICL_CODIGO": "N",
        "ASES_CODIGO": 1,
        "CLIE_NOMBRE": "CLEAN BANDIT",
        "TISB_CODIGO": 0,
        "clie_tipo": "C",
        "CLIE_TIPO_ROL": "D",
        NIIN_CODIGO: 1,
        "CLIE_CLAVE": "",
    });

    // Funcion que escucha los cambios en los formularios de los imputs tipo texto y date
    const handleChange = name => event => {
        setValues({ ...values, [name]: event.target.value });
    }

    // Funcion que escucha los cambios en los formularios de los selects
    const handleSelectChange = name => event => {
        setValues({ ...values, [name]: event.value });
    }

    // Funcion para actualizar datos del cliente en la API
    const clickSubmit = e => {
        e.preventDefault();
        swal({
            title: "¿Estas seguro?",
            text: "¡No podrás revertir esto!",
            icon: "info",
            buttons: ["Cancelar", "Si, actualizar!"],
            infoMode: true,
        })
            .then((value) => {
                if (value) {
                    setError(false)
                    setLoading(true)
                    updateClienteNatural(client.CLIE_CODIGO, values)
                        .then(data => {
                            setLoading(false)
                            if (data.status === 400 || data.status === 409) {
                                swal(data.message, {
                                    icon: "error",
                                });
                            } else if (data.status === 200) {
                                swal(data.message, {
                                    icon: "success",
                                });
                            } else {
                                swal("Lo sentimos, hubo un error inesperado. Intente de nuevo.", {
                                    icon: "error",
                                });
                            }
                        }).catch(() => {
                            swal("Lo sentimos, hubo un error inesperado. Intente de nuevo.", {
                                icon: "error",
                            });
                        })
                }
            });
    }

    // Funcionalidad para obtener los datos de catalogos desde la API
    const loadCatalogos = () => {
        getCatalogos().then(res => {
            if (res.error) {
                setError(res.error)
            } else {
                res?.data?.forEach(cat => {
                    if (cat.profesion) setProfesionList(cat.profesion)
                    if (cat.nacionalidad) setNacionalidadList(cat.nacionalidad)
                    if (cat.actividad_economica) setActividadEcList(cat.actividad_economica)
                    if (cat.sexo) setSexoList(cat.sexo)
                    if (cat.vivienda) setViviendaList(cat.vivienda)
                    if (cat.estado_civil) setEstadoCivilList(cat.estado_civil)
                    if (cat.situacion_laboral) setSitLaboralList(cat.situacion_laboral)
                    if (cat.tipo_clase) setTipoClaseList(cat.tipo_clase)
                    if (cat.tipo_proyecto) setTipoProyectoList(cat.tipo_proyecto)
                    if (cat.tipo_rol) setTipoRolList(cat.tipo_rol)
                })
            }
        })
    }

    // Funcion inicializadora
    useEffect(() => {
        loadCatalogos();
    }, []);

    // funcion que retorna la alerta de error
    const showAlert = () => (
        <Alert color="danger">
            {error}
        </Alert>
    )

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

                {error && showAlert()}

                <ClientInfo clientCode={client?.CLIE_CODIGO} typeClient={"NATURAL"} typeIdentification={"CEDULA"} identification={client?.CLIE_IDENTIFICACION} nameClient={values?.CLIE_NOMBRE_CORRESPONDENCIA} className='bg-primary' onChange={handleChange} />

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
                                            <Select
                                                defaultValue={{ value: 2, label: "Colombiana" }}
                                                options={nacionalidadList?.map(item => ({ value: item.NACI_CODIGO, label: item.NACI_DESCRIPCION }))}
                                                onChange={handleSelectChange("NACI_CODIGO")}
                                            />
                                        </Col>
                                    </FormGroup>
                                </Col>
                                <Col md={4}>
                                    <FormGroup row>
                                        <Label for="category" sm={4}>Categoría cliente:</Label>
                                        <Col sm={8}>
                                            <Select
                                                options={tipoProyectoList?.map(item => ({ value: item.COD_TIPO_PROYECTO, label: item.DESC_TIPO_PROYECTO }))}
                                                onChange={handleSelectChange("CLIE_TIPO_PROYECTO")}
                                            />
                                        </Col>
                                    </FormGroup>
                                </Col>
                                <Col md={4}>
                                    <FormGroup row>
                                        <Label for="state" sm={4}>Estado:</Label>
                                        <Col sm={8}>
                                            <Select
                                                options={tipoClaseList?.map(item => ({ value: item.CLIE_TIPO, label: item.DESC_TIPO }))}
                                                onChange={handleSelectChange("TIDO_CODIGO")}
                                            />
                                        </Col>
                                    </FormGroup>
                                </Col>
                            </Row>
                            <Row>
                                <Col md={4}>
                                    <FormGroup row>
                                        <Label for="economicActivity" sm={4}>Actividad Económica:</Label>
                                        <Col sm={8}>
                                            <Select
                                                options={actividadEcList?.map(item => ({ value: item.ACTI_CODIGO, label: item.ACTI_DESCRIPCION }))}
                                                onChange={handleSelectChange("ACTI_CODIGO")}
                                            />
                                        </Col>
                                    </FormGroup>
                                </Col>
                                <Col md={4}>
                                    <FormGroup row>
                                        <Label for="rol" sm={4}>Tipo rol:</Label>
                                        <Col sm={8}>
                                            <Select
                                                options={tipoRolList?.map(item => ({ value: item.TIRO_CODIGO, label: item.TIROL_DESCRIPCION }))}
                                            />
                                        </Col>
                                    </FormGroup>
                                </Col>
                            </Row>

                            <div className="d-flex align-items-center">
                                <div className="mx-auto">
                                    <Button outline className="mb-2 me-2 btn-icon btn-pill" color="link" onClick={() => setIsOpen(!isOpen)}>
                                        {isOpen
                                            ? <><i className="pe-7s-angle-down btn-icon-wrapper"> </i>Ocultar información</>
                                            : <><i className="pe-7s-angle-right btn-icon-wrapper"> </i>Más Información</>}
                                    </Button>
                                </div>
                            </div>

                            <Row className="d-flex flex-column justify-content-center align-items-center">
                                <Col sm={6}>
                                    <div className="d-flex align-items-center">
                                        <div className="mx-auto">
                                            <ClientMoreInfo isOpen={isOpen} setIsOpen={setIsOpen} />
                                        </div>
                                    </div>
                                </Col>
                            </Row>

                            <Row className='divider'></Row>

                            <Row >
                                <Col md={3}>
                                    <FormGroup row>
                                        <Label for="firstName" sm={4}>Primer nombre:</Label>
                                        <Col sm={8}>
                                            <Input type="text" name="firstName" id="firstName" value={values.CLNA_NOMBRE1} onChange={handleChange('CLNA_NOMBRE1')} />
                                        </Col>
                                    </FormGroup>
                                </Col>
                                <Col md={3}>
                                    <FormGroup row>
                                        <Label for="secondName" sm={4}>Segundo nombre:</Label>
                                        <Col sm={8}>
                                            <Input type="text" name="secondName" id="secondName" value={values.CLNA_NOMBRE2} onChange={handleChange('CLNA_NOMBRE2')} />
                                        </Col>
                                    </FormGroup>
                                </Col>
                                <Col md={3}>
                                    <FormGroup row>
                                        <Label for="firtsName" sm={4}>Primer apellido:</Label>
                                        <Col sm={8}>
                                            <Input type="text" name="firtsName" id="firtsName" value={values.CLNA_APELLIDO1} onChange={handleChange('CLNA_APELLIDO1')} />
                                        </Col>
                                    </FormGroup>
                                </Col>
                                <Col md={3}>
                                    <FormGroup row>
                                        <Label for="secondSurname" sm={4}>Segundo apellido:</Label>
                                        <Col sm={8}>
                                            <Input type="text" name="secondSurname" id="secondSurname" value={values.CLNA_APELLIDO2} onChange={handleChange('CLNA_APELLIDO2')} />
                                        </Col>
                                    </FormGroup>
                                </Col>
                            </Row>
                            <Row>
                                <Col md={3}>
                                    <FormGroup row>
                                        <Label for="sex" sm={4}>Sexo:</Label>
                                        <Col sm={8}>
                                            <Select
                                                options={sexoList?.map(item => ({ value: item.SEXO_CODIGO, label: item.SEXO_DESCRIPCION }))}
                                                onChange={handleSelectChange("SEXO_CODIGO")}
                                            />
                                        </Col>
                                    </FormGroup>
                                </Col>
                                <Col md={3}>
                                    <FormGroup row>
                                        <Label for="profession" sm={4}>Profesion:</Label>
                                        <Col sm={8}>
                                            <Select
                                                options={profesionList?.map(item => ({ value: item.PROF_CODIGO, label: item.PROF_DESCRIPCION }))}
                                                onChange={handleSelectChange("PROF_CODIGO")}
                                            />
                                        </Col>
                                    </FormGroup>
                                </Col>
                                <Col md={3}>
                                    <FormGroup row>
                                        <Label for="maritalStatus" sm={4}>Estado civil:</Label>
                                        <Col sm={8}>
                                            <Select
                                                options={estadoCivilList?.map(item => ({ value: item.ESCI_CODIGO, label: item.ESCI_DESCRIPCION }))}
                                                onChange={handleSelectChange("ESCI_CODIGO")}
                                            />
                                        </Col>
                                    </FormGroup>
                                </Col>
                                <Col md={3}>
                                    <FormGroup row>
                                        <Label for="employmentSituation" sm={4}>Situación laboral:</Label>
                                        <Col sm={8}>
                                            <Select
                                                options={sitLaboralList?.map(item => ({ value: item.SITL_CODIGO, label: item.SITL_DESCRIPCION }))}
                                                onChange={handleSelectChange("CLIE_SITUACION_LABORAL")}
                                            />
                                        </Col>
                                    </FormGroup>
                                </Col>
                            </Row>
                            <Row>
                                <Col md={3}>
                                    <FormGroup row>
                                        <Label for="typeHousing" sm={4}>Tipo de vivienda:</Label>
                                        <Col sm={8}>
                                            <Select
                                                options={viviendaList?.map(item => ({ value: item.VIVI_CODIGO, label: item.VIVI_DESCRIPCION }))}
                                                onChange={handleSelectChange("CLIE_TIPO_VIVIENDA")}
                                            />
                                        </Col>
                                    </FormGroup>
                                </Col>
                                <Col md={3}>
                                    <FormGroup row>
                                        <Label for="placeBirth" sm={4}>Lugar de nacimiento:</Label>
                                        <Col sm={8}>
                                            <Input type="text" name="placeBirth" id="placeBirth" onChange={handleChange('CLNA_LUGAR_NACIMIENTO')} />
                                        </Col>
                                    </FormGroup>
                                </Col>
                                <Col md={3}>
                                    <FormGroup row>
                                        <Label for="numberLoads" sm={4}>Número de cargas:</Label>
                                        <Col sm={8}>
                                            <Input type="number" name="numberLoads" id="numberLoads" onChange={handleChange("CLNA_NUM_CARGAS")} min={0} />
                                        </Col>
                                    </FormGroup>
                                </Col>
                                <Col md={3}>
                                    <FormGroup row>
                                        <Label for="dateBirth" sm={4}>Fecha nacimiento:</Label>
                                        <Col sm={8}>
                                            <Input type="date" name="dateBirth" id="dateBirth" onChange={handleChange('CLNA_FECHA_NACIMIENTO')} />
                                        </Col>
                                    </FormGroup>
                                </Col>
                            </Row>
                            <Row>
                                <Col md={3}>
                                    <FormGroup row>
                                        <Label for="workCompany" sm={4}>Empresa trabajo:</Label>
                                        <Col sm={8}>
                                            <Input type="text" name="workCompany" id="workCompany" onChange={handleChange("CLNA_EMPRESA_TRABAJA")} />
                                        </Col>
                                    </FormGroup>
                                </Col>
                                <Col md={3}>
                                    <FormGroup row>
                                        <Label for="passportExp" sm={4}>Exp. pasaporte:</Label>
                                        <Col sm={8}>
                                            <Input type="date" name="passportExp" id="passportExp" onChange={handleChange("CLNA_EXPIRA_PASAPORTE")} />
                                        </Col>
                                    </FormGroup>
                                </Col>
                                <Col md={3}>
                                    <FormGroup row>
                                        <Label for="homeRevenues" sm={4}>Inicio ingresos:</Label>
                                        <Col sm={8}>
                                            <Input type="date" name="homeRevenues" id="homeRevenues" onChange={handleChange("CLNA_INICIO_INGRESOS")} />
                                        </Col>
                                    </FormGroup>
                                </Col>
                                <Col md={3}>
                                    <FormGroup row>
                                        <Label for="startResidency" sm={4}>Inicio recidencia:</Label>
                                        <Col sm={8}>
                                            <Input type="date" name="startResidency" id="startResidency" onChange={handleChange("CLNA_INICIO_RESIDENCIA")} />
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