import Chart from 'chart.js';
import axios from 'axios';
//import excludingWords from '../utils/constants/excludingWords';

const URL_WORD_DATA = 'http://localhost:3333/cleanword/';
let wordChart = null;

const fetchWord = (ref, numberOfWords) => {
    let words = [];
    let counts = [];
    axios.get(URL_WORD_DATA)
        .then(res => {
            if (wordChart != null) {
                wordChart.destroy();
            }
            let counter = 0;
            const wordFetched = res.data;
            while (words.length < numberOfWords) {
                console.log(wordFetched[counter].word);
                words.push(wordFetched[counter].word);
                counts.push(parseInt(wordFetched[counter].count));
                counter += 1;
            }
            wordChart = new Chart(ref.current, {
                type: 'bar',
                data: {
                    labels: words,
                    datasets: [{
                        data: counts,
                    }]
                },
                options: {
                    responsive: true,
                }
            })
        })
        .catch(err => {
            console.log(err);
        });
}

export default fetchWord;
