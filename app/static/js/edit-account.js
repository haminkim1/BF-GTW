window.addEventListener("load", function () {

    const emailAddressInput = document.querySelector("#email-address");
    const usernameInput = document.querySelector("#username");
    const editAccountBtn = document.querySelector("#edit-account-btn");

    let emailExists = false;
    let usernameExists = false;
    ifEmailAndUsernameExist();

    
    function ifEmailAndUsernameExist() {
        const debouncedEmailAddressAPI = debounce(async function() {
            let response = await fetch("/edit-account/check_email_exist?email_address=" + emailAddressInput.value);
            let status = await response.json();
            emailExists = status.emailExists;
            updateSubmitButton();
        }, 500);

        const debouncedUsernameAPI = debounce(async function() {
            let response = await fetch("/edit-account/check_username_exist?username=" + usernameInput.value);
            let status = await response.json();
            usernameExists = status.usernameExists;
            updateSubmitButton();
        }, 500);

        emailAddressInput.addEventListener("input", debouncedEmailAddressAPI);  
        usernameInput.addEventListener("input", debouncedUsernameAPI);
    }


    function debounce(func, wait) {
      let timeout;
      return function executedFunction(...args) {
        const later = () => {
          clearTimeout(timeout);
          func(...args);
        };
        clearTimeout(timeout);
        timeout = setTimeout(later, wait);
      };
  }
    

  function updateSubmitButton() {
      console.log(emailExists)
      console.log(usernameExists)
      if (emailExists || usernameExists) {
        // disable submission
        editAccountBtn.disabled = true;
      } else {
        // enable submission
        editAccountBtn.disabled = false;
      }
  }
})



