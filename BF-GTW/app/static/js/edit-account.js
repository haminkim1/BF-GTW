window.addEventListener("load", function () {

    const emailAddressInput = document.querySelector("#email-address");
    // const currentEmailAddress = emailAddressInput.value;

    const usernameInput = document.querySelector("#username");
    // const currentUsername = usernameInput.value;

    const emailExistStatus = ifCurrentEmailAddressExists();
    const usernameExistStatus = ifCurrentUsernameExists();

    if (emailExistStatus == true || usernameExistStatus == true) {
        // disable submission
    }
    else {
        // enable submission
    }

    function ifCurrentEmailAddressExists() {
        emailAddressInput.addEventListener("input", async function() {
            let response = await fetch("/edit-account/check_email_exist?email_address=" + emailAddressInput.value);
            let emailExists = await response.json();
            console.log(emailExists)
            return emailExists;
        })
    }

    function ifCurrentUsernameExists() {
        usernameInput.addEventListener("input", async function() {
            let response = await fetch("/edit-account/check_username_exist?username=" + usernameInput.value);
            let username = await response.json();
            console.log(username)
            return username;
        })
    }
})



