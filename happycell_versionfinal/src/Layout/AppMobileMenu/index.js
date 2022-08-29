import React, { Fragment, useState } from "react";
import { useSelector, useDispatch } from "react-redux";

import { Slider } from "react-burgers";

import cx from "classnames";

import { faEllipsisV } from "@fortawesome/free-solid-svg-icons";

import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";

import { Button } from "reactstrap";

import { setEnableMobileMenu, setEnableMobileMenuSmall } from '../../features/themeOptions/themeOptions';

const AppMobileMenu = () => {

  const [active, setActive] = useState(false);
  const [activeSecondaryMenuMobile, setActiveSecondaryMenuMobile] = useState(false);

  // const closedSmallerSidebar = useSelector((state) => state.themeOptions.enableClosedSidebar)
  const enableMobileMenu = useSelector((state) => state.themeOptions.enableMobileMenu)
  const enableMobileMenuSmall = useSelector((state) => state.themeOptions.enableMobileMenuSmall)

  const dispatch = useDispatch();

  const toggleMobileSidebar = () => {
    dispatch(setEnableMobileMenu(!enableMobileMenu))
  }

  const toggleMobileSmall = () => {
    dispatch(setEnableMobileMenuSmall(!enableMobileMenuSmall))
  }

  return (
    <Fragment>
      <div className="app-header__mobile-menu">
        <div onClick={toggleMobileSidebar}>
          <Slider width={26} lineHeight={2} lineSpacing={5} color="#6c757d"
            active={active} onClick={() => setActive(!active)} />
        </div>
      </div>
      <div className="app-header__menu">

        <span onClick={toggleMobileSmall}>
          <Button size="sm" className={cx("btn-icon btn-icon-only", {
            active: activeSecondaryMenuMobile
          })}
            color="primary"
            onClick={() =>
              setActiveSecondaryMenuMobile(!activeSecondaryMenuMobile)
            }>
            <div className="btn-icon-wrapper">
              <FontAwesomeIcon icon={faEllipsisV} />
            </div>
          </Button>
        </span>
      </div>
    </Fragment>
  );
}

export default AppMobileMenu;
