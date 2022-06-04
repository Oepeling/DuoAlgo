import React from 'react';
import PropTypes from 'prop-types';
import {Form} from 'react-bootstrap';

const FirstName = (props) => {
    return (
        <Form.Group className={'group'}>
            <Form.Label className={'label'}>Prenume</Form.Label>
            <Form.Control type='text'
                          name='firstName'
                          value={props.firstName}
                          onChange={props.handleChange}
                          placeholder='Prenume'/>
        </Form.Group>
    )
}

FirstName.propTypes = {
    firstName: PropTypes.string.isRequired,
    handleChange: PropTypes.func.isRequired
}

export default FirstName;
