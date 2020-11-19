// this displays the log of all questions
// to work with redux from this componet

import React, { Component, Fragment } from 'react';
import { connect } from 'react-redux';
import PropTypes from 'prop-types';
import { getTopic } from '../../actions/topics';

export class Log_summary extends Component {
    static propTypes = {
        topics: PropTypes.array.isRequired,
    };

    componentDidMount() {
        this.props.getTopic();
    }

    render() {
        return (
            <Fragment>
               <h2>Log of topics</h2>
               <table className="table table-striped table-bordered">
                 <thead >
                     <tr>
                         <th>Topic Name</th>
                         
                     </tr>
                 </thead>
                 <tbody>
                    { this.props.topics.map(topic => (
                        <tr key={topic.id}>
                            <td>{topic.name}</td>
                            
                        </tr>
                    ))}
                 </tbody>
               </table>
            </Fragment>
        )
    }
}

const mapStateToProps = (state) => ({
    topics: state.topics.topics,
});

export default connect(mapStateToProps, { getTopic })(Log_summary);
