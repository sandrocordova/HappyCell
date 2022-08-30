
import React, { Fragment } from "react";
import { Route } from "react-router-dom";

// Clients
import SearchClient from '../SearchClient';
import ClientsNat from '../ClientsNat';
import ClientsJur from '../ClientsJur';
import UpdateAddress from '../UpdateAddress';
import UpdatePhone from '../UpdatePhone';
import UpdateObservation from '../UpdateObservation';
import UpdateFamilyBond from '../UpdateFamilyBond';

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
                        <Route path={`${match.url}/clientsjur`} component={ClientsJur} />
                        <Route path={`${match.url}/update-adress`} component={UpdateAddress} />
                        <Route path={`${match.url}/update-phone`} component={UpdatePhone} />
                        <Route path={`${match.url}/update-obser`} component={UpdateObservation} />
                        <Route path={`${match.url}/update-bond`} component={UpdateFamilyBond} />
                    </div>
                    {/* <AppFooter /> */}
                </div>
            </div>
        </Fragment>
    );
}

export default Index;