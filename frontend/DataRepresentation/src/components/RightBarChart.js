
import {useEffect, useRef, useState} from 'react';
import fetchWord from '../utils/fetching';

const URL_WORD_DOT_DATA = 'http://localhost:3333/cleanworddot/';

const RightBarChart = () => {
    const rightChartRef = useRef(null);
    const [renderedNumberOfWords, setRenderedNumberOfWords] = useState(14);
    let numberOfWords = 14;

    useEffect(() => fetchWord(1, rightChartRef, renderedNumberOfWords, URL_WORD_DOT_DATA), [renderedNumberOfWords]);

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
                ref={rightChartRef}
                id="rightbarchart"
                aria-label="Right bar chart"
                role="img"
            />
        </div>
    )
}

export default RightBarChart;
