import axios from "axios";

import { GET_SUGGESTEDPRACTICES } from "./types";

//GET SUGGESTED_PRACTICES
export const getSuggestedPractices = () => (dispatch) => {
  axios
    .get("/suggestedpracticeapi/suggestedpractice/")
    .then((res) => {
      dispatch({
        type: GET_SUGGESTEDPRACTICES,
        payload: res.data,
      });
    })
    .catch((err) => console.log(err));
};
