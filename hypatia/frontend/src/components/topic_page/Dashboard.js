// this holds everything in the topics page (i.e. division page)
import React, { Fragment } from "react";
import Log from "./Log";
import Practice from "./Practice";
import Progress from "./Progress";
import NoteForm from './NoteForm';
import NoteList from './NoteList';

export default function Dashboard() {
  return (
    <Fragment>
      <Progress />
      <Log />
      <Practice />
      <NoteList/>
      <NoteForm />
    </Fragment>
  );
}
