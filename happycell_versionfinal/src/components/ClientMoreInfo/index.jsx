import React from 'react';
import {
    Row,
    Col,
    Button,
    Card,
    CardBody,
    Collapse
} from "reactstrap";

const Index = ({ isOpen = false, setIsOpen }) => {
    return (
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
                            <span className='fw-bold text-black-50 me-1'>Primer atraso:</span> <span>123</span>
                        </Col>
                        <Col md={12} className="mb-2 d-flex justify-content-between">
                            <span className='fw-bold text-black-50 me-1'>Segundo atraso:</span> <span>123</span>
                        </Col>
                        <Col md={12} className="mb-2 d-flex justify-content-between">
                            <span className='fw-bold text-black-50 me-1'>Tercer atraso:</span> <span>123</span>
                        </Col>
                        <Col md={12} className="mb-2 d-flex justify-content-between">
                            <span className='fw-bold text-black-50 me-1'>Atraso promedio:</span> <span>123</span>
                        </Col>
                        <Col md={12} className="mb-2 d-flex justify-content-between">
                            <span className='fw-bold text-black-50 me-1'>N° meses de la última cancelación:</span> <span>123</span>
                        </Col>
                        <Col md={12} className="mb-2 d-flex justify-content-between">
                            <span className='fw-bold text-black-50 me-1'>N° de operaciones vigentes:</span> <span>123</span>
                        </Col>
                        <Col md={12} className="mb-2 d-flex justify-content-between">
                            <span className='fw-bold text-black-50 me-1'>N° de operaciones canceladas:</span> <span>123</span>
                        </Col>
                        <Col md={12} className="mb-2 d-flex justify-content-between">
                            <span className='fw-bold text-black-50 me-1'>N° de operaciones castigadas:</span> <span>123</span>
                        </Col>
                        <Col md={12} className="mb-2 d-flex justify-content-between">
                            <span className='fw-bold text-black-50 me-1'>N° de operaciones anuladas:</span> <span>123</span>
                        </Col>
                        <Col md={12} className="mb-2 d-flex justify-content-between">
                            <span className='fw-bold text-black-50 me-1'>N° de operaciones no anuladas:</span> <span>123</span>
                        </Col>
                        <Col md={12} className="mb-2 d-flex justify-content-between">
                            <span className='fw-bold text-black-50 me-1'>N° de operaciones vencidas:</span> <span>123</span>
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
    );
}

export default Index;
