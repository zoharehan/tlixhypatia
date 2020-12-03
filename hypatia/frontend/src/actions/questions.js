// any action we want to fire off goes in here
// this where make all of our HTTP requests

import axios from "axios";
import { GET_QUESTIONS } from "./types";

//GET QUESTIONS
// from question api created earlier

var path = window.location.pathname.split('/')[2]

console.log(path);

export const getQuestion = () => (dispatch) => {
  axios
    .get(`/questionapi/question?topic_type=${path}`)
    .then((res) => {
      dispatch({
        type: GET_QUESTIONS,
        payload: res.data,
      });
    })
    .catch((err) => console.log(err));
};
