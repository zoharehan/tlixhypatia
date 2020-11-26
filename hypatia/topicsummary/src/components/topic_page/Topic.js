import React, { Component, Fragment } from "react";
import { connect } from "react-redux";
import PropTypes from "prop-types";
import { getTopic } from "../../actions/topics";

export class Topic extends Component {
  static propTypes = {
    topics: PropTypes.array.isRequired,
  };

  componentDidMount() {
    this.props.getTopic();
  }

  render() {
    return (
      <Fragment>
        <div class="container" style={{ marginTop: "20px" }}>
          <b style={{ fontSize: 25 }}>Course Summary</b>
          {this.props.topics.map((topic) => (
            <div
              class="card-deck-wrapper"
              style={{ padding: "10px", marginBottom: 10, marginTop: 10 }}
            >
              <div class="card-deck">
                <div
                  class="card p-2"
                  style={{
                    borderRadius: "5px",
                    padding: "20px",
                    boxShadow: "2px 2px #e5e5e5",
                  }}
                >
                  <a
                    key={topic.id}
                    class="card-block"
                    href="https://sophysun.me"
                  >
                    <h5
                      class="card-title"
                      style={{
                        padding: "10px",
                        color: "black",
                        "& h4:hover": {
                          backgroundcolor: "pink",
                        },
                      }}
                    >
                      {topic.name}
                    </h5>
                  </a>
                </div>
              </div>
            </div>
          ))}
        </div>
      </Fragment>
    );
  }
}

const mapStateToProps = (state) => ({
  topics: state.topics.topics,
});

export default connect(mapStateToProps, { getTopic })(Topic);
// export default Topic;
// { this.props.topics.map(topic => (
//  <a key={topic.id} class="card-block" href="https://sophysun.me" >
//  ))}

// { this.props.topics.map(topic => (
//
// <h4 class="card-title"  style={{padding : '10px', color: 'black', '& h4:hover': {
//   backgroundcolor: 'pink',},}}>{topic.name}</h4>
//
//
// ))}

// </a>
// </div>
//
// </div>
// </div>

//       </Fragment>
//     );
//   }
// }
//
// const mapStateToProps = (state) => ({
//   topics: state.topics.topics,
// });
//
// export default connect(mapStateToProps, { getTopic })(Topic);
// // export default Topic;
