import React from 'react';
import {Container, Nav, Navbar} from 'react-bootstrap';

const NavBar = () => {
    return (
        <Navbar variant={'dark'} className={'nav-color'} expand={'lg'} fixed={'top'}>
            <Container fluid>
                <Navbar.Brand href={'/'}>Duolearn</Navbar.Brand>

                <div className={'nav-items'}>
                    <Navbar.Toggle aria-controls={'navbar-dark-example'}/>
                    <Navbar.Collapse id={'navbar-dark-example'}>
                        <Nav fill className={'padding-nav'}>
                            <Nav.Item>
                                <Nav.Link href={'/progress'}>
                                    Progress
                                </Nav.Link>
                            </Nav.Item>

                            <Nav.Item>
                                <Nav.Link href={'/account'}>
                                    Account
                                </Nav.Link>
                            </Nav.Item>
                        </Nav>
                    </Navbar.Collapse>
                </div>
            </Container>
        </Navbar>
    )
}

export default NavBar;
