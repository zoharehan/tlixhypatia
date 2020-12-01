// this displays the log of all questions
// to work with redux from this componet

import React, { Component, Fragment } from "react";
import { connect } from "react-redux";
import PropTypes from "prop-types";
import { getQuestion } from "../../actions/questions";
import Card from "react-bootstrap/Card";

export class Log extends Component {
  static propTypes = {
    questions: PropTypes.array.isRequired,
  };

  componentDidMount() {
    this.props.getQuestion();
  }

  render() {
    return (
      <Fragment>
        <h2>Questions Completed</h2>
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
                  <th>Question Prompt</th>
                  <th>Question Type</th>
                  <th>Completion Date</th>
                </tr>
              </thead>
              <tbody>
                {this.props.questions.map((question) => (
                  <tr key={question.id}>
                    <td>{question.question_prompt}</td>
                    <td>{question.topic_type}</td>
                    <td>{question.created_at}</td>
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
  questions: state.questions.questions,
});

export default connect(mapStateToProps, { getQuestion })(Log);
