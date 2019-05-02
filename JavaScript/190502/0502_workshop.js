// const data = {??}
// url = 'http://13.125.249.144:8080/daejeon/2/posts/'
// axios.post(url, data)


const axios = require('axios');

const url = 'http://13.125.249.144:8080/ssafy/daejeon/2/posts'

const data = {
    "post": {
        'title': 'umm',
        'content': 'dae ddaa',
        'author': 'Aciel Aunt',
    } 
}
axios.post(url, data)
axios.get(url)
    .then(res => {
        console.log(res.data.posts)
    })