import React from 'react';
import axios from 'axios';

class Users extends React.Component {
    constructor(props) {
        super(props);
        this.state = { result: "" };
    }

    componentDidMount() {
        // 삽입할 데이터 객체 선언
        const data = { "email": "eve.holt@reqres.in", "password": "cityslicka" };
        axios.post('https://reqres.in/api/login', data)
            .then(response => {
                this.setState({ result: response.data.token });
            });
    }

    render() {
        const { result } = this.state;
        return (
            <div>
                <h4>React Axios로 HTTP POST 요청하기</h4>
                <div>
                    Token: {result}
                </div>
            </div>
        );
    }
}

export default Users;