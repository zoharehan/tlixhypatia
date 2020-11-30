// this displays the log of all questions
// to work with redux from this component

import React, { Component, Fragment } from "react";
import { connect } from "react-redux";
import PropTypes from "prop-types";
import {
  getSuggestedPractices,
  deleteSuggestedPractices,
} from "../../actions/suggestedpractices";
import suggestedpractices from "../../reducers/suggestedpractices";

export class Practice extends Component {
  static PropTypes = {
    suggestedpractices: PropTypes.array.isRequired,
  };

  componentDidMount() {
    this.props.getSuggestedPractices();
  }

  render() {
    return (
      <Fragment>
        <h2>Suggested Practice Questions</h2>
        <table className="table table-striped table-bordered">
          <thead>
            <tr>
              <th>Questions Suggested</th>
              <th>Status</th>
            </tr>
          </thead>
          <tbody>
            {this.props.suggestedpractices.map((suggestedpractice) => (
              <tr key={suggestedpractice.id}>
                <td>{suggestedpractice.question_suggested}</td>
                <td>
                  <button
                    onClick={this.props.deleteSuggestedPractices.bind(
                      this,
                      suggestedpractice.id
                    )}
                    className="btn btn-success btn-sm"
                  >
                    {" "}
                    Mark as Complete
                  </button>
                </td>
              </tr>
            ))}
          </tbody>
        </table>
      </Fragment>
    );
  }
}
const mapStateToProps = (state) => ({
  suggestedpractices: state.suggestedpractices.suggestedpractices,
});

export default connect(mapStateToProps, {
  getSuggestedPractices,
  deleteSuggestedPractices,
})(Practice);
