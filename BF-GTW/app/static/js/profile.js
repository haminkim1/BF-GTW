window.addEventListener("load", function () {
    getHighScoreData()


    async function getHighScoreData() {
        try {
            const response = await fetch("/profile/highscore");
            const data = await response.json();
            const highScores = data.highScores;
            const modes = data.modes;
            populateHighScoreTable(highScores, modes);
        } catch (error) {
            console.error(error);
        }
    }


    function populateHighScoreTable (data, modes) {
        console.log(data)
        let table = document.getElementById("high-score-table");
        // Adding difficulty mode row headings. 
        table.innerHTML = `
        <tr id="high-score-table-columns">
            <th></th>
        </th>
        `
        columnHeadings = document.getElementById("high-score-table-columns");
        for (let i in modes) {
            let difficulty = modes[i].first_letter_cap
            columnHeadings.innerHTML += `
            <th>${difficulty}</th>
            `
        }

        // Adding row of user's highscore in each difficulty mode for each BF game. 
        for (let i in data) {
            table.innerHTML += `
            <tr id="${data[i].BF_game}-rows">
                <th id="${data[i].BF_game}-heading" rowspan="2">${data[i].BF_game}</th>
            </tr>
            `
            rows = document.getElementById(`${data[i].BF_game}-rows`);
            for (let j in modes) {
                let difficulty = modes[j].mode
                rows.innerHTML += `
                <td id="${data[i].BF_game}-${difficulty}"></td>
                `
                if (data[i].modes[difficulty] !== null) {
                    document.getElementById(`${data[i].BF_game}-${difficulty}`).innerText = `${data[i].modes[difficulty]}`;
                }
                // table.innerHTML += `
                // <tr id="date-row">
                // </tr>
                // `
                // let dateRow = document.getElementById(`${data[i].BF_game}-date-row`);
                // console.log(data[i].BF_game);
                // dateRow.innerHTML += `
                // <td id=${data[i].BF_game}-${difficulty}-date"></td>
                // `
            }     

            // if (data[i].date !== null) {
            //     document.getElementById(`${data[i].BF_game}-${difficulty}-date`).innerText = `${data[i].date}`;
            // }    
//             <table>
//   <tr>
//     <th rowspan="2">Row Heading</th>
//     <td>Cell 1</td>
//     <td>Cell 2</td>
//   </tr>
//   <tr>
//     <td>Cell 3</td>
//     <td>Cell 4</td>
//   </tr>
// </table>
        };
    }
})



