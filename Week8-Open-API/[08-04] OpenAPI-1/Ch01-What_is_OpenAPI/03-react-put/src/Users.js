import React from 'react';
import axios from 'axios';

class Users extends React.Component {
    constructor(props) {
        super(props);
        this.state = { result: "" };
    }

    componentDidMount() {
        // 수정할 데이터 선언
        const updateData = { "first_name": "White", "last_name": "Rabbit", "email": "alice@elice.io" };
        axios.put('https://reqres.in/api/users/2', updateData)
            .then(response => {
                this.setState({ result: response.data });
            });
    }

    render() {
        const { result } = this.state;
        return (
            <div>
                <h4>React Axios로 HTTP PUT 요청하기</h4>
                <div>
                    Name: {result.first_name + " " + result.last_name}
                    <br />
                    Email: {result.email}
                    <br />
                    Update Date: {result.updatedAt}
                </div>
            </div>
        );
    }
}

export default Users;