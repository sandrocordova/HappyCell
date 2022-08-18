import React, { Fragment } from "react";

// DASHBOARDS



// Layout

import AppHeader from "../../Layout/AppHeader/";
import AppSidebar from "../../Layout/AppSidebar/";
import AppFooter from "../../Layout/AppFooter/";

// Theme Options
import ThemeOptions from "../../Layout/ThemeOptions/";
function Dashboard() {
    return (
        <Fragment>
            <ThemeOptions />
            <AppHeader />
            <div className="app-main">
                <AppSidebar />
                <div className="app-main__outer">
                    <div className="app-main__inner">
                        <h1>
                            hola mundo
                        </h1>
                    </div>
                    <AppFooter />
                </div>
            </div>
        </Fragment>
    );
}
export default Dashboard;