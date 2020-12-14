import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
//import App from './App';
//import reportWebVitals from './reportWebVitals';
import LeftBarChart from './components/LeftBarChart';
import RightBarChart from './components/RightBarChart';
//import Post from './components/Post';

ReactDOM.render(
    <LeftBarChart />,
    document.getElementById('leftbarchart')
)

ReactDOM.render(
    <RightBarChart />,
    document.getElementById('rightbarchart')
)

// ReactDOM.render(
//   <React.StrictMode>
//     <App />
//   </React.StrictMode>,
//   document.getElementById('root')
// );



// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals

//reportWebVitals();
