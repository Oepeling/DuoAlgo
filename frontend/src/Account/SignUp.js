import React, {Component} from 'react';
import {Button, Form} from 'react-bootstrap';
import {Redirect} from 'react-router-dom';
import Email from './FormGroups/Email';
import Password from './FormGroups/Password';
import PasswordConfirm from './FormGroups/PasswordConfirm';
import LastName from './FormGroups/LastName';
import PhoneNo from './FormGroups/PhoneNo';
import Birthday from './FormGroups/Birthday';
import FirstName from './FormGroups/FirstName';
import axios from 'axios';

axios.defaults.xsrfCookieName = 'csrftoken'
axios.defaults.xsrfHeaderName = 'X-CSRFToken'

class SignUp extends Component {
    constructor(props) {
        super(props);
        this.state = {
            email: '',
            password: '',
            passwordConfirmation: '',
            firstName: '',
            lastName: '',
            phoneNo: '',
            birthday: null,
            invalidEmail: false,
            signedIn: false
        }
        this.handleChange = this.handleChange.bind(this)
        this.handleSubmit = this.handleSubmit.bind(this)
        this.signedIn = this.signedIn.bind(this)
        this.reset = this.reset.bind(this)
    }

    reset() {
        this.setState({
            invalidEmail: false,
            signedIn: false
        })
    }

    signedIn() {
        if (this.state.signedIn) {
            return <Redirect to='/login'/>
        }
    }

    validateForm() {
        return this.state.email.length > 0 &&
            this.state.password.length > 0 &&
            this.state.lastName.length > 0 &&
            this.state.firstName.length > 0
    }

    checkPassword() {
        if (this.state.password !== this.state.passwordConfirmation) {
            return <p className={'FormError'}>Cele doua parole nu se potrivesc</p>
        }
    }

    wrongEmail() {
        if (this.state.invalidEmail) {
            this.reset();
            return <p className={'FormError'}>Email-ul este deja asociat unui cont</p>
        }
    }

    handleChange = event => {
        let {name, value} = event.target
        this.setState({
            [name]: value
        })
    }

    handleSubmit = (event) => {
        console.log('HEEEI')
        this.reset()
        axios({
            method: 'post',
            url: 'add/user/',
            data: {
                'user_email': this.state.email,
                'user_password': this.state.password,
                'user_first_name': this.state.firstName,
                'user_last_name': this.state.lastName,
                'user_phone': this.state.phoneNo,
                'user_birthday': this.state.birthday.toISOString().split('T')[0],
                'user_gender': 'N'
            },
            headers: {
                'content-type': 'application/json'
            }
        }).then(result => {
            if (!result.data['added']) {
                this.setState({invalidEmail: true})
                console.log('email deja inregistrat')
            } else {
                this.setState({signedIn: true})
                console.log('ok')
            }
        }).catch(function (error) {
            console.log(error)
        })
        event.preventDefault()
    }

    render() {
        return (
            <div className={'sign-up-htm'}>
                <Form onSubmit={this.handleSubmit}>
                    <Email email={this.state.email}
                           handleChange={this.handleChange}
                           name={'signup'}/>
                    <Password password={this.state.password}
                              handleChange={this.handleChange}
                              name={'signup'}/>
                    <PasswordConfirm passwordConfirmation={this.state.passwordConfirmation}
                                     handleChange={this.handleChange}/>
                    <LastName lastName={this.state.lastName}
                              handleChange={this.handleChange}/>
                    <FirstName firstName={this.state.firstName}
                               handleChange={this.handleChange}/>
                    <PhoneNo phoneNo={this.state.phoneNo}
                             handleChange={this.handleChange}/>
                    <Birthday birthday={this.state.birthday}
                              handleChange={this.handleChange}/>
                    <Button block disabled={!this.validateForm()} type='submit' className={'button'}>
                        Sign Up
                    </Button>
                </Form>
                {this.checkPassword()}
                {this.wrongEmail()}
                {this.signedIn()}
            </div>
        )
    }
}

export default SignUp;
