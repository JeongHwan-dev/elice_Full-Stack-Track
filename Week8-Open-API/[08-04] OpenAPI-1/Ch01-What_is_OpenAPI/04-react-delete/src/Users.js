import React from 'react';
import axios from 'axios';

class Users extends React.Component {
    constructor(props) {
        super(props);
        this.state = { result: "" };
    }

    componentDidMount() {
        axios.delete('https://reqres.in/api/users/2')
            .then(response => {
                this.setState({result: response.status});
            });
    }

    render() {
        const { result } = this.state;
        return (
            <div>
                <h4>React Axios로 HTTP DELETE 요청하기</h4>
                <div>Status: {result}</div>
            </div>
        );
    }
}

export default Users;