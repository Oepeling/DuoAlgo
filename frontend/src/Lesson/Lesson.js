import React from 'react';

const Lesson = (props) => {
    return (
        <div>
            <h1>{props.title}</h1>
            <h2>{props.author}</h2>
            <p>{props.lesson}</p>

            <ul>
                {props.problems.items.map((item, index) =>
                    <a key={'problems-' + index} target={'_blank'} href={item} rel='noreferrer'>
                        {item}
                    </a>
                )}
            </ul>

            <button>Mark as done</button>
        </div>
    )
}

export default Lesson;
