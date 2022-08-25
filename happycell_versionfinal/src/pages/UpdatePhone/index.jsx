import React, { Fragment, useState } from 'react';
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
import { updateTelefono } from '../../Api/apicall_cliente';

const Index = () => {

    // estados de utilidad
    const [loading, setLoading] = useState(false);
    const [error, setError] = useState(false);
    // estado para guardar los datos del formulario
    // ! los datos por defecto deben de ser remplazados, y extraerlos de la busqueda
    const [values, setValues] = useState({
        TELE_CODIGO: 1,
        TITE_CODIGO: 1,
        TIDE_CODIGO: 1,
        DIRE_CODIGO: 3,
        TELE_NUMERO: ""
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
                    const datos = { CLIE_CODIGO: client.CLIE_CODIGO, telefonos: [values] }
                    updateTelefono(datos)
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

    return (
        <Fragment>

            <Modal isOpen={loading} backdrop={'static'} centered className='shadow-none text-center' contentClassName={"bg-transparent shadow-none border border-0"}>
                <Loader type="ball-pulse" />
            </Modal>

            <PageTitle
                heading="Mantenimiento de Teléfonos"
                icon="lnr-phone icon-gradient bg-tempting-azure"
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
                        <Col md={2}>
                            <FormGroup>
                                <Label for="city">Ciudad:</Label>
                                <Input type="text" name="city" id="city" value={"QUITO"} disabled />
                            </FormGroup>
                        </Col>
                        <Col md={8}>
                            <FormGroup>
                                <Label for="adress">Dirección:</Label>
                                <Input type="text" name="adress" id="adress" value={"AMAZONAS Y GASPAR DE VILLARROEL"} disabled />
                            </FormGroup>
                        </Col>
                    </Row>
                </ClientInfo>

                <Card className="mt-4 mb-4">
                    <CardBody>
                        <Form>
                            <Row className="d-flex flex-column justify-content-center align-items-center">
                                <Col md={6}>
                                    <FormGroup row>
                                        <Label for="phoneType" sm={4}>Tipo teléfono:</Label>
                                        <Col sm={8}>
                                            <Select
                                                defaultValue={{ value: 2, label: "CELULAR" }}
                                                options={[{ value: 2, label: "CELULAR" }]}
                                            />
                                        </Col>
                                    </FormGroup>
                                </Col>
                            </Row>
                            <Row className="d-flex flex-column justify-content-center align-items-center">
                                <Col md={6}>
                                    <FormGroup row>
                                        <Label for="phone" sm={4}>Número de teléfono:</Label>
                                        <Col sm={8}>
                                            <Input type="text" id="phone" name="phone" onChange={handleChange("TELE_NUMERO")} />
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
