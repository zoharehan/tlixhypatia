import axios from "axios";
import { GET_QUESTIONS, ADD_QUESTIONS } from "./types";

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

//ADD QUESTIONS

export const addQuestion = (question) => (dispatch) => {
  axios
    .post("/questionapi/question/", question)
    .then((res) => {
      dispatch({
        type: ADD_QUESTIONS,
        payload: res.data,
      });
    })
    .catch((err) => console.log(err));
};