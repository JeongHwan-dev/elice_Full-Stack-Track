import React from 'react';
import axios from 'axios';

class Messages extends React.Component {
    constructor(props) {
        super(props);
        this.state = { result: "" };
    }

    componentDidMount() {
        // 백엔드 API 주소 
        axios.get('https://cors-anywhere.herokuapp.com/https://백엔드 주소')
            .then(response => this.setState({
                result: response.data.result.message
            }));
    }

    render() {
        const { result } = this.state;
        return (
            <div>
                <h5>HTTP GET 요청</h5>
                <div>Message: {result}</div>
            </div>
        )
    }
}

export default Messages;