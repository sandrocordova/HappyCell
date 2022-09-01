
import React, { Component, Fragment } from "react";
//import {Mantenimiento} from "../../components/Clientes"
import { Button } from "reactstrap";

// Clients
import SearchClient from '../SearchClient';
import ClientsNat from '../ClientsNat';
import { BrowserRouter, Router, Route } from 'react-router-dom';
// Layout
import AppHeader from "../../Layout/AppHeader/";
import AppSidebar from "../../Layout/AppSidebar/";
import AppFooter from "../../Layout/AppFooter/";
import Clientes from "../../components/Clientes";
import DataTableFixedHeader from "../../components/Clientes/FixedHeader"

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
                        {/* <Clientes/>*/}
                        <div className="app-page-title">
                            <div className="page-title-wrapper">
                                <div className="page-title-heading">
                                    Mantenimiento de Clientes
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

                        {/*<div>*/}
                        {/*    Mantenimiento Clientes*/}
                        {/*</div>*/}
                        {/*<DataTableFixedHeader />*/}
                        {/*<Route path={`${match.url}/clientsnat/:id`} component={ClientsNat} />*/}
                    </div>
                    {/* <AppFooter /> */}
                </div>
            </div>
        </Fragment>
    );
}

export default Index;