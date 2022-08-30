import React from 'react';
import Select from "react-select";
import {
    Row,
    Col,
    Card,
    CardBody,
    Input,
    FormGroup,
    Label,
} from "reactstrap";

const Index = ({ clientCode, typeClient, typeIdentification, identification, nameClient, children, onChange, type = "Info" }) => {
    return (
        <Card className='bg-transparent'>
            <CardBody>
                <Row>
                    <Col md={2}>
                        <FormGroup>
                            <Label for="clientCode">Código cliente:</Label>
                            <Input type="text" name="clientCode" id="clientCode" value={clientCode} disabled />
                        </FormGroup>
                    </Col>
                    <Col md={2}>
                        <FormGroup>
                            <Label for="clientTipe">Tipo:</Label>
                            <Select
                                defaultValue={{ value: "clie", label: typeClient }}
                                options={[{ value: "clie", label: typeClient }]}
                            />
                        </FormGroup>
                    </Col>
                    <Col md={3}>
                        <FormGroup>
                            <Label for="typeIdentification">Tipo de identificación:</Label>
                            <Select
                                defaultValue={{ value: "ident", label: typeIdentification }}
                                options={[{ value: "ident", label: typeIdentification }]}
                            />
                        </FormGroup>
                    </Col>
                    <Col md={2}>
                        <FormGroup>
                            <Label for="identification">Identificación:</Label>
                            <Input type="text" name="identification" id="identification" value={identification} disabled />
                        </FormGroup>
                    </Col>
                    <Col md={3}>
                        <FormGroup>
                            <Label for="clientName">Nombre:</Label>
                            {type === "Info"
                                ? <Input type="text" name="clientName" id="clientName" value={nameClient} disabled />
                                : <Input type="text" name="clientName" id="clientName" value={nameClient} onChange={onChange("CLIE_NOMBRE_CORRESPONDENCIA")} />}

                        </FormGroup>
                    </Col>
                </Row>
                {children}
            </CardBody>
        </Card>
    );
}

export default Index;
