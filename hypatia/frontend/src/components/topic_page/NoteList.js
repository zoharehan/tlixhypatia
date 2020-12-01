import React, { Component, Fragment } from "react";
import { connect } from "react-redux";
import PropTypes from "prop-types";
import { getNotes } from "../../actions/notes";
import Card from "react-bootstrap/Card";

export class NoteList extends Component {
  static propTypes = {
    notes: PropTypes.array.isRequired,
    //Add prop types for getNotes
  };

  componentDidMount() {
    this.props.getNotes();
  }

  render() {
    return (
      <Fragment>
        <h2>Notes</h2>
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
                  <th>Saved Notes</th>
                  <th />
                </tr>
              </thead>
              <tbody>
                {this.props.notes.map((note) => (
                  <tr key={note.id}>
                    <td>{note._notes}</td>
                    <td>
                      <button
                        className="btn btn-danger btn-sm"
                        style={{ borderRadius: "5px" }}
                      >
                        Delete
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
  notes: state.notes.notes,
});

export default connect(mapStateToProps, { getNotes })(NoteList);
