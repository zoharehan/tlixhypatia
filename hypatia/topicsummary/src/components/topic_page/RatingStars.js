import React, { useState } from 'react';
import Star from './Star';

const RatingStars = () => {
    const [gradeIndex, setGradeIndex] = useState();
    const GRADES = ['Not started', 'Just started', 'In Progress', 'Advanced', 'Completed'];
    const activeStar = {
        fill: 'yellow'
    };

    const changeGradeIndex = ( index ) => {
        setGradeIndex(index);
    }

    return (
        <div className="container">
            <h1 className="result">{ GRADES[gradeIndex] ? GRADES[gradeIndex] : ""}</h1>
            <div className="stars">
                {
                    GRADES.map((grade, index) => (
                        <Star 
                            index={index} 
                            key={grade} 
                            changeGradeIndex={changeGradeIndex}
                            style={ gradeIndex > index ? activeStar : {}}
                        />
                    ))
                }
            </div>
        </div>
    );
}

export default RatingStars;