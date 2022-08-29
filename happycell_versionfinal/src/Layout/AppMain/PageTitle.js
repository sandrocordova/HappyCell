import React from "react";
import { useSelector } from "react-redux";
import cx from "classnames";

import TitleComponent1 from "./PageTitleExamples/Variation1";
import TitleComponent2 from "./PageTitleExamples/Variation2";
import TitleComponent3 from "./PageTitleExamples/Variation3";

const PageTitle = ({ heading,
  icon,
  subheading }) => {

  const randomize = (myArray) => {
    return myArray[Math.floor(Math.random() * myArray.length)];
  }

  const enablePageTitleIcon = useSelector((state) => state.themeOptions.enablePageTitleIcon)
  const enablePageTitleSubheading = useSelector((state) => state.themeOptions.enablePageTitleSubheading)


  let arr = [<TitleComponent1 />, <TitleComponent2 />, <TitleComponent3 />];

  return (
    <div className="app-page-title">
      <div className="page-title-wrapper">
        <div className="page-title-heading">
          <div className={cx("page-title-icon", {
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
        <div className="page-title-actions">{randomize(arr)}</div>
      </div>
    </div>
  );
}

export default PageTitle;
