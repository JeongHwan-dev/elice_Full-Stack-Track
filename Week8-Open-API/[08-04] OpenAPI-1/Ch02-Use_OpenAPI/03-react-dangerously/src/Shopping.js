import React from 'react';
import axios from 'axios';

class Shopping extends React.Component {
    constructor(props) {
        super(props);
        this.state = { result: [] };
    }

    componentDidMount() {
        // 자신의 OpenAPI 키
        const CLIENT_ID = '';
        const CLIENT_SECRET = '';

        axios.get('https://cors-anywhere.herokuapp.com/https://openapi.naver.com/v1/search/shop', 
            { 
              params: { query: '컴퓨터' },
              headers: { 'X-Naver-Client-Id': CLIENT_ID, 'X-Naver-Client-Secret': CLIENT_SECRET }
            }
        )
            .then(response => {
                this.setState({ result: response.data.items });
            });
    }

    render() {
        const { result } = this.state;
        const goods = result.map((good, index) => (
            // 기존 코드: <li key={index}>{good.title}</li>
            <li key={index} dangerouslySetInnerHTML={{__html: good.title}}></li>
        ));

        return (
            <div>
                <h4>상품 리스트</h4>
                <div>{goods}</div>
            </div>
        );
    }
}

export default Shopping;