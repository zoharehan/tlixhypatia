import {
  GET_SUGGESTEDPRACTICES,
  DELETE_SUGGESTEDPRACTICES,
} from "../actions/types.js";

const initialState = {
  suggestedpractices: [],
};

export default function (state = initialState, action) {
  switch (action.type) {
    case GET_SUGGESTEDPRACTICES:
      return {
        ...state,
        suggestedpractices: action.payload,
      };
    case DELETE_SUGGESTEDPRACTICES:
      return {
        ...state,
        suggestedpractices: state.suggestedpractices.filter(
          (suggestedpractice) => suggestedpractice.id !== action.payload
        ),
      };
    default:
      return state;
  }
}
