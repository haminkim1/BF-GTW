window.addEventListener("load", function () {

    const emailAddressInput = document.querySelector("#email-address");

    async function ifCurrentEmailAddressExists() {
        emailAddressInput.addEventListener("input", async function() {
            let response = await fetch("/edit-account/email_address?email_address=" + emailAddressInput.value);
            let emailAddress = await response.json();
            console.log(emailAddress)
        })
        

    }

    async function ifCurrentUsernameExists() {

    }

    function displayWeaponNames() {
        input.addEventListener('input', async function() {
            autoCompleteList.innerHTML = "";

            let response = await fetch('/bfv/name?name=' + input.value);
            let weapons = await response.json();
            for (let i in weapons) {
                let name = weapons[i];
                autoCompleteList.innerHTML += `
                <div class="weapon-names">
                    <span class="clickableName green">${name}</span>
                </div>
                `;
            }
            
            sendNameToInputBoxIfClicked()
        });
    }
})



