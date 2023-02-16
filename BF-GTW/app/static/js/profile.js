window.addEventListener("load", function () {
    getHighScoreData()


    async function getHighScoreData() {
        try {
            const response = await fetch("/profile/highscore");
            let data = await response.json();
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
        <tr id="high-score-table-columns">
            <th></th>
        </th>
        `
        columnHeadings = document.getElementById("high-score-table-columns");
        for (let i in modes) {
            columnHeadings.innerHTML += `
            <th>${modes[i].first_letter_cap}</th>
            `
        }

        // Adding row of user's highscore in each difficulty mode for each BF game. 
        for (let i in data) {
            table.innerHTML += `
            <tr id="${data[i].BF_game}-rows">
                <th id="${data[i].BF_game}-heading">${data[i].BF_game}</th>
            </tr>
            `
            rows = document.getElementById(`${data[i].BF_game}-rows`);
            for (let j in modes) {
                rows.innerHTML += `
                <td id="${data[i].BF_game}-${modes[j].mode}"></td>
                `
            }

            if (data[i].modes.easy !== null) {
                document.getElementById(`${data[i].BF_game}-easy`).innerText = `${data[i].modes.easy}`;
            }
            if (data[i].modes.medium !== null) {
                document.getElementById(`${data[i].BF_game}-medium`).innerText = `${data[i].modes.medium}`;
            }
            if (data[i].modes.hard !== null) {
                document.getElementById(`${data[i].BF_game}-hard`).innerText = `${data[i].modes.hard}`;
            }
        };
    }
})



