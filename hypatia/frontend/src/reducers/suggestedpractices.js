import { GET_SUGGESTEDPRACTICES } from "../actions/types.js";

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
    default:
      return state;
  }
}
