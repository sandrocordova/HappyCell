import React from 'react';
import {
    Row,
    Col,
    Card,
    CardBody,
    Input,
    FormGroup,
    Label,
} from "reactstrap";

const Index = ({ clientCode, typeClient, typeIdentification, identification, nameClient, children }) => {
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
                            <Input type="select" id="clientTipe" name="clientTipe" defaultValue={"DEFAULT"}>
                                <option value="SELECT" selected>{typeClient}</option>
                            </Input>
                        </FormGroup>
                    </Col>
                    <Col md={3}>
                        <FormGroup>
                            <Label for="typeIdentification">Tipo de identificación:</Label>
                            <Input type="select" id="typeIdentification" name="typeIdentification">
                                <option value="">{typeIdentification}</option>
                            </Input>
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
                            <Input type="text" name="clientName" id="clientName" value={nameClient} disabled />
                        </FormGroup>
                    </Col>
                </Row>
                {children}
            </CardBody>
        </Card>
    );
}

export default Index;
