import Chart from 'chart.js';
import axios from 'axios';

const URL_WORD_DATA = 'http://localhost:3333/word/';

const fetchWord_new = (ref, numberOfWords) => {
    let words = [];
    let counts = [];
    axios.get(URL_WORD_DATA)
        .then(res => {
            console.log(res.data.slice(0, numberOfWords));
            const wordFetched = res.data.slice(0, numberOfWords);
            for (const Word of wordFetched) {
                words.push(Word.word);
                counts.push(parseInt(Word.count))
            };
            const wordChart = new Chart(ref.current, {
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
            console.log(wordChart);

        })
        .catch(err => {
            console.log(err);
        });
}

export default fetchWord_new;
