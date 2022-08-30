import React from "react";
import { useSelector } from "react-redux";
import cx from "classnames";

import { Button, UncontrolledTooltip } from "reactstrap";

import { toast, Slide } from "react-toastify";

import { faBatteryThreeQuarters } from "@fortawesome/free-solid-svg-icons";

import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";

const PageTitle = ({ heading, icon, subheading }) => {

  const enablePageTitleIcon = useSelector((state) => state.themeOptions.enablePageTitleIcon)
  const enablePageTitleSubheading = useSelector((state) => state.themeOptions.enablePageTitleSubheading)

  const notify22 = () =>
  (toast("You can add whatever element in this section.", {
    transition: Slide,
    closeButton: true,
    autoClose: 5000,
    position: "bottom-center",
    type: "default",
  }));

  return (
    <div className="app-page-title">
      <div className="page-title-wrapper">
        <div className="page-title-heading">
          <div className={cx("page-title-icon bg-happy-fisher", {
            "d-none": !enablePageTitleIcon,
          })}>
            <i className={icon} />
          </div>
          <div>
            {heading}
            <div className={cx("page-title-subheading", {
              "d-none": !enablePageTitleSubheading,
            })}>
              {subheading}
            </div>
          </div>
        </div>
        <div className="page-title-actions">
          <Button className="btn-pill me-3" onClick={notify22} color="success" id="Tooltip-123">
            <FontAwesomeIcon icon={faBatteryThreeQuarters} />
          </Button>
          <UncontrolledTooltip placement="left" target={"Tooltip-123"}>
            A notification example!
          </UncontrolledTooltip>
        </div>
      </div>
    </div>
  );
}

export default PageTitle;
