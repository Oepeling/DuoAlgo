import React from 'react';
import {Container, Nav, Navbar} from 'react-bootstrap';
import {Link} from 'react-router-dom';
import './NavBar.css';

class NavBar extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            loggedIn: false
        }
        // this.refreshLoggedIn = this.refreshLoggedIn.bind(this)
    }

    componentDidMount() {
        // this.refreshLoggedIn()
    }

    // refreshLoggedIn = () => {
    //     this.setState({loggedIn: Cookies.get('user_id') !== undefined})
    // }

    Item = ({section}) => {
        return (
            <div className={'Item'}>
                <h2>{section}</h2>
            </div>
        )
    }

    render() {
        return (
            <div className={'NavBarHelp'}>
                <Navbar className={'NavBar'}>
                    <Link to={'/'} className={'Left'}>
                        <this.Item section={'DuoAlgo'}/>
                    </Link>

                    <Link to={'/progress'} className={'Left'}>
                        <this.Item section={'Progress'}/>
                    </Link>

                    <Link to={'/account'} className={'Right'}>
                        <this.Item section={'Account'}/>
                    </Link>
                </Navbar>
            </div>
        )
    }
}

// const NavBar = () => {
//     return (
//         <Navbar variant={'dark'} className={'NavBar'} expand={'lg'} fixed={'top'}>
//             <Container fluid>
//                 <Navbar.Brand href={'/'} className={'Left'}>DuoAlgo</Navbar.Brand>
//
//                 <div className={'nav-items'}>
//                     <Navbar.Toggle aria-controls={'navbar-dark-example'}/>
//                     <Navbar.Collapse id={'navbar-dark-example'}>
//                         <Nav fill className={'padding-nav'}>
//                             <Nav.Item className={'Left'}>
//                                 <Nav.Link href={'/progress'}>
//                                     Progress
//                                 </Nav.Link>
//                             </Nav.Item>
//
//                             <Nav.Item>
//                                 <Nav.Link href={'/account'} className={'Right'}>
//                                     Account
//                                 </Nav.Link>
//                             </Nav.Item>
//                         </Nav>
//                     </Navbar.Collapse>
//                 </div>
//             </Container>
//         </Navbar>
//     )
// }

export default NavBar;
