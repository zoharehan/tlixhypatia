// this displays the log of all questions
// to work with redux from this componet

import React, { Component, Fragment } from "react";
import ReactDOM from 'react-dom'
import { connect } from "react-redux";
import PropTypes from "prop-types";
import {
  getSuggestedPractices,
  deleteSuggestedPractices,
} from "../../actions/suggestedpractices";


export class Practice extends Component {
  static PropTypes = {
    suggestedpractices: PropTypes.array.isRequired,
  };

  componentDidMount() {
    this.props.getSuggestedPractices();
  }

  // Count = () =>{
  //   const length = this.props.suggestedpractices.length;
  //   return length;
  // }
  
  render() {
    // const length = Count();
    return (
      <Fragment>
        <h2>Suggested Practice Questions</h2>
        {/* <p>the length is {length} </p> */}
        <table className="table table-striped table-bordered">
          <thead>
            <tr>
              <th>Questions Suggested</th>
              <th>Status</th>
            </tr>
          </thead>
          <tbody>
            {this.props.suggestedpractices.map((suggestedpracticee) => (
              <tr key={suggestedpracticee.id}>
                <td>{suggestedpracticee.question_suggested}</td>
                <td>
                  <button type="button" 
                  // class="btn btn-primary" id = "complete" 
                  // data-toggle="modal" data-target="#example"    
                  onClick={this.props.deleteSuggestedPractices.bind(
                       this, suggestedpracticee.id
                     )}
                     className="btn btn-success btn-sm"
                  >
                    {" "}
                    Mark as Complete
                  </button>

                  {/* <!-- Modal --> */}
                  <div class="modal fade" id="example" tabindex="-1" role="dialog" aria-labelledby="exampleModalLabel" aria-hidden="true">
                    <div class="modal-dialog" role="document">
                      <div class="modal-content">
                        <div class="modal-header">
                          <h5 class="modal-title" id="exampleModalLabel">Great</h5>
                          <button type="button" class="close" data-dismiss="modal" aria-label="Close">
                            <span aria-hidden="true">&times;</span>
                          </button>
                        </div>
                        <div class="modal-body">
                          Please confirm to add new question. 
                        </div>
                        <div class="modal-footer">
                          <button type="button" class="btn btn-secondary" data-dismiss="modal">Close</button>
                        </div>
                      </div>
                    </div>
                  </div>

                </td>
              </tr>
            ))}
          </tbody>
        </table>
      </Fragment>
    );
  }
}


export function add(x,y) {
  return x+y;
}

const mapStateToProps = (state) => ({
  suggestedpractices: state.suggestedpractices.suggestedpractices,
});

export default connect(mapStateToProps, {
  getSuggestedPractices,
  deleteSuggestedPractices,
})(Practice);
