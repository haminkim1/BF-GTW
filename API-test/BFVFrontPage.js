window.addEventListener("load", function () {
    async function displayBFV() {
        let bfvStats = await fetch(`https://api.gametools.network/bfv/weapons/?format_values=true&name=HAMINATOR1997&platform=pc&skip_battlelog=false&lang=en-us`);
        let bfvArray = await bfvStats.json();
        displayJSONString(bfvArray.weapons[0].image);

            displayPartialArticleOnPage(bfvArray.weapons[0].weaponName);

    }

    function displayPartialArticleOnPage(articleObj) {
        let articleDivElement = document.createElement("div");

        articleDivElement.innerHTML = `
        <h3 class=article-title">${articleObj.weapons[0].weaponName}`;

        // let articlesDiv = document.querySelector("#article-inner");
        // articlesDiv.appendChild(articleDivElement);
    }

    function displayJSONString(jsonArray) {
        let jsonString = JSON.stringify(jsonArray);
        let jsonDiv = document.querySelector("#json-string");
        jsonDiv.innerText = jsonString;

        let image = document.createElement("p");
        image.src = bfvArray.weapons[0].image;
    }

    displayBFV();
});