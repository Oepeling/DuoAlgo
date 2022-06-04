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
        this.refreshLessons()
    }

    refreshLessons = () => {
        lessonList().then(
            result => this.setState({
                lessons: result
            }))
    }

    render() {
        return (
            <Router id={'App'}>
                <NavBar/>

                <Route exact path={'/'}>
                    <Redirect to={'/account'}/>
                </Route>
                <Route path={'/account'}> <Account/> </Route>
                <Route path={'/progress'}> <Progress lessons={this.state.lessons}/> </Route>

                {this.state.lessons.map(lesson =>
                    <Route key={lesson.id} path={'/lesson/' + lesson.id}>
                        <Lesson lesson={lesson}/>
                    </Route>
                )}
            </Router>
        )
    }
}

export default App;
