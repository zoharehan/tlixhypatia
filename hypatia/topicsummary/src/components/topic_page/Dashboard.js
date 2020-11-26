import React, { Fragment } from "react";
import Topic from "./Topic";
// import Progress from "../../../../frontend/src/components/topic_page/Progress";
import Star from "./Star";
import RatingStars from "./RatingStars";

export default function Dashboard() {
  return (
    <Fragment>
      <RatingStars />
      <Topic />
      
    </Fragment>
  );
}
