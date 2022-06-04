import React from 'react';
import PropTypes from 'prop-types';
import {Form} from 'react-bootstrap';

const PhoneNo = (props) => {
    return (
        <Form.Group className={'group'}>
            <Form.Label>Numar de telefon</Form.Label>
            <Form.Control type='text'
                          name='phoneNo'
                          value={props.phoneNo}
                          onChange={props.handleChange}
                          placeholder='Numar de telefon'/>
        </Form.Group>
    )
}

PhoneNo.propTypes = {
    phoneNo: PropTypes.string.isRequired,
    handleChange: PropTypes.func.isRequired
}

export default PhoneNo;
