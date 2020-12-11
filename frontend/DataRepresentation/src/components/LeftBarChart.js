import {useEffect, useRef} from 'react';
import fetchWord_new from '../utils/fetching';


const LeftBarChart = () => {
    const leftChartRef = useRef(null);


    useEffect(() => fetchWord_new(leftChartRef, 20), []);

    return (
        <div>
            <form>
                <input type="text" />
                <input type="submit" value="Submit" />
            </form>
            <canvas ref={leftChartRef}
                id="leftbarchart"
                aria-label="Left bar chart"
                role="img" />
        </div>
    )
}

export default LeftBarChart;
