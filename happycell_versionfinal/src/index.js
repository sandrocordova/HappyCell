import "./polyfills";
import React from "react";
import ReactDOM from "react-dom";

import * as serviceWorker from "./serviceWorker";

import { HashRouter } from "react-router-dom";
import "./assets/base.scss";
import App from "./App";

import { Provider } from "react-redux";
import { store } from './redux/store';

const rootElement = document.getElementById("root");

const renderApp = (Component) => {
  ReactDOM.render(
    <Provider store={store}>
      <HashRouter>
        <Component />
      </HashRouter>
    </Provider>,
    rootElement
  );
};

renderApp(App);
/*
if (module.hot) {
  module.hot.accept("./DemoPages/Main", () => {
    const NextApp = require("./DemoPages/Main").default;
    renderApp(NextApp);
  });
}*/
serviceWorker.unregister();