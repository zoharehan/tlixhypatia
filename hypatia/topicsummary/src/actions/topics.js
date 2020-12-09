import axios from "axios";
import { GET_TOPICS } from "./types";

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
