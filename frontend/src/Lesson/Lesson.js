import React from 'react';
import ReactMarkdown from 'react-markdown';
import remarkMath from 'remark-math';
import rehypeKatex from 'rehype-katex';
import remarkGfm from 'remark-gfm';
import rehypeRaw from 'rehype-raw'

import {lessonInfo} from '../Queries';

class Lesson extends React.Component {
    constructor(props) {
        super(props)
        console.log(props)
        this.state = {
            id: props['lesson_id'],
            title: "",
            author: "",
            stage: 0,
            level: 0,
            topic: "",
            prerequisites: [],
            status: 1,
            content: "",
            tasks: [],
            link_to_code: ""
        }
    }

    componentDidMount() {
        lessonInfo(this.state.id).then(lesson => {
            this.setState({
                title: lesson.title,
                author: lesson.author,
                stage: lesson.stage,
                level: lesson.level,
                topic: lesson.topic,
                prerequisites: lesson.prerequisites,
                status: lesson.status,
                content: lesson.content,
                tasks: lesson.tasks,
                link_to_code: lesson.link_to_code
            })
        })
    }

    render() {
        return (
            <div>
                <h1>{this.state.title}</h1>
                <h2>{this.state.author}</h2>
                <h3>{this.state.topic}</h3>

                <ReactMarkdown
                    children={this.state.content}
                    remarkPlugins={[remarkMath, remarkGfm]}
                    rehypePlugins={[rehypeKatex, rehypeRaw]}
                />

                <p>{this.state.link_to_code}</p>

                {/*<ul>*/}
                {/*    {lesson.problems.items.map((item, index) =>*/}
                {/*        <a key={'problems-' + index} target={'_blank'} href={item} rel='noreferrer'>*/}
                {/*            {item}*/}
                {/*        </a>*/}
                {/*    )}*/}
                {/*</ul>*/}

                <button>Mark as done</button>
            </div>
        )
    }
}

// const Lesson = ({lesson}) => {
//     return (
//         <div>
//             <h1>{lesson.title}</h1>
//             <h2>{lesson.author}</h2>
//             {/*<p>{lesson.content}</p>*/}
//
//             {/*<ul>*/}
//             {/*    {lesson.problems.items.map((item, index) =>*/}
//             {/*        <a key={'problems-' + index} target={'_blank'} href={item} rel='noreferrer'>*/}
//             {/*            {item}*/}
//             {/*        </a>*/}
//             {/*    )}*/}
//             {/*</ul>*/}
//
//             <button>Mark as done</button>
//         </div>
//     )
// }

export default Lesson;
