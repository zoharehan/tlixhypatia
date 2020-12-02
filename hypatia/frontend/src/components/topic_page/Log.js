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
          {this.props.questions.map((question) => (
            <div class="card-deck-wrapper" style={{ padding: "10px" }}>
              <div class="card-deck">
                <div
                  class="card"
                  style={{
                    borderRadius: "5px",
                    boxShadow: "2px 2px #e5e5e5",
                    padding: "5px",
                  }}
                >
                  <h5 style={{ padding: "5px" }}>Question Prompt:</h5>
                  <h6
                    class="card-title"
                    style={{
                      marginLeft: "5px",
                      color: "black",
                      "& h4:hover": {
                        backgroundcolor: "pink",
                      },
                    }}
                  >
                    {question.question_prompt}
                  </h6>
                  <div className="details-line" style={{ clear: "both" }}>
                    <h6
                      style={{
                        marginLeft: "5px",
                        float: "left",
                      }}
                    >
                      Topic: {question.topic_type}
                    </h6>
                    <h6
                      style={{
                        marginLeft: "5px",
                        marginRight: "5px",
                        float: "right",
                      }}
                    >
                      Submission Time: {question.created_at}
                    </h6>
                  </div>
                </div>
              </div>
            </div>
          ))}
        </Card>
      </Fragment>
    );
  }
}

const mapStateToProps = (state) => ({
  questions: state.questions.questions,
});

export default connect(mapStateToProps, { getQuestion })(Log);
