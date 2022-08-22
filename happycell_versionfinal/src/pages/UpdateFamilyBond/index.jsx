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
                heading="Mantenimiento de Vínculos"
                icon="lnr-users icon-gradient bg-tempting-azure"
            />

            <Container fluid>

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
                                            <Input type="select" id="bondType" name="bondType">
                                                <option value="">Select</option>
                                            </Input>
                                        </Col>
                                    </FormGroup>
                                </Col>
                                <Col md={4}>
                                    <FormGroup>
                                        <Label for="identification">Identificación:</Label>
                                        <Col>
                                            <Input type="text" id="identification" name="identification" />
                                        </Col>
                                    </FormGroup>
                                </Col>
                                <Col md={4}>
                                    <FormGroup>
                                        <Label for="bondName">Nombre de vínculo:</Label>
                                        <Col>
                                            <Input type="text" id="bondName" name="bondName" />
                                        </Col>
                                    </FormGroup>
                                </Col>
                            </Row>
                            <Row>
                                <Col md={8}>
                                    <FormGroup>
                                        <Label for="adress">Dirección:</Label>
                                        <Col>
                                            <Input type="text" id="adress" name="adress" />
                                        </Col>
                                    </FormGroup>
                                </Col>
                                <Col md={4}>
                                    <FormGroup>
                                        <Label for="phone">Teléfono:</Label>
                                        <Col>
                                            <Input type="text" id="phone" name="phone" />
                                        </Col>
                                    </FormGroup>
                                </Col>
                            </Row>
                            <Row>
                                <Col md={4}>
                                    <FormGroup>
                                        <Label for="nationality">Nacionalidad:</Label>
                                        <Col>
                                            <Input type="select" id="nationality" name="nationality">
                                                <option value="">Select</option>
                                            </Input>
                                        </Col>
                                    </FormGroup>
                                </Col>
                                <Col md={4}>
                                    <FormGroup>
                                        <Label for="maritalStatus">Estado civil:</Label>
                                        <Col>
                                            <Input type="select" id="maritalStatus" name="maritalStatus">
                                                <option value="">Select</option>
                                            </Input>
                                        </Col>
                                    </FormGroup>
                                </Col>
                                <Col md={4}>
                                    <FormGroup>
                                        <Label for="profession">Profesión:</Label>
                                        <Col>
                                            <Input type="select" id="profession" name="profession">
                                                <option value="">Select</option>
                                            </Input>
                                        </Col>
                                    </FormGroup>
                                </Col>
                            </Row>
                            <Row>
                                <Col md={8}>
                                    <FormGroup>
                                        <Label for="jobTitle">Cargo:</Label>
                                        <Col>
                                            <Input type="text" id="jobTitle" name="jobTitle" />
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
