window.addEventListener("load", function () {
    getHighScoreData()


    async function getHighScoreData() {
        try {
            const response = await fetch("/profile/highscore");
            let data = await response.json();
            const highScores = data.highScores;
            const BFGame = data.BF_games;
            const modes = data.modes;
            console.log(highScores)
            console.log(BFGame);
            console.log(modes);
            populateHighScoreTable(highScores);
        } catch (error) {
            console.error(error);
        }
    }


    function populateHighScoreTable (data) {
        let table = document.getElementById("high-score-table");
        table.innerHTML = `
        <tr>
            <th></th>
            <th>Easy</th>
            <th>Medium</th>
            <th>Hard</th>
        </th>
        `
        for (let i in data) {
            table.innerHTML += `
            <tr>
                <th id="BF-game-heading">${data[i].BF_game}</th>
                <td id="${data[i].BF_game}-easy"></td>
                <td id="${data[i].BF_game}-medium"></td>
                <td id="${data[i].BF_game}-hard"></td>
            </tr>
            `
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



