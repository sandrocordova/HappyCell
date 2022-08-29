import React, { Fragment } from "react";
import { useSelector, useDispatch } from "react-redux";
import cx from "classnames";

import Nav from "../AppNav/VerticalNavWrapper";

import { CSSTransition, TransitionGroup } from 'react-transition-group';

import PerfectScrollbar from "react-perfect-scrollbar";
import HeaderLogo from "../AppLogo";

import { setEnableMobileMenu } from '../../features/themeOptions/themeOptions';

const AppSidebar = () => {

  const enableMobileMenu = useSelector((state) => state.themeOptions.enableMobileMenu)
  const backgroundColor = useSelector((state) => state.themeOptions.backgroundColor)
  const enableBackgroundImage = useSelector((state) => state.themeOptions.enableBackgroundImage)
  const enableSidebarShadow = useSelector((state) => state.themeOptions.enableSidebarShadow)
  const backgroundImage = useSelector((state) => state.themeOptions.backgroundImage)
  const backgroundImageOpacity = useSelector((state) => state.themeOptions.backgroundImageOpacity)

  const dispatch = useDispatch()

  const toggleMobileSidebar = () => {
    dispatch(setEnableMobileMenu(!enableMobileMenu))
  };

  return (
    <Fragment>
      <div className="sidebar-mobile-overlay" onClick={toggleMobileSidebar} />
      <TransitionGroup>
        <CSSTransition component="div"
          className={cx("app-sidebar", backgroundColor, {
            "sidebar-shadow": enableSidebarShadow,
          })}
          appear={true} enter={false} exit={false} timeout={500}>
          <div>
            <HeaderLogo />
            <PerfectScrollbar>
              <div className="app-sidebar__inner">
                <Nav />
              </div>
            </PerfectScrollbar>
            <div className={cx("app-sidebar-bg", backgroundImageOpacity)}
              style={{
                backgroundImage: enableBackgroundImage
                  ? "url(" + backgroundImage + ")"
                  : null,
              }}>
            </div>
          </div>
        </CSSTransition>
      </TransitionGroup>
    </Fragment>
  );

}

export default AppSidebar;
