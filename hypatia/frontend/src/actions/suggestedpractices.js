import axios from "axios";

import { GET_SUGGESTEDPRACTICES, DELETE_SUGGESTEDPRACTICES } from "./types";

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

//DELETE COMPLETED SUGGESTED PRACTICE QUESTIONS
export const deleteSuggestedPractices = (id) => (dispatch) => {
  axios
    .delete(`/suggestedpracticeapi/suggestedpractice/${id}/`)
    .then((res) => {
      dispatch({
        type: DELETE_SUGGESTEDPRACTICES,
        payload: id,
      });
    })
    .catch((err) => console.log(err));
};
