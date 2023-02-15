window.addEventListener("load", function () {
    getHighScoreData()



    async function getHighScoreData() {
        let table = document.getElementById("high-score-table");
        try {
            const response = await fetch("/profile/highscore");
            let highScores = await response.json();

            table.innerHTML = "";
            table.innerHTML = `
            <tr>
                <th></th>
                <th>Easy</th>
                <th>Medium</th>
                <th>Hard</th>
            </th>
            `
            for (let i in highScores) {
                table.innerHTML += `
                <tr>
                    <th>${highScores[i].BF_game}</th>
                    <td class="high-score-cells">${highScores[i].easy}</th>
                    <td class="high-score-cells">${highScores[i].medium}</th>
                    <td class="high-score-cells">${highScores[i].hard}</th>
                </tr>
                `
            };

            // let highScoreCells = document.querySelectorAll(".high-score-cells");
            // console.log(highScoreCells[0].textContent);
            
            // for (let i in highScoreCells) {
            //     if (highScoreCells[i].textContent === null) {
            //         highScoreCells[i].innerHTML = `<td class="high-score-cells">1</td>`;
            //     }
            // }

 
        } catch (error) {
            console.error(error);
        }
    }
})



