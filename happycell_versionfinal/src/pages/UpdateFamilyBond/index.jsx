import React, { Fragment, useState, useEffect } from 'react';
import PageTitle from "../../Layout/AppMain/PageTitle";
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
import ClientInfo from '../../components/ClientInfo';
import { getCatalogos, updateVinculos } from '../../Api/apicall_cliente';

const Index = () => {

    // estatados para almacenar las listas de los catalogos
    const [tipoVinculoList, setTipoVinculoList] = useState(null);
    const [profesionList, setProfesionList] = useState(null);
    const [nacionalidadList, setNacionalidadList] = useState(null);
    const [estadoCivilList, setEstadoCivilList] = useState(null);
    // estados de utilidad
    const [loading, setLoading] = useState(false);
    const [error, setError] = useState(false);
    // estado para guardar los datos del formulario
    // ! los datos por defecto deben de ser remplazados, y extraerlos de la busqueda
    const [values, setValues] = useState({
        VINC_CODIGO: 1,
        TIVI_CODIGO: 1,
        VINC_IDENTIFICACION: "1029381723",
        VINC_NOMBRE: "AFRO JACK",
        VINC_DIRECCION: "LOST SANTOS CA",
        VINC_TELEFONO: "9918282992",
        NACI_CODIGO: 1,
        PROF_CODIGO: 2,
        CIUD_CODIGO: 1,
        VINC_CARGO: "LOREM",
        esci_codigo: 1,
    });
    /**
     * Estado para almacenar los datos del cliente
     * * El estado debe de guardar los datos que vienen de la busqueda o simplemente utilizar axios
     * TODO: obtener los datos de la busqueda por axios
     */
    const [client, setClient] = useState({
        CLIE_CODIGO: 4578,
        CLIE_IDENTIFICACION: "2367894621",
        CLIE_NOMBRE_CORRESPONDENCIA: "Ratter Bee",
        TICL_CODIGO: "N"
    });

    // Funcion que escucha los cambios en los formularios de los imputs tipo texto y date
    const handleChange = name => event => {
        setValues({ ...values, [name]: event.target.value });
    }

    // TODO: implementar el handle select en el tipo de telefono
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
                    const datos = { CLIE_CODIGO: client.CLIE_CODIGO, TICL_CODIGO: client.TICL_CODIGO, vinculos: [values] }
                    updateVinculos(datos)
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
                    if (cat.estado_civil) setEstadoCivilList(cat.estado_civil)
                    if (cat.tipo_vinculo) setTipoVinculoList(cat.tipo_vinculo)
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
                heading="Mantenimiento de Vínculos"
                icon="lnr-users icon-gradient bg-tempting-azure"
            />

            <Container fluid>

                {error && showAlert()}

                <ClientInfo clientCode={"0978374"} typeClient={"NATURAL"} typeIdentification={"CEDULA"} identification={"1111111112"} nameClient={"ojdflakdflaksdflkasf"}>
                    <Row>
                        <Col md={2}>
                            <FormGroup>
                                <Label for="sequence">Código vínculo:</Label>
                                <Input type="text" name="sequence" id="sequence" value={"1"} disabled />
                            </FormGroup>
                        </Col>
                    </Row>
                </ClientInfo>

                <Card className="mt-4 mb-4">
                    <CardBody>
                        <Form>
                            <Row>
                                <Col md={4}>
                                    <FormGroup>
                                        <Label for="bondType">Tipo de vínculo:</Label>
                                        <Col>
                                            <Select
                                                options={tipoVinculoList?.map(item => ({ value: item.TIVI_CODIGO, label: item.TIVI_DESCRIPCION }))}
                                                onChange={handleSelectChange("TIVI_CODIGO")}
                                            />
                                        </Col>
                                    </FormGroup>
                                </Col>
                                <Col md={4}>
                                    <FormGroup>
                                        <Label for="identification">Identificación:</Label>
                                        <Col>
                                            <Input type="text" id="identification" name="identification" onChange={handleChange("VINC_IDENTIFICACION")} />
                                        </Col>
                                    </FormGroup>
                                </Col>
                                <Col md={4}>
                                    <FormGroup>
                                        <Label for="bondName">Nombre de vínculo:</Label>
                                        <Col>
                                            <Input type="text" id="bondName" name="bondName" onChange={handleChange("VINC_NOMBRE")} />
                                        </Col>
                                    </FormGroup>
                                </Col>
                            </Row>
                            <Row>
                                <Col md={8}>
                                    <FormGroup>
                                        <Label for="adress">Dirección:</Label>
                                        <Col>
                                            <Input type="text" id="adress" name="adress" onChange={handleChange("VINC_DIRECCION")} />
                                        </Col>
                                    </FormGroup>
                                </Col>
                                <Col md={4}>
                                    <FormGroup>
                                        <Label for="phone">Teléfono:</Label>
                                        <Col>
                                            <Input type="text" id="phone" name="phone" onChange={handleChange("VINC_TELEFONO")} />
                                        </Col>
                                    </FormGroup>
                                </Col>
                            </Row>
                            <Row>
                                <Col md={4}>
                                    <FormGroup>
                                        <Label for="nationality">Nacionalidad:</Label>
                                        <Col>
                                            <Select
                                                options={nacionalidadList?.map(item => ({ value: item.NACI_CODIGO, label: item.NACI_DESCRIPCION }))}
                                                onChange={handleSelectChange("NACI_CODIGO")}
                                            />
                                        </Col>
                                    </FormGroup>
                                </Col>
                                <Col md={4}>
                                    <FormGroup>
                                        <Label for="maritalStatus">Estado civil:</Label>
                                        <Col>
                                            <Select
                                                options={estadoCivilList?.map(item => ({ value: item.ESCI_CODIGO, label: item.ESCI_DESCRIPCION }))}
                                                onChange={handleSelectChange("esci_codigo")}
                                            />
                                        </Col>
                                    </FormGroup>
                                </Col>
                                <Col md={4}>
                                    <FormGroup>
                                        <Label for="profession">Profesión:</Label>
                                        <Col>
                                            <Select
                                                options={profesionList?.map(item => ({ value: item.PROF_CODIGO, label: item.PROF_DESCRIPCION }))}
                                                onChange={handleSelectChange("PROF_CODIGO")}
                                            />
                                        </Col>
                                    </FormGroup>
                                </Col>
                            </Row>
                            <Row>
                                <Col md={8}>
                                    <FormGroup>
                                        <Label for="jobTitle">Cargo:</Label>
                                        <Col>
                                            <Input type="text" id="jobTitle" name="jobTitle" onChange={handleChange("VINC_CARGO")} />
                                        </Col>
                                    </FormGroup>
                                </Col>
                                <Col md={4}>
                                    <FormGroup>
                                        <Label for="city">Ciudad:</Label>
                                        <Col>
                                            <Input type="select" id="city" name="city">
                                                <option value="">Select</option>
                                            </Input>
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
