import axios from "axios";

import { GET_SUGGESTEDPRACTICES } from "./types";

//GET SUGGESTED_PRACTICES
export const getSuggestedPractices = () => (dispatch) => {
  axios
    .get("http://127.0.0.1:8000/suggestedpracticeapi/suggestedpractice/")
    .then((res) => {
      dispatch({
        type: GET_SUGGESTEDPRACTICES,
        payload: res.data,
      });
    })
    .catch((err) => console.log(err));
};
