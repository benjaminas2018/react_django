// import React from "react";
// import ReactDOM from "react-dom";
// import DataProvider from "./DataProvider";
// import Table from "./Tables";
// const App = () => (
//   <DataProvider endpoint="api/lead/" 
//                 render={data => <Table data={data} />} />
// );
// const wrapper = document.getElementById("app");
// wrapper ? ReactDOM.render(<App />, wrapper) : null;

import React, { Component, Fragment } from 'react';
import ReactDOM from 'react-dom';

import Header from './layout/Header';
import Dashboard from './leads/Dashboard';

import { Provider } from "react-redux";
import store from "../store";


class App extends Component {
  render() {
    return (
      <Provider store={store}>
        <Fragment>
            <Header />
            <div className="container">
              <Dashboard />
            </div>
        </Fragment>
      </Provider>
    );
  }
}

ReactDOM.render(<App />, document.getElementById('app'));