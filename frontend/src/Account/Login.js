import React, {Component} from 'react';
import {Button, Form} from 'react-bootstrap';
// noinspection ES6CheckImport
import {Redirect} from 'react-router-dom';
import Password from './FormGroups/Password';
import Email from './FormGroups/Email';
import axios from 'axios';
import Cookies from 'js-cookie';

axios.defaults.xsrfCookieName = 'csrftoken'
axios.defaults.xsrfHeaderName = 'X-CSRFToken'

class Login extends Component {
    constructor(props) {
        super(props)
        this.state = {
            email: '',
            password: '',
            wrongEmail: false,
            wrongPassword: false,
            loggedIn: false
        }
        this.handleChange = this.handleChange.bind(this)
        this.handleSubmit = this.handleSubmit.bind(this)
        this.refreshLoggedIn = this.refreshLoggedIn.bind(this)
    }

    componentDidMount() {
        this.refreshLoggedIn()
    }

    refreshLoggedIn = () => {
        this.setState({loggedIn: Cookies.get('user_id') !== undefined})
    }

    reset() {
        this.setState({
            wrongEmail: false,
            wrongPassword: false,
            loggedIn: false
        })
    }

    wrongEmail() {
        if (this.state.wrongEmail)
            return <p className={'FormError'}>Email gresit</p>
    }

    wrongPassword() {
        if (this.state.wrongPassword)
            return <p className={'FormError'}>Parola gresita</p>
    }

    loggedIn() {
        if (this.state.loggedIn)
            return <Redirect to='/saloane'/>
    }

    validateForm() {
        return this.state.email.length > 0 && this.state.password.length > 0
    }

    handleChange = event => {
        let {name, value} = event.target
        this.setState({
            [name]: value
        })
    }

    handleSubmit = (event) => {
        this.reset();
        axios({
            method: 'post',
            url: 'user/login/',
            data: {
                'user_email': this.state.email,
                'user_password': this.state.password
            },
            headers: {
                'content-type': 'application/json'
            }
        }).then(result => {
            if (!result.data['check_user']) {
                this.setState({wrongEmail: true})
                console.log('email gresit')
            } else if (!result.data['check_password']) {
                this.setState({wrongPassword: true})
                console.log('parola gresita')
            } else {
                this.setState({loggedIn: true})
                Cookies.set('user_id', result.data['user_id'], {expires: 7})
                console.log('ok')
            }
        }).catch(function (error) {
            console.log(error)
        })
        event.preventDefault()
    }

    render() {
        return (
            <div className={'sign-in-htm'}>
                <Form onSubmit={this.handleSubmit}>
                    <Email email={this.state.email}
                           handleChange={this.handleChange}
                           name={'login'}/>
                    <Password password={this.state.password}
                              handleChange={this.handleChange}
                              name={'login'}/>
                    <Button block disabled={!this.validateForm()} type='submit' className={'button'}>
                        Login
                    </Button>
                </Form>
                {this.wrongEmail()}
                {this.wrongPassword()}
                {this.loggedIn()}
            </div>
        )
    }
}

export default Login;
