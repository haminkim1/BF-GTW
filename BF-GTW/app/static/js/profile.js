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
        let table = document.getElementById("high-score-table");
        // Adding difficulty mode row headings. 
        table.innerHTML = `
        <thead>
            <tr id="high-score-table-columns">
                <th></th>
            </th>
        </thead>
        `
        let columnHeadings = document.getElementById("high-score-table-columns");
        for (let i in modes) {
            let difficulty = modes[i].first_letter_cap
            columnHeadings.innerHTML += `
            <th>${difficulty}</th>
            `
        }

        table.innerHTML += `
        <tbody id="high-score-body">
        </tbody>
        `
        let highScoreTableBody = document.getElementById("high-score-body");

        // Populating row of user's highscore in each difficulty mode for each BF game. 
        for (let i in data) {
            setHighScoreTableRows(highScoreTableBody, data[i].BF_game)
            // Populating score and date of each difficulty mode for each BF game. 
            rows = document.getElementById(`${data[i].BF_game}-rows`);
            for (let j in modes) {
                let difficulty = modes[j].mode
                populateHighScoreData(data[i].BF_game, difficulty, data[i].modes[difficulty]);
                populateHighScoreDates(data[i].BF_game, difficulty, data[i].date[difficulty]);      
            }     
        };
    }


    function setHighScoreTableRows(tableBody, BF_game) {
        tableBody.innerHTML += `
        <tr id="${BF_game}-rows">
            <th id="${BF_game}-heading" class="row-heading" rowspan="2">${BF_game}</th>
        </tr>
        `
        tableBody.innerHTML += `
        <tr id="${BF_game}-date-row">
        </tr>
        `
    }


    function populateHighScoreData(BF_game, difficulty, score) {
        rows = document.getElementById(`${BF_game}-rows`);
            rows.innerHTML += `
            <td id="${BF_game}-${difficulty}" class="score-cells"></td>
            `
            if (score !== null) {
                document.getElementById(`${BF_game}-${difficulty}`).innerText = `${score}`;
            }
    }


    function populateHighScoreDates(BF_game, difficulty, date) {
        let dateRow = document.getElementById(`${BF_game}-date-row`);
        dateRow.innerHTML += `
        <td id="${BF_game}-${difficulty}-date" class="date-cells"></td>
        `
        if (date !== null) {
            document.getElementById(`${BF_game}-${difficulty}-date`).innerText = `${date}`;
        }
    }
})



