import { combineReducers } from "redux";
import questions from "./questions";
import suggestedpractices from "./suggestedpractices";
import notes from './notes';

export default combineReducers({
  questions,
  notes,
  suggestedpractices: suggestedpractices,
});
