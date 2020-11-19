// meeting place for all your reducers
import { combineReducers } from 'redux';
import questions from './questions';
import notes from './notes';

export default combineReducers({
    questions,
    notes
});
