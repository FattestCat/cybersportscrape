import Chart from 'chart.js';
import axios from 'axios';
//import excludingWords from '../utils/constants/excludingWords';

let wordChart = [];

const fetchWord = (id, ref, numberOfWords, url) => {
    let words = [];
    let counts = [];
    //console.log('0.1');
    axios.get(url)
        .then(res => {
            if (wordChart[id] != null) {
                wordChart[id].destroy();
            }
            //console.log('0.2');
            console.log(res.data);
            let counter = 0;
            const wordFetched = res.data.results;
            while (words.length < numberOfWords) {
                console.log(wordFetched[counter].word);
                words.push(wordFetched[counter].word);
                counts.push(parseInt(wordFetched[counter].count));
                counter += 1;
            }
            //console.log('0.3');
            wordChart[id] = new Chart(ref.current, {
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
