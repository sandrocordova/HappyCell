import React, { Fragment, useState } from 'react';
import PageTitle from "../../Layout/AppMain/PageTitle";
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

const Index = () => {

    // state
    const [loading, setLoading] = useState(false);

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
                    setLoading(true)
                    setTimeout(function () {
                        setLoading(false)
                        swal("Actualización completada con éxito!", {
                            icon: "success",
                        });
                    }, 2000);
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

                <ClientInfo clientCode={"0978374"} typeClient={"NATURAL"} typeIdentification={"CEDULA"} identification={"1111111112"} nameClient={"ojdflakdflaksdflkasf"}>
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
                                            <Input type="select" id="phoneType" name="phoneType">
                                                <option value="">Select</option>
                                            </Input>
                                        </Col>
                                    </FormGroup>
                                </Col>
                            </Row>
                            <Row className="d-flex flex-column justify-content-center align-items-center">
                                <Col md={6}>
                                    <FormGroup row>
                                        <Label for="phone" sm={4}>Número de teléfono:</Label>
                                        <Col sm={8}>
                                            <Input type="text" id="phone" name="phone" />
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
