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
    Form
} from "reactstrap";
import swal from 'sweetalert';
import Loader from "react-loaders";
import ClientInfo from '../../components/ClientInfo';
import { getCatalogos, updateDirecciones } from '../../Api/apicall_cliente';

const Index = () => {

    // estados de las listas
    const [tipoDireccion, setTipoDireccion] = useState(null);
    const [provinciaList, setProvinciaList] = useState(null);
    const [cantonLista, setCantonLista] = useState(null);
    const [parroquiaList, setParroquiaList] = useState(null);
    // estados de utilidad
    const [loading, setLoading] = useState(false);
    const [error, setError] = useState(false);
    // estado para guardar los datos del formulario
    // ! los datos por defecto deben de ser remplazados, y extraerlos de la busqueda
    const [values, setValues] = useState({
        DIRE_CODIGO: 3,
        TIDE_CODIGO: 5,
        DIRE_DESCRIPCION: "Jesús García 55",
        prov_codigo: 1,
        cant_codigo: 1,
        parr_codigo: 10
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
                    const datos = { CLIE_CODIGO: client.CLIE_CODIGO, direcciones: [values] }
                    updateDirecciones(datos)
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
                    if (cat.zona) setProvinciaList(cat.zona)
                    if (cat.ciudad) setCantonLista(cat.ciudad)
                    if (cat.tipo_direccion) setTipoDireccion(cat.tipo_direccion)
                })
            }
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
                heading="Mantenimiento de Direcciones"
                icon="lnr-earth icon-gradient bg-tempting-azure"
            />

            <Container fluid>

                <ClientInfo clientCode={client?.CLIE_CODIGO} typeClient={"NATURAL"} typeIdentification={"CEDULA"} identification={client?.CLIE_IDENTIFICACION} nameClient={client?.CLIE_NOMBRE_CORRESPONDENCIA} className='bg-primary' onChange={handleChange} type={"Info"}>

                    <Row>
                        <Col md={2}>
                            <FormGroup>
                                <Label for="sequence">Secuencia:</Label>
                                <Input type="text" name="sequence" id="sequence" value={"1"} disabled />
                            </FormGroup>
                        </Col>
                    </Row>
                </ClientInfo>

                <Card className="mt-4 mb-4">
                    <CardBody>
                        <Form>
                            <Row className="d-flex flex-column justify-content-center align-items-center">
                                <Col md={8}>
                                    <FormGroup row>
                                        <Label for="adressType" sm={4}>Tipo de dirección:</Label>
                                        <Col sm={4}>
                                            <Select
                                                options={tipoDireccion?.map(item => ({ value: item.TIDE_CODIGO, label: item.TIDE_DESCRIPCION }))}
                                                onChange={handleSelectChange("TIDE_CODIGO")}
                                            />
                                        </Col>
                                    </FormGroup>
                                </Col>
                            </Row>
                            <Row className="d-flex flex-column justify-content-center align-items-center">
                                <Col md={8}>
                                    <FormGroup row>
                                        <Label for="city" sm={4}>Provincia:</Label>
                                        <Col sm={4}>
                                            <Select
                                                options={provinciaList?.map(item => ({ value: item.ZONA_CODIGO, label: item.ZONA_DESCRIPCION }))}
                                                onChange={handleSelectChange("prov_codigo")}
                                            />
                                        </Col>
                                    </FormGroup>
                                </Col>
                            </Row>
                            <Row className="d-flex flex-column justify-content-center align-items-center">
                                <Col md={8}>
                                    <FormGroup row>
                                        <Label for="city" sm={4}>Cantón:</Label>
                                        <Col sm={4}>
                                            <Select
                                                options={cantonLista?.map(item => ({ value: item.CIUD_CODIGO, label: item.CIUD_NOMBRE }))}
                                                onChange={handleSelectChange("cant_codigo")}
                                            />
                                        </Col>
                                    </FormGroup>
                                </Col>
                            </Row>
                            <Row className="d-flex flex-column justify-content-center align-items-center">
                                <Col md={8}>
                                    <FormGroup row>
                                        <Label for="adress" sm={4}>Dirección:</Label>
                                        <Col sm={8}>
                                            <Input type="text" id="adress" name="adress" value={values?.DIRE_DESCRIPCION} onChange={handleChange("DIRE_DESCRIPCION")} />
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
