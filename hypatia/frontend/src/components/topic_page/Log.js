// this displays the log of all questions
// to work with redux from this componet

import React, { Component, Fragment } from 'react';
import { connect } from 'react-redux';
import PropTypes from 'prop-types';
import { getQuestion } from '../../actions/questions';

export class Log extends Component {
    static propTypes = {
        questions: PropTypes.array.isRequired,
    };

    componentDidMount() {
        this.props.getQuestion();
    }

    render() {
        return (
            <Fragment>
               <h2>Log of questions</h2>
               <table className="table table-striped">
                 <thead >
                     <tr>
                         <th>Question Prompt</th>
                         <th>Question Type</th>
                         <th>Date Created</th>
                     </tr>
                 </thead>
                 <tbody>
                    { this.props.questions.map(question => (
                        <tr key={question.id}>
                            <td>{question.question_prompt}</td>
                            <td>{question.topic_type}</td>
                            <td>{question.created_at}</td>
                        </tr>
                    ))}
                 </tbody>
               </table>
            </Fragment>
        )
    }
}

const mapStateToProps = (state) => ({
    questions: state.questions.questions,
});

export default connect(mapStateToProps, { getQuestion })(Log);
