// evaluate function and send out states

import { GET_SUGGESTEDPRACTICE } from "../actions/types.js";

const initalState = {
  suggestedpractice: [],
};

export default function (state = initalState, action) {
  switch (action.type) {
    case GET_SUGGESTEDPRACTICE:
      return {
        //the spread operator that returns everything that may be in the initial state
        ...state,
        suggestedpractice: action.payload,
      };
    default:
      return state;
  }
}
