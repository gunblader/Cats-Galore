import React from 'react';
import ContactList from './ContactList';

class App extends React.Component {
    render() {
        return (
            <div>
                <h1>Contact List</h1>
                <ContactList/>
            </div>
        )
    }
}

React.render(<App />, document.getElementById('app'));