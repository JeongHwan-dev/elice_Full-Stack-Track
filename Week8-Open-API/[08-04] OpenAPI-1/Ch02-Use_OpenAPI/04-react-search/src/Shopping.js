import React from 'react';
import axios from 'axios';

class Shopping extends React.Component {
    constructor(props) {
        super(props);
        this.state = { 
            search: '',         // <input> 태그에 저장된 검색어가 저장
            goods: null          // goods에는 반환데는 데이터가 아래에 대한 map() 함수를 적용한 뒤 저장
        };
    }

    handleChange = e => {
        this.setState({ search: e.target.value });
    }

    // 버튼 클릭 시 입력된 검색어로 GET 요청을 하고 반환된 결과를 출력 가능한 형태로 state에 저장
    handleClick = e => {
        const CLIENT_ID = 'i3KmWAjQSNqdPnkBXfcW';
        const CLIENT_SECRET = 'creOaz9WWI';

        axios.get('https://cors-anywhere.herokuapp.com/https://openapi.naver.com/v1/search/shop',
            { params: { query: this.state.search },
              headers: { 'X-Naver-Client-Id': CLIENT_ID, 'X-Naver-Client-Secret': CLIENT_SECRET }
            }
        )
            .then(response => {
                const result = response.data.items;
                const sortedResult = result.map((good, index) => (
                    <li key={index} dangerouslySetInnerHTML={{__html: good.title}} />
                ));
                this.setState({ goods: sortedResult });
            })
    }

    render() {
        return (
            <div>
                <h4>상품 검색</h4>
                <input onChange={this.handleChange} />
                <button onClick={this.handleClick}>검색</button>
                <div>{this.state.goods}</div>
            </div>
        );
    }
}

export default Shopping;