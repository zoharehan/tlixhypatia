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
import axios from 'axios';
import { addQuestion } from "../../actions/questions";

export class Practice extends Component {
  static PropTypes = {
    suggestedpractices: PropTypes.array.isRequired,
    addQuestion: PropTypes.func.isRequired
  };

  componentDidMount() {
    this.props.getSuggestedPractices();
  }


  // state = {
  //   question_suggested = "",
  //   topic_most_missed = "",
  // };

  deleteAndPost(suggestedpractice){
    this.props.deleteSuggestedPractices.bind(
      this,
      suggestedpractice.id
    )

    // const question = {
    //   "question_prompt": suggestedpractice.question_suggested,
    //   "topic_type": suggestedpractice.topic_most_missed
    // }
    // axios.post('http://127.0.0.1:8000/questionapi/question/', question)

    //this.props.addQuestion(question);

  }

  // QUESTIONAPI_ENDPOINT = 'http://127.0.0.1:8000/questionapi/question/'

  // question_data = {
  //     "question_prompt": question_prompt,
  //     "topic_type": topic_type
  // }

  // r = requests.post(url=QUESTIONAPI_ENDPOINT, data=question_data)

  //OnClick = axios.post(url='http://127.0.0.1:8000/questionapi/question/', data=suggestedpractice)

  // this.deleteAndPost(suggestedpractice)

  //addquestion.bind(parameter)


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
          {this.props.suggestedpractices.map((suggestedpractice) => (
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
                    {suggestedpractice.question_suggested}
                  </h6>
                  <h6
                    style={{
                      marginLeft: "5px",
                      float: "left",
                    }}
                  >
                    Topic: {suggestedpractice.topic_most_missed}
                  </h6>
                  <button
                    style={{
                      borderRadius: "5px",
                      width: "80px",
                      height: "30px",
                      position: "absolute",
                      top: "35px",
                      right: "30px",
                    }}
                    // onClick={this.props.addQuestion({
                    //     "question_prompt": suggestedpractice.question_suggested,
                    //     "topic_type": suggestedpractice.topic_most_missed
                    //   })}
                    className="btn btn-success btn-sm"
                  >
                    {" "}
                    Completed
                  </button>
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
  suggestedpractices: state.suggestedpractices.suggestedpractices,
});

export default connect(mapStateToProps, {
  getSuggestedPractices,
  deleteSuggestedPractices, 
  addQuestion
})(Practice);
