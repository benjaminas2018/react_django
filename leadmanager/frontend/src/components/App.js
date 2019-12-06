import React, { Component, Fragment } from "react";
import ReactDOM from "react-dom";

import { transitions, positions, Provider as AlertProvider } from "react-alert";
import AlertTemplate from "react-alert-template-basic";

import Header from "./layout/Header";
import Dashboard from "./leads/Dashboard";
import Alerts from "./layout/Alerts";

import { Provider } from "react-redux";
import store from "../store";

// optional cofiguration
const options = {
  // you can also just use 'bottom center'
  position: positions.TOP_CENTER,
  timeout: 5000,
  offset: "30px",
  // you can also just use 'scale'
  transition: transitions.SCALE
};

class App extends Component {
  render() {
    return (
      <Provider store={store}>
        <AlertProvider template={AlertTemplate} {...options}>
          <Fragment>
            <Header />
            <Alerts />
            <div className="container">
              <Dashboard />
            </div>
          </Fragment>
        </AlertProvider>
      </Provider>
    );
  }
}

ReactDOM.render(<App />, document.getElementById("app"));
