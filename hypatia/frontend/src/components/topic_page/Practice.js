// this displays the log of all questions
// to work with redux from this componet

import React, { Component, Fragment } from "react";
import { connect } from "react-redux";
import PropTypes from "prop-types";
import { getSuggestedPractices } from "../../actions/suggestedpractices";

export class Practice extends Component {
  static PropTypes = {
    suggestedpractices: PropTypes.array.isRequired,
  };

  componentDidMount() {
    this.props.getSuggestedPractices;
  }

  render() {
    return (
      <Fragment>
        <h2>Log of sugprac</h2>
      </Fragment>
    );
  }
}
const mapStateToProps = (state) => ({
  suggestedpractices: state.suggestedpractices.suggestedpractices,
});

export default connect(mapStateToProps, { getSuggestedPractices })(Practice);
