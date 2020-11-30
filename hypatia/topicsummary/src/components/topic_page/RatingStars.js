import React, { useState } from 'react';
import Star from './Star';

const RatingStars = () => {
    const [gradeIndex, setGradeIndex] = useState();
    const GRADES = ['Not started', 'Just started', 'In Progress', 'Advanced', 'Completed'];
    const activeStar = {
        fill: 'blue'
    };

    const changeGradeIndex = ( index ) => {
        setGradeIndex(index);
    }

    return (
        <div className="container">
            <h5 className="result">{ GRADES[gradeIndex] ? GRADES[gradeIndex] : ""}</h5>
            <div className="stars">
                {
                    GRADES.map((grade, index) => (
                        <Star 
                            index={index} 
                            key={grade} 
                            changeGradeIndex={changeGradeIndex}
                            style={ gradeIndex > index ? activeStar : {} }
                        />
                    ))
                }
            </div>
        </div>
    );
}

export default RatingStars;