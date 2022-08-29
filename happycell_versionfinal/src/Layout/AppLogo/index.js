import React, { Fragment, useState } from "react";
import { useSelector, useDispatch } from "react-redux";

import { Slider } from "react-burgers";

import AppMobileMenu from "../AppMobileMenu";

import { setEnableClosedSidebar } from '../../features/themeOptions/themeOptions';

const HeaderLogo = () => {

  const [active, setActive] = useState(false);
  const enableClosedSidebar = useSelector((state) => state.themeOptions.enableClosedSidebar)
  // const enableMobileMenu = useSelector((state) => state.themeOptions.enableMobileMenu)
  // const enableMobileMenuSmall = useSelector((state) => state.themeOptions.enableMobileMenuSmall)

  const dispatch = useDispatch();

  const toggleEnableClosedSidebar = () => {
    dispatch(setEnableClosedSidebar(!enableClosedSidebar))
  }

  return (
    <Fragment>
      <div className="app-header__logo">
        <div className="logo-src" />
        <div className="header__pane ms-auto">
          <div onClick={toggleEnableClosedSidebar}>
            <Slider width={26} lineHeight={2} lineSpacing={5} color="#6c757d"
              active={active} onClick={() => setActive(!active)} />
          </div>
        </div>
      </div>
      <AppMobileMenu />
    </Fragment>
  );
}

export default HeaderLogo;
