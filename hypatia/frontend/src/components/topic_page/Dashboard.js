// this holds everything in the topics page (i.e. division page)
import React, { Fragment } from 'react';
import Log from './Log';
import NoteForm from './NoteForm';
import NoteList from './NoteList';


export default function Dashboard() {
    return (
        <Fragment>
            <Log />
            <NoteList/>
            <NoteForm />
        </Fragment>
    )
}
