import React, { useState, useEffect } from 'react';
import ReactDOM from 'react-dom';
import reportWebVitals from '../reportWebVitals';

import axios from 'axios';

const URL_DATA = 'http://localhost:3333/postdata/';

function Post() {
    const [data, setData] = useState([]);

    useEffect(() => {
        const fetchData = async () => {
            const result = await axios(
                URL_DATA,
            );
            setData(result.data);
        };
        fetchData();
    }, []);
    

    return (
        <div>
            <ul>
                {data.map(post =>(
                    <li key={post.id}>
                        <p>{post.title}</p>
                    </li>
                ))}
            </ul>
        </div>
    );
};

export default Post;