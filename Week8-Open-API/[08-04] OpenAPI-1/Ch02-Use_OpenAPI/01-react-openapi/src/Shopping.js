import React from 'react';
import axios from 'axios';

class Shopping extends React.Component {
    constructor(props) {
        super(props);
        this.state = { result: [] };
    }

    componentDidMount() {
        const CLIENT_ID = 'i3KmWAjQSNqdPnkBXfcW';
        const CLIENT_SECRET = 'creOaz9WWI';
        axios.get('https://cors-anywhere.herokuapp.com/https://openapi.naver.com/v1/search/shop',
            { params: { query: '컴퓨터' },
              headers: {'X-Naver-Client-Id': CLIENT_ID, 'X-Naver-Client-Secret': CLIENT_SECRET}
            }
        )
            .then(response => {
                this.setState({ result: response.status });
            });
    }

    render() {
        const { result } = this.state;
        return (
            <div>
                <h4>HTTP 상태 코드</h4>
                <div>
                    {result}
                </div>
            </div>
        );
    }
}

export default Shopping;