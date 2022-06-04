import {Form} from 'react-bootstrap';
import PropTypes from 'prop-types';
import React from 'react';

const PasswordConfirm = (props) => {
    return (
        <Form.Group className={'group'}>
            <Form.Label>Reintrodu parola</Form.Label>
            <Form.Control type='password'
                          name='passwordConfirmation'
                          value={props.passwordConfirmation}
                          onChange={props.handleChange}
                          placeholder='Parola'/>
        </Form.Group>
    )
}

PasswordConfirm.propTypes = {
    passwordConfirmation: PropTypes.string.isRequired,
    handleChange: PropTypes.func.isRequired
}

export default PasswordConfirm;
