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

    let input = document.querySelector('#bfvInput');
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

    modalFunctionality()

    submitWeaponName()


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

                imageURL = data[0].encrypted_image_name
                weaponImage = document.querySelector("#weaponImage");
                weaponImage.src = `static/images/bfvImages/${imageURL}`;
                document.querySelector('#bfvInput').value = "";
            } catch (error) {
                console.error(error);
            }
          });
    }


    function updatePageAfterSubmission(URL) {
        // Update image to the next weapon image.
        weaponImage = document.querySelector("#weaponImage");
        weaponImage.src = `static/images/bfvImages/${URL}`;
        document.querySelector('#bfvInput').value = "";
    }

})



