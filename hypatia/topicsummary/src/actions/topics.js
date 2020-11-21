// any action we want to fire off goes in here
// this where make all of our HTTP requests

import axios from "axios";
import { GET_TOPICS } from "./types";

//GET QUESTIONS
// from question api created earlier

export const getTopic = () => (dispatch) => {
  axios
    .get("/topicapi/topic/")
    .then((res) => {
      dispatch({
        type: GET_TOPICS,
        payload: res.data,
      });
    })
    .catch((err) => console.log(err));
};
