import React from 'react';
import axios from 'axios';

class Users extends React.Component {
    constructor(props) {
        super(props);
        this.state = { result: "" };
    }

    componentDidMount() {
        // axios.get을 호출하고 result에 반환되는 데이터 저장
        axios.get('https://reqres.in/api/users/2')
            .then(response => {
                this.setState({ result: response.data.data });
            });
    }

    render() {
        const { result } = this.state;
        return (
            <div>
                <h3>React Axios로 HTTP GET 요청하기</h3>
                <div>
                    Name: {result.first_name} {result.last_name}
                    <br />
                    Email: {result.email}
                </div>
            </div>
        )
    }
}

export default Users;