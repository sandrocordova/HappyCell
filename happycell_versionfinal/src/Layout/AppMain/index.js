import { Route, Redirect } from "react-router-dom";
import React, { Suspense, lazy, Fragment } from "react";
import Loader from "react-loaders";
import Dashboard from "../../pages/Dashboard";
import { ToastContainer } from "react-toastify";
import Clients from "../../pages/Clients";
const UserPages = lazy(() => import("../../DemoPages/UserPages"));
const Applications = lazy(() => import("../../DemoPages/Applications"));
const Dashboards = lazy(() => import("../../DemoPages/Dashboards"));

const Widgets = lazy(() => import("../../DemoPages/Widgets"));
const Elements = lazy(() => import("../../DemoPages/Elements"));
const Components = lazy(() => import("../../DemoPages/Components"));
const Charts = lazy(() => import("../../DemoPages/Charts"));
const Forms = lazy(() => import("../../DemoPages/Forms"));
const Tables = lazy(() => import("../../DemoPages/Tables"));


const AppMain = () => {

    return (
        <Fragment>
            {/* Clients */}
            <Suspense fallback={
                <div className="loader-container">
                    <div className="loader-container-inner">
                        <div className="text-center">
                            <Loader type="ball-grid-cy" />
                        </div>
                        <h6 className="mt-3">
                            Please wait while we load all the Dashboards examples
                            <small>Because this is a demonstration, we load at once all the Dashboards examples. This wouldn't happen in a real live app!</small>
                        </h6>
                    </div>
                </div>
            }>
                <Route path="/clients" component={Clients} />
            </Suspense>

            <Suspense fallback={
                <div className="loader-container">
                    <div className="loader-container-inner">
                        <div className="text-center">
                            <Loader type="ball-grid-cy"/>
                        </div>
                        <h6 className="mt-3">
                            Please wait while we load all the Dashboards examples
                            <small>Because this is a demonstration, we load at once all the Dashboards examples. This wouldn't happen in a real live app!</small>
                        </h6>
                    </div>
                </div>
            }>
                <Route path="/dashboard" component={Dashboard}/>
            </Suspense>


            <Route exact path="/" render={() => (
                <Redirect to="/dashboard"/>
            )}/>
            <ToastContainer/>
        </Fragment>
    )
};

export default AppMain;
