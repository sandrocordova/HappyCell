import React, { Component, Fragment } from "react";
import { withRouter } from "react-router-dom";
import { connect } from "react-redux";
import MetisMenu from "react-metismenu";
import { setEnableMobileMenu } from "../../reducers/ThemeOptions";
import {
    DashboardNav,
    ClientNav,
    DirNav,
} from "./NavItems";

class Nav extends Component {
    state = {};

    toggleMobileSidebar = () => {
        let { enableMobileMenu, setEnableMobileMenu } = this.props;
        setEnableMobileMenu(!enableMobileMenu);
    };

    render() {
        return (
            <Fragment>
                <h5 className="app-sidebar__heading">Menu</h5>
                <MetisMenu content={DashboardNav} onSelected={this.toggleMobileSidebar} activeLinkFromLocation
                    className="vertical-nav-menu" iconNamePrefix="" classNameStateIcon="pe-7s-angle-down" />

                <h5 className="app-sidebar__heading">Clientes</h5>
                <MetisMenu content={ClientNav} onSelected={this.toggleMobileSidebar} activeLinkFromLocation
                    className="vertical-nav-menu" iconNamePrefix="" classNameStateIcon="pe-7s-angle-down" />

                <h5 className="app-sidebar__heading">Direcciones</h5>
                <MetisMenu content={DirNav} onSelected={this.toggleMobileSidebar} activeLinkFromLocation
                    className="vertical-nav-menu" iconNamePrefix="" classNameStateIcon="pe-7s-angle-down" />
            </Fragment>
        );
    }

    isPathActive(path) {
        return this.props.location.pathname.startsWith(path);
    }
}
const mapStateToProps = (state) => ({
    enableMobileMenu: state.ThemeOptions.enableMobileMenu,
});

const mapDispatchToProps = (dispatch) => ({
    setEnableMobileMenu: (enable) => dispatch(setEnableMobileMenu(enable)),
});
export default connect(mapStateToProps, mapDispatchToProps)(withRouter(Nav));
