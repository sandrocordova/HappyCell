
import React, { Component, Fragment } from "react";
import { Route } from 'react-router-dom';
//import {Mantenimiento} from "../../components/Clientes"
import { Button } from "reactstrap";

// Clients
import SearchClient from '../SearchClient';
import ClientsNat from '../ClientsNat';
import ClientsJur from '../ClientsJur';

// Layout
import AppHeader from "../../Layout/AppHeader/";
import AppSidebar from "../../Layout/AppSidebar/";
import AppFooter from "../../Layout/AppFooter/";

import DataTableFixedHeader from "../../components/Clientes/FixedHeader"


const Index = ({ match }) => {
    return (
        <Fragment>
            <AppHeader />
            <div className="app-main">
                <AppSidebar />
                <div className="app-main__outer">
                    <div className="app-main__inner">
                        <Route path={`${match.url}/searchclient`} component={SearchClient} />
                        <Route path={`${match.url}/clientsnat/:id`} component={ClientsNat} />
                        <Route path={`${match.url}/clientsjur/:id`} component={ClientsJur} />
                    </div>
                    {/* <AppFooter /> */}
                </div>
            </div>
        </Fragment>
    );
}

export default Index;