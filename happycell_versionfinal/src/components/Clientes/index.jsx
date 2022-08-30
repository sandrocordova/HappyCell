
import React, { Component, Fragment } from "react";

import {
    Row,
    Col,
    Container,

} from "reactstrap";


// Layout

import AppHeader from "../../Layout/AppHeader/";
import AppSidebar from "../../Layout/AppSidebar/";
import AppFooter from "../../Layout/AppFooter/";



// Theme Options

import ThemeOptions from "../../Layout/ThemeOptions/";


const Mantenimiento = () => {





    return (
        <div>
            <Fragment>
                <Container fluid>
                    <Row>
                        <Col md="6" xl="4">
                            <div className="card mb-3 widget-content bg-night-fade">
                                <div className="widget-content-wrapper text-white">
                                    <div className="widget-content-left">
                                        <div className="widget-heading">Clientes</div>

                                    </div>

                                </div>
                            </div>
                        </Col>
                        <Col md="6" xl="4">
                            <div className="card mb-3 widget-content bg-arielle-smile">
                                <div className="widget-content-wrapper text-white">
                                    <div className="widget-content-left">
                                        <div className="widget-heading">Direcciones</div>

                                    </div>

                                </div>
                            </div>
                        </Col>
                        <Col md="6" xl="4">
                            <div className="card mb-3 widget-content bg-happy-green">
                                <div className="widget-content-wrapper text-white">
                                    <div className="widget-content-left">
                                        <div className="widget-heading">Asesor</div>

                                    </div>

                                </div>
                            </div>
                        </Col>

                    </Row>
                    <Row>
                        <Col md="6" xl="4">
                            <div className="card mb-3 widget-content bg-night-fade">
                                <div className="widget-content-wrapper text-white">
                                    <div className="widget-content-left">
                                        <div className="widget-heading">Documentos</div>

                                    </div>

                                </div>
                            </div>
                        </Col>
                        <Col md="6" xl="4">
                            <div className="card mb-3 widget-content bg-arielle-smile">
                                <div className="widget-content-wrapper text-white">
                                    <div className="widget-content-left">
                                        <div className="widget-heading">Referencias Comerciales</div>

                                    </div>

                                </div>
                            </div>
                        </Col>
                        <Col md="6" xl="4">
                            <div className="card mb-3 widget-content bg-happy-green">
                                <div className="widget-content-wrapper text-white">
                                    <div className="widget-content-left">
                                        <div className="widget-heading">Referencias Bancarias</div>

                                    </div>

                                </div>
                            </div>
                        </Col>

                    </Row>
                    <Row>
                        <Col md="6" xl="4">
                            <div className="card mb-3 widget-content bg-night-fade">
                                <div className="widget-content-wrapper text-white">
                                    <div className="widget-content-left">
                                        <div className="widget-heading">Situacion Financiera</div>

                                    </div>

                                </div>
                            </div>
                        </Col>


                    </Row>

                </Container>
            </Fragment>
        </div>

    )
};
export default Mantenimiento;