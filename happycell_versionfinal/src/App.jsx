import React, { Fragment } from "react";
import { useSelector } from 'react-redux'
import cx from "classnames";
import { withRouter } from "react-router-dom";

import ResizeDetector from "react-resize-detector";

import AppMain from "./Layout/AppMain";

const App = () => {

    const closedSmallerSidebar = false
    const colorScheme = useSelector((state) => state.themeOptions.colorScheme);
    const enableFixedHeader = useSelector((state) => state.themeOptions.enableFixedHeader);
    const enableFixedSidebar = useSelector((state) => state.themeOptions.enableFixedSidebar);
    const enableFixedFooter = useSelector((state) => state.themeOptions.enableFixedFooter);
    const enableClosedSidebar = useSelector((state) => state.themeOptions.enableClosedSidebar);
    const enableMobileMenu = useSelector((state) => state.themeOptions.enableMobileMenu);
    const enablePageTabsAlt = useSelector((state) => state.themeOptions.enablePageTabsAlt);

    return (
        <ResizeDetector
            handleWidth
            render={({ width }) => (
                <Fragment>
                    <div
                        className={cx(
                            "app-container app-theme-" + colorScheme,
                            { "fixed-header": enableFixedHeader },
                            { "fixed-sidebar": enableFixedSidebar || width < 1250 },
                            { "fixed-footer": enableFixedFooter },
                            { "closed-sidebar": enableClosedSidebar || width < 1250 },
                            {
                                "closed-sidebar-mobile": closedSmallerSidebar || width < 1250,
                            },
                            { "sidebar-mobile-open": enableMobileMenu },
                            { "body-tabs-shadow-btn": enablePageTabsAlt }
                        )}
                    >
                        <AppMain />
                    </div>
                </Fragment>
            )}
        />
    );
}

export default withRouter(App);
