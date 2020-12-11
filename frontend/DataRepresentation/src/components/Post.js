import React, {useState, useEffect} from 'react';
//import ReactDOM from 'react-dom';
//import reportWebVitals from '../reportWebVitals';

import LeftBarChart from './LeftBarChart';

//const URL_DATA = 'http://localhost:3333/postdata/';
//const URL_WORD_DATA = 'http://localhost:3333/word/';

function Post() {
    //const [data, setData] = useState([]);
    //const [word, setWord] = useState([]);

    //useEffect(() => {
    //const fetchData = async () => {
    //const result = await axios(
    //URL_DATA,
    //);
    //setData(result.data);
    //};
    //fetchData();
    //}, []);

    //useEffect(
    //() => {
    //const fetchWord = async () => {
    //const result = await axios(
    //URL_WORD_DATA,
    //);
    //setWord(result.data.slice(0, 20));
    //};
    //fetchWord();

    //}
    //, []);

    return (
        <LeftBarChart />
    );
};

export default Post;
