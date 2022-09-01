
import React, { Component, Fragment } from "react";
import { Button } from "reactstrap";
//import {Mantenimiento} from "../../components/Clientes"



// Layout

import AppHeader from "../../Layout/AppHeader/";
import AppSidebar from "../../Layout/AppSidebar/";
import AppFooter from "../../Layout/AppFooter/";

import DataTableFixedHeader from "../../components/Telefonos/FixedHeader"

// Theme Options

import ThemeOptions from "../../Layout/ThemeOptions/";

const Index = ({ match }) => {
    return (
        <Fragment>
            <ThemeOptions />
            <AppHeader />
            <div className="app-main">
                <AppSidebar />
                <div className="app-main__outer">
                    <div className="app-main__inner">
                        <div className="app-page-title">
                            <div className="page-title-wrapper">
                                <div className="page-title-heading">
                                    Telefonos
                                </div>
                            </div>
                            {/* <Mantenimiento/>*/}

                        </div>
                        <div>
                            <DataTableFixedHeader />
                        </div>
                        <div style={{ textAlign: "right" }}>
                            <Button className="mb-2 me-2" color="success">
                                Seleccionar
                            </Button>
                            <Button className="mb-2 me-2" color="danger">
                                Cerrar
                            </Button>
                        </div>

                    </div>
                    <AppFooter />
                </div>
            </div>
        </Fragment>
    );
}

export default Index;