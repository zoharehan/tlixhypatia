import React, { Component, Fragment } from "react";
import { connect } from "react-redux";
import PropTypes from "prop-types";
import { getNotes, deleteNotes } from "../../actions/notes";
import Card from "react-bootstrap/Card";

export class NoteList extends Component {
  static propTypes = {
    notes: PropTypes.array.isRequired,
    getNotes: PropTypes.func.isRequired,
    deleteNotes: PropTypes.func.isRequired,
  };

  componentDidMount() {
    this.props.getNotes();
  }

  render() {
    return (
      <Fragment>
        <Card
          style={{
            borderRadius: "5px",
            boxShadow: "2px 2px #e5e5e5",
            marginBottom: "20px",
            marginLeft: "20px",
            marginTop: "20px",
            flex: 0.7,
          }}
        >
          <Card.Body>
            <h2>Notes</h2>
            <table className="table table-stripped">
              <tbody>
                {this.props.notes.map((note) => (
                  <tr key={note.id}>
                    <td>{note._notes}</td>
                    <td>
                      <button
                        onClick={this.props.deleteNotes.bind(this, note.id)}
                        className="btn btn-danger btn-sm"
                        style={{ float: "right", borderRadius: "5px" }}
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

export default connect(mapStateToProps, { getNotes, deleteNotes })(NoteList);
