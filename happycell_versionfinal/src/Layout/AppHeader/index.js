import React, { Fragment } from "react";
import cx from "classnames";

import { useSelector } from "react-redux";

import { CSSTransition, TransitionGroup } from 'react-transition-group';

import HeaderLogo from "../AppLogo";

import UserBox from "./Components/UserBox";
// import SearchBox from "./Components/SearchBox";
// import MegaMenu from "./Components/MegaMenu";
// import HeaderDots from "./Components/HeaderDots";

const Header = () => {

  const enableHeaderShadow = useSelector((state) => state.themeOptions.enableHeaderShadow);
  const headerBackgroundColor = useSelector((state) => state.themeOptions.headerBackgroundColor);
  const enableMobileMenuSmall = useSelector((state) => state.themeOptions.enableMobileMenuSmall);
  // const closedSmallerSidebar= useSelector((state) => state.themeOptions.closedSmallerSidebar);

  return (
    <Fragment>
      <TransitionGroup>
        <CSSTransition component="div"
          className={cx("app-header", headerBackgroundColor, {
            "header-shadow": enableHeaderShadow,
          })}
          appear={true} timeout={1500} enter={false} exit={false}>
          <div>
            <HeaderLogo />
            <div className={cx("app-header__content", {
              "header-mobile-open": enableMobileMenuSmall,
            })}>
              <div className="app-header-left">
                {/* <SearchBox /> */}
                {/* <MegaMenu /> */}
              </div>
              <div className="app-header-right">
                {/* <HeaderDots /> */}
                <UserBox />
              </div>
            </div>
          </div>
        </CSSTransition>
      </TransitionGroup>
    </Fragment>
  );
}

export default Header;
