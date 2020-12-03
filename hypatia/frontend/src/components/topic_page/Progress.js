import React, { Component } from "react";
import { ProgressBar } from "react-bootstrap";
import Practice from "./Practice";
import len from "./Practice";
import { connect } from "react-redux";
import PropTypes from "prop-types";
import { getQuestion } from "../../actions/questions";

export class Progress extends Component {
  constructor() {
    super();
    this.state = {
      percentage: 0,
    };
  }

  static propTypes = {
    questions: PropTypes.array.isRequired,
  };

  componentDidMount() {
    this.props.getQuestion();
  }

  percentageLimits = (min, value, max) => {
    return Math.min(Math.max(min, value), max);
  };

  // clickMe = () => {
  //   this.setState({ percentage: this.state.percentage + 25 });
  //   const requestOptions = {
  //     method: "GET",
  //     headers: { "Content-Type": "application/json" },
  //     // body: JSON.stringify({ title: 'StudentName' })
  //   };
  //   fetch("/progressapi/progress/").then(handleRedirect);
  // };
  // handleRedirect = (res) => {
  //   if (res.status === 200) {
  //     // redirect here
  //     window.location.href = "/progressapi/progress/";
  //   } else {
  //     // Something went wrong here
  //   }
  // };

  render() {
    const k = this.props.questions.length;
    return (
      <div style={{ marginBottom: 30, marginTop: 30 }}>
        <h2>Your Progress</h2>
        <ProgressBar
          now={this.percentageLimits(0, k * 10, 100)}
          style={{
            height: 25,
            borderRadius: 25,
            marginBottom: "5px",
            marginTop: "5px",
            boxShadow: "2px 2px #e5e5e5",
          }}
        />
        {/* <button onClick={this.clickMe}>Next</button> */}
      </div>
    );
  }
}

const mapStateToProps = (state) => ({
  questions: state.questions.questions,
});

export default connect(mapStateToProps, { getQuestion })(Progress);
