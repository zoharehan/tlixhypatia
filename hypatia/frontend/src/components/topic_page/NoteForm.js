import React, { Component } from 'react';
import { connect } from 'react-redux';
import PropTypes from 'prop-types';
import { addNotes } from "../../actions/notes";

export class NoteForm extends Component {
    state = {
        _notes: ""
    }

    static propTypes = {
        addNotes: PropTypes.func.isRequired
    }

    onChange = e => this.setState({ [e.target.name]: e.target.value });

    onSubmit = e => {
        e.preventDefault();
        //console.log(this.state);
        const { _notes } = this.state;
        const note = { _notes };
        this.props.addNotes(note);
    };

    render() {
        const{ notes } = this.state;
        return (
            <div className = "card card-body mt-4 mb-4">
                <h2>Add Note</h2>
                <form onSubmit={this.onSubmit}>
                    <div className="form-group">
                        <label>Message</label>
                        <input
                            className="form-control"
                            type="text"
                            name="_notes"
                            onChange={this.onChange}
                            value={notes}
                        />
                    </div>
                    <div className="form-group">
                        <button type="submit" className="btn btn-primary">
                            Submit
                        </button>
                    </div>
                </form>
            </div>
        )
    }
}

export default connect(null, { addNotes })(NoteForm);