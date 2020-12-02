import React, { Component } from "react";
import { connect } from "react-redux";
import PropTypes from "prop-types";
import { addNotes } from "../../actions/notes";

export class NoteForm extends Component {
  state = {
    _notes: "",
  };

  static propTypes = {
    addNotes: PropTypes.func.isRequired,
  };

  onChange = (e) => this.setState({ [e.target.name]: e.target.value });

  onSubmit = (e) => {
    e.preventDefault();
    //console.log(this.state);
    const { _notes } = this.state;
    const note = { _notes };
    this.props.addNotes(note);
  };

  render() {
    const { notes } = this.state;
    return (
      <div
        className="card card-body"
        style={{
          borderRadius: "5px",
          boxShadow: "2px 2px #e5e5e5",
          marginBottom: "20px",
          marginTop: "20px",
        }}
      >
        <h2>Add a Note</h2>
        <form onSubmit={this.onSubmit}>
          <div className="form-group">
            <h6>Something for Future You!</h6>
            <input
              className="form-control align-content-start"
              style={{ height: 250, alignContent: "start" }}
              type="text"
              name="_notes"
              onChange={this.onChange}
              value={notes}
            />
          </div>
          <div className="form-group">
            <button
              type="submit"
              className="btn btn-primary"
              style={{ float: "right", borderRadius: "5px" }}
            >
              Submit
            </button>
          </div>
        </form>
      </div>
    );
  }
}

export default connect(null, { addNotes })(NoteForm);
