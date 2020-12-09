// evaluate function and send out states

import { GET_QUESTIONS, ADD_QUESTIONS } from "../actions/types.js";

const initalState = {
  questions: [],
};

export default function (state = initalState, action) {
  switch (action.type) {
    case GET_QUESTIONS:
      return {
        ...state,
        questions: action.payload,
      };
    case ADD_QUESTIONS:
      return {
        ...state,
        questions: [...state.questions, action.payload]
      }
    default:
      return state;
  }
}
