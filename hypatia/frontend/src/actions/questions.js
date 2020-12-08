import axios from "axios";
import { GET_QUESTIONS } from "./types";

var path = window.location.pathname.split('/')[2]

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
