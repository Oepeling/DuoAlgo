import {Form} from 'react-bootstrap';
import PropTypes from 'prop-types';
import React from 'react';

const Email = (props) => {
    return (
        <Form.Group className={'group'}>
            <Form.Label>Email</Form.Label>
            <Form.Control autoFocus
                          type='email'
                          name='email'
                          placeholder='Email'
                          value={props.email}
                          onChange={props.handleChange}/>
        </Form.Group>
    )
}

Email.propTypes = {
    email: PropTypes.string.isRequired,
    handleChange: PropTypes.func.isRequired
}

export default Email;
