import React, { Component, Fragment } from "react";
import { connect } from "react-redux";
import PropTypes from "prop-types";
import { getTopic } from "../../actions/topics";

export class Topic extends Component {
  //   static propTypes = {
  //     topics: PropTypes.array.isRequired,
  //   };

  //   componentDidMount() {
  //     this.props.getTopic();
  //   }

  render() {
    return (
      <Fragment>
        <h2>Topics</h2>
      </Fragment>
    );
  }
}

// const mapStateToProps = (state) => ({
//   topics: state.topics.topics,
// });

// export default connect(mapStateToProps, { getTopic })(Topic);
export default Topic;
