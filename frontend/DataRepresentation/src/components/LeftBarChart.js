import {useEffect, useRef, useState} from 'react';
import fetchWord from '../utils/fetching';

const LeftBarChart = () => {
    const leftChartRef = useRef(null);
    const [renderedNumberOfWords, setRenderedNumberOfWords] = useState(15);
    let numberOfWords = 15;

    useEffect(() => fetchWord(leftChartRef, renderedNumberOfWords), [renderedNumberOfWords]);

    const handleSubmit = (e) => {
        e.preventDefault();
        console.log('inside handleSubmit');
        setRenderedNumberOfWords(numberOfWords);
    }

    return (
        <div>
            <form onSubmit={handleSubmit}>
                <input
                    type="text"
                    onChange={(e) => {
                        numberOfWords = parseInt(e.target.value);
                        console.log(numberOfWords);
                    }}
                />
                <input
                    type="submit"
                    value="Go"
                />
            </form>
            <canvas
                ref={leftChartRef}
                id="leftbarchart"
                aria-label="Left bar chart"
                role="img"
            />
        </div>
    )
}

export default LeftBarChart;
