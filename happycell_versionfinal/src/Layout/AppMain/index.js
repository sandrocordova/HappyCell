import { Route, Redirect } from "react-router-dom";
import React, { Suspense, lazy, Fragment } from "react";
import Loader from "react-loaders";
import { ToastContainer } from "react-toastify";

const Dashboard = lazy(() => import("../../pages/Dashboard"));
const Clients = lazy(() => import("../../pages/Clients"));
const Directions = lazy(() => import("../../pages/Directions"));

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
            {/*Direcciones*/}
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
                <Route path="/directions" component={Directions} />
            </Suspense>
            {/*Dashboard*/}
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
                <Route path="/dashboard" component={Dashboard} />
            </Suspense>



            <Route exact path="/" render={() => (
                <Redirect to="/dashboard" />
            )} />
            <ToastContainer />
        </Fragment>
    )
};

export default AppMain;
