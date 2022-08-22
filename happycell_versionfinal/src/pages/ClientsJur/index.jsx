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

    return (
        <Fragment>

            <Modal isOpen={loading} backdrop={'static'} centered className='shadow-none text-center' contentClassName={"bg-transparent shadow-none border border-0"}>
                <Loader type="ball-pulse" />
            </Modal>

            <PageTitle
                heading="Mantenimiento de Cliente Jurídico"
                icon="lnr-user icon-gradient bg-tempting-azure"
            />

            <Container fluid>

                <ClientInfo clientCode={"123"} typeClient={"JURIDICO"} typeIdentification={"RUC"} identification={"0987654321234"} nameClient={"ojdflakdflaksdflkasf"} />

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
                                                {/* {catalogo[1]?.nacionalidad?.map((data, i) => (
                                                <option key={i} value={data.naci_codigo}>
                                                    {data.naci_descripcion}
                                                </option>
                                            ))} */}
                                            </Input>
                                        </Col>
                                    </FormGroup>
                                </Col>
                                <Col md={4}>
                                    <FormGroup row>
                                        <Label for="name" sm={4}>Nombre:</Label>
                                        <Col sm={8}>
                                            <Input type="text" name="name" id="name" />
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
                                                {/* {catalogo[2]?.actividad_economica?.map((data, i) => (
                                                <option key={i} value={data.acti_codigo}>
                                                    {data.acti_descripcion}
                                                </option>
                                            ))} */}
                                            </Input>
                                        </Col>
                                    </FormGroup>
                                </Col>
                                <Col md={4}>
                                    <FormGroup row>
                                        <Label for="categoryClient" sm={4}>Categoría cliente:</Label>
                                        <Col sm={8}>
                                            <Input type="select" id="categoryClient" name="categoryClient">
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
                                <Col md={4}>
                                    <FormGroup row>
                                        <Label for="typeCompany" sm={4}>Tipo empresa:</Label>
                                        <Col sm={8}>
                                            <Input type="select" id="typeCompany" name="typeCompany">
                                                <option value="">Select</option>
                                                {/* {catalogo[2]?.actividad_economica?.map((data, i) => (
                                                <option key={i} value={data.acti_codigo}>
                                                    {data.acti_descripcion}
                                                </option>
                                            ))} */}
                                            </Input>
                                        </Col>
                                    </FormGroup>
                                </Col>
                                <Col md={4}>
                                    <FormGroup row>
                                        <Label for="businessName" sm={4}>Razón social:</Label>
                                        <Col sm={8}>
                                            <Input type="text" name="businessName" id="businessName" />
                                        </Col>
                                    </FormGroup>
                                </Col>
                                <Col md={4}>
                                    <FormGroup row>
                                        <Label for="advertisingName" sm={4}>Nombre publicitario:</Label>
                                        <Col sm={8}>
                                            <Input type="text" name="advertisingName" id="advertisingName" />
                                        </Col>
                                    </FormGroup>
                                </Col>
                            </Row>
                            <Row>
                                <Col md={4}>
                                    <FormGroup row>
                                        <Label for="subscribedCapital" sm={4}>Capital suscrito:</Label>
                                        <Col sm={8}>
                                            <Input type="text" name="subscribedCapital" id="subscribedCapital" />
                                        </Col>
                                    </FormGroup>
                                </Col>
                                <Col md={4}>
                                    <FormGroup row>
                                        <Label for="paidCapital" sm={4}>Capital pagado:</Label>
                                        <Col sm={8}>
                                            <Input type="text" name="paidCapital" id="paidCapital" />
                                        </Col>
                                    </FormGroup>
                                </Col>
                                <Col md={4}>
                                    <FormGroup row>
                                        <Label for="reservaLegal" sm={4}>Reserva legal:</Label>
                                        <Col sm={8}>
                                            <Input type="text" name="reservaLegal" id="reservaLegal" />
                                        </Col>
                                    </FormGroup>
                                </Col>
                            </Row>
                            <Row>
                                <Col md={4}>
                                    <FormGroup row>
                                        <Label for="economicGroup" sm={4}>Grupo económico:</Label>
                                        <Col sm={8}>
                                            <Input type="text" name="economicGroup" id="economicGroup" />
                                        </Col>
                                    </FormGroup>
                                </Col>
                                <Col md={5}>
                                    <FormGroup row>
                                        <Label for="statutesDate" sm={6}>Fecha reforma estatutos:</Label>
                                        <Col sm={6}>
                                            <Input type="date" name="statutesDate" id="statutesDate" />
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
