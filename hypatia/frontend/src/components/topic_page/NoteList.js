import React, { Component, Fragment } from 'react';
import { connect } from 'react-redux';
import PropTypes from 'prop-types';
import { getNotes } from '../../actions/notes';

export class NoteList extends Component {
    static propTypes = {
        notes: PropTypes.array.isRequired
        //Add prop types for getNotes
    }

    componentDidMount() {
        this.props.getNotes();
    }

    render() {
        return (
            <Fragment>
                <h2>Notes</h2>
                <table className = "table table-stripped">
                    <thead>
                        <th>ID</th>
                        <th>Message</th>
                    </thead>
                    <tbody>
                        {this.props.notes.map(note => (
                            <tr key={note.id}>
                                <td>{note.id}</td>
                                <td>{note.message}</td>
                                <td><button classname="btn btn-danger btn-sm">Delete</button></td>
                            </tr>
                        ))}
                    </tbody>
                </table>
            </Fragment>
        )
    }
}

const mapStateToProps = state => ({
    notes: state.notes.notes
});

export default connect(mapStateToProps, {getNotes})(NoteList);
