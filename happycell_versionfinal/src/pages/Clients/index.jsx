
import React, { Fragment } from "react";
import { Route } from "react-router-dom";

// Clients
import SearchClient from '../SearchClient';
import ClientsNat from '../ClientsNat';

// Layout

import AppHeader from "../../Layout/AppHeader/";
import AppSidebar from "../../Layout/AppSidebar/";
import AppFooter from "../../Layout/AppFooter/";

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
                        <Route path={`${match.url}/searchclient`} component={SearchClient} />
                        <Route path={`${match.url}/clientsnat/:id`} component={ClientsNat} />
                    </div>
                    <AppFooter />
                </div>
            </div>
        </Fragment>
    );
}

export default Index;