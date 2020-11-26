import React, { Component } from "react";
import { ProgressBar } from "react-bootstrap";
import Practice from "./Practice";
import len from "./Practice";
import { connect } from "react-redux";
import PropTypes from "prop-types";
import {
  getSuggestedPractices,
  deleteSuggestedPractices,
} from "../../actions/suggestedpractices";

export class Progress extends Component {
  constructor() {
    super();
    this.state = {
      percentage: 0,
      // Change this to sth in the database. Django has to have some way to pass to react.
    };
  }
  static PropTypes = {
    suggestedpractices: PropTypes.array.isRequired,
  };

  componentDidMount() {
    this.props.getSuggestedPractices();
  }

  percentageLimits = (min, value, max) => {
    return Math.min(Math.max(min, value), max);
  };

  clickMe = () => {
    this.setState({ percentage: this.state.percentage + 25 });
    const requestOptions = {
      method: "GET",
      headers: { "Content-Type": "application/json" },
      // body: JSON.stringify({ title: 'StudentName' })
    };
    fetch("/progressapi/progress/").then(handleRedirect);
  };
  handleRedirect = (res) => {
    if (res.status === 200) {
      // redirect here
      window.location.href = "/progressapi/progress/";
    } else {
      // Something went wrong here
    }
  };

  render() {
    const k = this.props.suggestedpractices.length; //this is where the length is coming from
    return (
      <div style={{ marginBottom: 30, marginTop: 30 }}>
        <ProgressBar
          now={this.percentageLimits(0, this.state.percentage, 100)}
          style={{
            height: 25,
            borderRadius: 25,
            marginBottom: "5px",
            boxShadow: "2px 2px #e5e5e5",
          }}
        />
        <button onClick={this.clickMe}>Next</button>
      </div>
    );
  }
}

//this is the connection function to get suggestedpractices into our component, uses redux

const mapStateToProps = (state) => ({
  suggestedpractices: state.suggestedpractices.suggestedpractices,
});

export default connect(mapStateToProps, {
  getSuggestedPractices,
})(Progress);
