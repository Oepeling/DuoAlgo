import React from 'react';
import {BrowserRouter as Router, Redirect, Route} from 'react-router-dom';

import Account from './Account/Account';
import Progress from './Progress/Progress';
import Lesson from './Lesson/Lesson';

import {lessonList} from './Queries';
import './App.css';
import NavBar from "./Navbar/NavBar";

class App extends React.Component {
    constructor(props) {
        super(props)
        this.state = {
            lessons: []
        }
    }

    componentDidMount() {
        this.setState({lessons: []})
        lessonList().then(lessons => {
            this.setState({lessons})
            // console.log("lesson_list", lessons)
            // console.log(this.state.lessons)
        })
    }

    render() {
        return (
            <Router className={'App'}>
                <NavBar/>

                <div className={'AppPage'}>
                    {/*<Route exact path={'/'}>*/}
                    {/*    <Redirect to={'/account'}/>*/}
                    {/*</Route>*/}
                    <Route path={'/account'}> <Account/> </Route>
                    <Route path={'/progress'}> <Progress lessons={this.state.lessons}/> </Route>

                    {this.state.lessons.map(lesson =>
                        <Route key={lesson.id} path={'/lesson/' + lesson.id}>
                            <Lesson lesson_id={lesson.id}/>
                        </Route>
                    )}
                </div>
            </Router>
        )
    }
}

export default App;
