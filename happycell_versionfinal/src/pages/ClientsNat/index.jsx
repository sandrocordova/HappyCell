import React, { Fragment, useState, useEffect } from 'react';
import Select from "react-select";
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
        console.log(name)
        console.log(event.target.value)
        //setValues({ ...values, [name]: event.target.value });
    }

    const handleSelectChange = name => event => {
        console.log(name)
        console.log(event.value)
        //setValues({ ...values, [name]: event.value });
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
        /* getCatalogos().then(res => {
            res.data?.forEach(cat => {
                if (cat.profesion) setProfesionList(cat.profesion)
                if (cat.nacionalidad) setNacionalidadList(cat.nacionalidad)
                if (cat.actividad_economica) setActividadEcList(cat.actividad_economica)
                if (cat.sexo) setSexoList(cat.sexo)
                if (cat.vivienda) setViviendaList(cat.vivienda)
                if (cat.estado_civil) setEstadoCivilList(cat.estado_civil)
                if (cat.situacion_laboral) setSitLaboralList(cat.situacion_laboral)
            })
        }) */
        /* 
        ! Eliminar el siguiente forEach, es solo para trabajar con mock. Utilizar la funcion de arriba
        */
        catalogo?.forEach(cat => {
            if (cat.profesion) setProfesionList(cat.profesion)
            if (cat.nacionalidad) setNacionalidadList(cat.nacionalidad)
            if (cat.actividad_economica) setActividadEcList(cat.actividad_economica)
            if (cat.sexo) setSexoList(cat.sexo)
            if (cat.vivienda) setViviendaList(cat.vivienda)
            if (cat.estado_civil) setEstadoCivilList(cat.estado_civil)
            if (cat.situacion_laboral) setSitLaboralList(cat.situacion_laboral)
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
                                            <Select
                                                options={nacionalidadList?.map(item => ({ value: item.NACI_CODIGO, label: item.NACI_DESCRIPCION }))}
                                                onChange={handleSelectChange("nacionalidad")}
                                            />
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
                                            <Select
                                                options={actividadEcList?.map(item => ({ value: item.ACTI_CODIGO, label: item.ACTI_DESCRIPCION }))}
                                                onChange={handleSelectChange("actividadEconomica")}
                                            />
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
                                <Col sm={4}>
                                    <div className="d-flex align-items-center">
                                        <div className="mx-auto">
                                            <Collapse isOpen={isOpen}>
                                                <Card className='no-shadow border'>
                                                    <CardBody>
                                                        <Row>
                                                            <Col md={12} className="mb-2 d-flex justify-content-between">
                                                                <span className='fw-bold text-black-50 me-1'>Atraso promedio:</span>
                                                                <span>123</span>
                                                            </Col>
                                                            <Col md={12} className="mb-2 d-flex justify-content-between">
                                                                <span className='fw-bold text-black-50 me-1'>Atraso máximo:</span>
                                                                <span>123</span>
                                                            </Col>
                                                            <Col md={12} className="mb-2 d-flex justify-content-between">
                                                                <span className='fw-bold text-black-50 me-1'>N° de pagos totales:</span>
                                                                <span>123</span>
                                                            </Col>
                                                            <Col md={12} className="mb-2 d-flex justify-content-between">
                                                                <span className='fw-bold text-black-50 me-1'>Años de antiguedad:</span> <span>123</span>
                                                            </Col>
                                                            <Col md={12} className="mb-2 d-flex justify-content-between">
                                                                <span className='fw-bold text-black-50 me-1'>N° de operaciones vigentes:</span> <span>123</span>
                                                            </Col>
                                                            <Col md={12} className="mb-2 d-flex justify-content-between">
                                                                <span className='fw-bold text-black-50 me-1'>N° de operaciones canceladas:</span> <span>123</span>
                                                            </Col>
                                                            <Col md={12} className="mb-2 d-flex justify-content-between">
                                                                <span className='fw-bold text-black-50 me-1'>Cupo utilizado:</span> <span>123</span>
                                                            </Col>
                                                            <Col md={12} className="mb-2 d-flex justify-content-between">
                                                                <span className='fw-bold text-black-50 me-1'>Cupo utilizado:</span> <span>123</span>
                                                            </Col>
                                                        </Row>
                                                        <Row>
                                                            <Button outline className="mb-2 me-2 btn-icon btn-pill" color="link" onClick={() => setIsOpen(!isOpen)}>
                                                                <i className="pe-7s-angle-up btn-icon-wrapper"> </i>
                                                                Ocultar información
                                                            </Button>
                                                        </Row>
                                                    </CardBody>
                                                </Card>
                                            </Collapse>
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
                                            <Select
                                                options={sexoList?.map(item => ({ value: item.SEXO_CODIGO, label: item.SEXO_DESCRIPCION }))}
                                                onChange={handleSelectChange("sexo")}
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
                                                onChange={handleSelectChange("profesion")}
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
                                                onChange={handleSelectChange("estadoCivil")}
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
                                                onChange={handleSelectChange("situacionLaboral")}
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
                                                onChange={handleSelectChange("tipoVivienda")}
                                            />
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