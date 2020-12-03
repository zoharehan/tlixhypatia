import React, { Component, Fragment } from "react";
import ReactDOM from "react-dom";

import Header from "./layout/Header";
import Dashboard from "./topic_page/Dashboard";

import { Provider } from "react-redux"; // connect redux to react through this provider
import store from "../store";

class App extends Component {
  render() {
    return (
      <Provider store={store}>
        <div style={{ backgroundColor: "#f5f5f5" }}>
          <Fragment>
            <Header />
            <div className="container">
              <Dashboard />
            </div>
          </Fragment>
        </div>
      </Provider>
    );
  }
}

ReactDOM.render(<App />, document.getElementById("app"));
