window.addEventListener("load", function () {

    // changing class within body tag in layout.html whenever bfv.html loads. 
    // the function loads devastation.webp instead of having a black background. 
    const background = document.querySelector(".background");
    background.classList.remove("background");
    
    const parentDiv = document.querySelector(".parentDiv");
    parentDiv.classList.add("bfv-main")

    const changeToShadowClass = document.querySelector(".changeToShadowClass");
    changeToShadowClass.className = '';
    changeToShadowClass.classList.add("shadow")

    const autoCompleteList = document.querySelector("#autoCompleteList");

    let input = document.querySelector('input');
    input.addEventListener('input', async function() {
        autoCompleteList.innerHTML = "";
        let response = await fetch('/bfv?name=' + input.value);
        let weapons = await response.json();
        // After fetching API data, display those names in a list below the input box 
        let html = '';
        for (let i in weapons) {
            let name = weapons[i];
            html += `<span class="clickableName white">` + name + `</span>`;
        }
        autoCompleteList.innerHTML += html;
        
        sendNameToInputBoxIfClicked()
    });

    function sendNameToInputBoxIfClicked() {
        let clickableName = document.getElementsByClassName("clickableName");

        for (let i = 0; i < clickableName.length; i++) {
            clickableName[i].addEventListener("click", function() {
                let text = this.innerText;
                document.getElementById("bfvInput").value = text;
                autoCompleteList.innerHTML = "";   
            })
        }
    }
})



