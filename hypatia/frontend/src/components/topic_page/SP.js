// this displays the log of all questions
// to work with redux from this componet

import React, { Component, Fragment } from "react";
import { connect } from "react-redux";
import PropTypes from "prop-types";
import { getSuggestedPractice } from "../../actions/suggestedpractices";

export class SP extends Component {
  static propTypes = {
    suggestedpractices: PropTypes.array.isRequired,
  };

  componentDidMount() {
    this.props.getSuggestedPractice();
  }

  render() {
    return (
      <Fragment>
        <h2>Suggested Questions</h2>
        <table className="table table-striped table-bordered">
          <thead>
            <tr>
              <th>Question Prompt</th>
            </tr>
          </thead>
          <tbody>
            {this.props.suggestedpractices.map((suggestedpractice) => (
              <tr key={suggestedpractice.id}>
                <td>{suggestedpractice.question_suggested}</td>
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

export default connect(mapStateToProps, { getSuggestedPractice })(SP);
