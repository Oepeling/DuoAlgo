import React from 'react';
import {Link} from 'react-router-dom';

const LessonCard = (lesson) => {
    return (
        <div className={'lesson lesson-' + lesson.status}>
            <p>{lesson.title}</p>
            <p>{lesson.author}</p>
        </div>
    )
}

const Progress = (lessons) => {
    return (
        <div>
            <ul>
                {lessons.items.map((item, index) =>
                    <div key={'lesson-' + index}>
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

export default Progress;
