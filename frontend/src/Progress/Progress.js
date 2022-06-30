import React from 'react';
import {Link} from 'react-router-dom';
import './Progress.css';

const LessonCard = ({lesson}) => {
    console.log(lesson)
    return (
        // <div className={'lesson lesson-' + lesson.status}>
        <div className={'LessonCard'}>
            <p>{lesson.title}</p>
            <p>{lesson.author}</p>
            <p>{lesson.topic}</p>
        </div>
    )
}


const Progress = ({lessons}) => {
    lessons.sort(function(a, b) {
        if (a.stage == b.stage) {
            return a.level - b.level;
        } else {
            return a.stage - b.stage;
        }
    });
    return (
        <div className={'LessonsList'}>
            <ul>
                {lessons.map((item, index) =>
                    <div key={'lesson-' + item.id}>
                        {item.status === 0 &&
                        <LessonCard lesson={item}/>}

                        {item.status > 0 &&
                        <Link key={item.id} to={'lesson/' + item.id}>
                            <LessonCard lesson={item}/>
                        </Link>}
                    </div>
                )}
            </ul>
        </div>
    )
}

// Progress.propTypes = {
//     lessons: PropTypes.array.isRequired
// }

export default Progress;
