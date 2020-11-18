// meeting place for all your reducers
import { combineReducers } from "redux";
import questions from "./questions";
import suggestedpractices from "./suggestedpractices";

export default combineReducers({
  questions,
  suggestedpractices: suggestedpractices,
});
