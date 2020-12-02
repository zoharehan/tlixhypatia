import axios from 'axios';

import { GET_NOTES, DELETE_NOTES, ADD_NOTES } from './types';

// GET NOTES
export const getNotes = () => dispatch => {
    axios.get('/noteapi/notes/')
        .then(res => {
            dispatch({
                type: GET_NOTES,
                payload: res.data
            });
        }).catch(err => console.log(err));
};

// DELETE NOTES
export const deleteNotes = (id) => dispatch => {
    axios.delete(`/noteapi/notes/${id}/`)
        .then(res => {
            dispatch({
                type: DELETE_NOTES,
                payload: id
            });
        }).catch(err => console.log(err));
};

// ADD NOTES
export const addNotes = (note) => dispatch => {
    axios.post('/noteapi/notes/', note)
        .then(res => {
            dispatch({
                type: ADD_NOTES,
                payload: res.data
            });
        }).catch(err => console.log(err));
};