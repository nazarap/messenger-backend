import React from 'react';
import SignIn from './signin.jsx';
import SignUp from './signup.jsx';

export default class LoginContent extends React.Component {
    render() {
        return (
            <div>
                <header className="login-header"></header>
                <SignIn/>
                <SignUp/>
            </div>
        )
    }
}