import React, { Fragment } from "react";
import { withRouter } from "react-router-dom";
import { useSelector, useDispatch } from "react-redux";
import MetisMenu from "react-metismenu";
import { setEnableMobileMenu } from '../../features/themeOptions/themeOptions';
import {
    DashboardNav,
    ClientNav,
    DirNav,
    TelNav,
    AseNav,
    ObsNav,
    VinNav
} from "./NavItems";

const Nav = () => {

    const enableMobileMenu = useSelector((state) => state.themeOptions.enableMobileMenu)

    const dispatch = useDispatch()

    const toggleMobileSidebar = () => {
        dispatch(setEnableMobileMenu(!enableMobileMenu))
    };

    return (
        <Fragment>
            <h5 className="app-sidebar__heading">Menu</h5>
            <MetisMenu content={DashboardNav} onSelected={toggleMobileSidebar} activeLinkFromLocation
                className="vertical-nav-menu" iconNamePrefix="" classNameStateIcon="pe-7s-angle-down" />

            <h5 className="app-sidebar__heading">Clientes</h5>
            <MetisMenu content={ClientNav} onSelected={toggleMobileSidebar} activeLinkFromLocation
                className="vertical-nav-menu" iconNamePrefix="" classNameStateIcon="pe-7s-angle-down" />

            <h5 className="app-sidebar__heading">Direcciones</h5>
            <MetisMenu content={DirNav} onSelected={toggleMobileSidebar} activeLinkFromLocation
                className="vertical-nav-menu" iconNamePrefix="" classNameStateIcon="pe-7s-angle-down" />
            <h5 className="app-sidebar__heading">Telefonos</h5>
            <MetisMenu content={TelNav} onSelected={toggleMobileSidebar} activeLinkFromLocation
                className="vertical-nav-menu" iconNamePrefix="" classNameStateIcon="pe-7s-angle-down" />
            <h5 className="app-sidebar__heading">Asesores</h5>
            <MetisMenu content={AseNav} onSelected={toggleMobileSidebar} activeLinkFromLocation
                className="vertical-nav-menu" iconNamePrefix="" classNameStateIcon="pe-7s-angle-down" />
            <h5 className="app-sidebar__heading">Observaciones</h5>
            <MetisMenu content={ObsNav} onSelected={toggleMobileSidebar} activeLinkFromLocation
                className="vertical-nav-menu" iconNamePrefix="" classNameStateIcon="pe-7s-angle-down" />
            <h5 className="app-sidebar__heading">Vinculos</h5>
            <MetisMenu content={VinNav} onSelected={toggleMobileSidebar} activeLinkFromLocation
                className="vertical-nav-menu" iconNamePrefix="" classNameStateIcon="pe-7s-angle-down" />
        </Fragment>
    );
}

// isPathActive(path) {
//     return this.props.location.pathname.startsWith(path);
// }
export default withRouter(Nav);
