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
import Card from "react-bootstrap/Card";

function rowStyleFormat(row, rowIdx) {
  return { backgroundColor: rowIdx % 2 === 0 ? "red" : "blue" };
}

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
        <Card
          style={{
            borderRadius: "5px",
            boxShadow: "2px 2px #e5e5e5",
            marginTop: "15px",
            marginBottom: "20px",
          }}
        >
          <Card.Body>
            <table className="table table-striped">
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
                        style={{ borderRadius: "5px" }}
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
          </Card.Body>
        </Card>
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
