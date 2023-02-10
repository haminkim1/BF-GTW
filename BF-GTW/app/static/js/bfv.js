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
    const input = document.querySelector('#bfvInput');
    // Fetching weapon names via API as user types the input box and display the names 
    // matching with the text typed in the input box as a list below the input box 
    // e.g. typing 12 will show 12g automatic as a list. 
    input.addEventListener('input', async function() {
        autoCompleteList.innerHTML = "";
        let response = await fetch('/bfv/name?name=' + input.value);
        let weapons = await response.json();
        let html = '';
        for (let i in weapons) {
            let name = weapons[i];
            html += `<span class="clickableName white">` + name + `</span>`;
        }
        autoCompleteList.innerHTML += html;
        
        sendNameToInputBoxIfClicked()
    });

    modalFunctionality();
    submitWeaponName();
    activateHintFeature();


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


    function modalFunctionality() {   
        document.getElementById("submit-form").addEventListener("submit", function(event) {
            event.preventDefault();
            startBtn = document.querySelector("#start-btn");
            startBtn.style.visibility = "hidden";
            startBtn.disabled = true;


            document.getElementById("myModal").style.display = "none";
        });
    }


    // Submits name from input textbox and changes to next weapon image. 
    async function submitWeaponName() {
        document.getElementById("submitWeaponNameBtn").addEventListener("click", async function(event) {
            event.preventDefault();
            let formData = new FormData(event.target.form);
            try {
                const response = await fetch("/bfv/check_results", {
                    method: "POST",
                    body: formData
                });
                const data = await response.json();
                console.log(data)

                // If user won the game, redirect to gameover page
                if (data.current_weapon == data.total_weapons) {
                    window.location.replace("/");
                }

                // If user has 0 lives, redirect to gameover page
                if (data.lives == 0) {
                    window.location.replace("/");
                }

                updatePageAfterSubmission(data)
            } catch (error) {
                console.error(error);
            }
          });
        
        // If user presses enter instead of clicking submit, the function makes it as if the user 
        // has clicked submit instead. 
        document.getElementById("bfvInput").addEventListener("keypress", function (event) {
            if (event.key === "Enter") {
                console.log("test");
                event.preventDefault();
                document.getElementById("submitWeaponNameBtn").click();
                autoCompleteList.innerHTML = ""; 
            }
        })
    }


    // After user clicks submit on the this.clientInformation, the function is executed to:
        // Display next weapon image
        // Clear the input textbox
        // Update the score
        // Update number of weapons left
        // Update number of hints and lives
    function updatePageAfterSubmission(data) {
        weaponImage = document.querySelector("#weaponImage");
        weaponImage.src = `static/images/bfvImages/${data.weapon}`;

        document.querySelector('#bfvInput').value = "";
        document.querySelector(".score").innerHTML = `Score: ${data.current_score}`;
        document.querySelector(".current-weapon").innerHTML = `Current weapon: ${data.current_weapon}/${data.total_weapons}`;
        document.querySelector(".lives").innerHTML = `Lives: ${data.lives}`;
        document.querySelector(".hints").innerHTML = `Hints: ${data.hints}`;
        document.querySelector("#hint_display").innerHTML = ``;
        document.querySelector("#hintBtn").disabled = false;
    }

    
    async function activateHintFeature() {
        const hintBtn = document.getElementById("hintBtn");
        hintBtn.addEventListener("click", async function(event) {
            event.preventDefault();
            try {
                const response = await fetch("/bfv/hint", {
                    method: "POST"
                })
                const data = await response.json();
                // data.hints, weapon_type and first_letter will only be undefined if user attempt to click hint button when there are 0 hints left. 
                if (Object.keys(data).length !== 0) {
                    hintBtn.innerHTML = `Hints: ${data.hints}`;
                    document.getElementById("hint_display").innerHTML = `<span id="hint_weapon_name">${data.weapon_type}.</span>`;
                    document.getElementById("hint_display").innerHTML += `
                    <span id="">First letter starts with ${data.first_letter}</span>`;
                }
                
                // Prevents user from clicking hint button more than once in the same round. 
                hintBtn.disabled = true;
            } catch (error) {
                console.error(error);
            }
        })
    }
})



