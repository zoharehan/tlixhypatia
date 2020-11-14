// any action we want to fire off goes in here
// this where make all of our HTTP requests

import axios from "axios";
import { GET_SUGGESTEDPRACTICE } from "./types";

//GET SUGGESTEDPRACTICE
// from suggestedpractice api created earlier

export const getSuggestedPractice = () => (dispatch) => {
  axios
    .get("/suggestedpractice/suggestedpractice/")
    .then((res) => {
      dispatch({
        type: GET_SUGGESTEDPRACTICE,
        payload: res.data,
      });
    })
    .catch((err) => console.log(err));
};
