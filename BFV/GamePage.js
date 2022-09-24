window.addEventListener("load", function () {

    document.querySelector("#submit").addEventListener("click", submitButton);



    const inputWeaponText = document.getElementById("weaponText");
  
    // Press the submit button by pressing the "Enter" button
    inputWeaponText.addEventListener("keypress", function (event) {
        if (event.key === "Enter") {
            event.preventDefault();
            document.getElementById("submit").click();
        }
    });

    // Unshuffled order of the weapons as a new array.
    var unshuffledWeapons = [...weapons];
    // Displaying weapon images on the front page in random order. 
    var shuffled_weapons = shuffle(weapons);

    autocompleteList();

    

    displayGame();
    let score = 0;


    // Shuffling the order of the weapons object array. This way, when the order is shuffled and I'm animating the pictures going from left to right, 
    // the user will not use that to his advantage and guess the name of the gun, if they find out the pictures are in alphabetical order. 
    function shuffle(array) {
        var currentIndex = array.length;
        var temporaryValue;
        var randomIndex;

        while (0 !== currentIndex) {
            randomIndex = Math.floor(Math.random() * currentIndex);
            currentIndex -= 1;
            temporaryValue = array[currentIndex];
            array[currentIndex] = array[randomIndex];
            array[randomIndex] = temporaryValue;
        }

        return array;
    }


    function autocompleteList() {
        // When input box is typed, it'll have autocomplete list of weapons starting with the letters typed in the input box. 
        // eg if "12" is typed, it'll show 12g Automatic below the input box.
        inputWeaponText.addEventListener("input", function () {
            const weaponAutoCompleteList = document.querySelector("#weaponAutoCompleteList");
            const valueOfInput = document.getElementById("weaponText").value;
            const arrayOfInput = Array.of(...valueOfInput)

            let newWeaponsList = []; // This array will be used later on. Weapons that have matching name with the input will be pushed and copied into this array. 
            /*    
            if input triggered, clear newWeaponsList array
                if valueOfInput == unshuffledWeapons.name.charAt
                create array (newWeaponsList) of all objects matching valueOfInput
                display autocomplete list of that new array
                
                else if input triggered, if valueOfInput != unshuffledWeapons.name.charAt
                clear autocomplete list
                    I prob don't need this else if statement, if input triggered and only IF valueOfInput == unshuffledWeapons.name.charAt
                    then a new array will be created. However, if only input is triggered and the IF statement is false, it'll clear the new array, hence
                    will not display the autocomplete list
            */
            // If the input box is empty, clear all autocomplete list
            if (arrayOfInput.length == 0) {
                weaponAutoCompleteList.innerHTML = "";
            }
            else {
                // Cycles through the UNSHUFFLED array which contains the names of all the weapons. If the starting letters of the weapon match with the input letters,
                // those weapons will be copied into a new array called newWeaponsList. This array will be used to display the autocomplete list. 
                for (let i in unshuffledWeapons) {
                    if (valueOfInput.toUpperCase() == unshuffledWeapons[i].name.substring(0, arrayOfInput.length).toUpperCase()) {
                        newWeaponsList.push(unshuffledWeapons[i].name)
                    }
                    else if (valueOfInput.toUpperCase() != unshuffledWeapons[i].name.substring(0, arrayOfInput.length).toUpperCase()) {
                        weaponAutoCompleteList.innerHTML = "";
                    }
                }
                // Lists all the weapons on the autocomplete list with the array that contains lists of all the weapons that start with the letters on the input box. 
                for (j = 0; j < newWeaponsList.length; j++) {
                    weaponAutoCompleteList.innerHTML += `
                <div class="hiddenLists">
                    <span id="hiddenWords"><strong>${newWeaponsList[j]}</strong></span>
                </div>`;
                    clickAutocompleteList(newWeaponsList[j]);
                }
            }
        })
    }




    function clickAutocompleteList(weapon) {
        document.querySelector("#weaponAutoCompleteList").addEventListener("click", function(){
            document.getElementById("weaponText").value.innerHTML = weapon;
            console.log("Works");
            console.log(document.getElementById("weaponText").value.innerText);
            console.log(weapon);
        })

    }

    // Loading a random weapon image. 
    function displayGame() {
        let weaponImage = document.querySelector("#weaponImage");
        weaponImage.innerHTML = `<img src="./guns/${shuffled_weapons[0].name}.png" id="weaponImageDisplay">`;
        document.getElementById("weaponText").value = "";
    }




    // This function should randomly display an image and prompt the user to guess. 
    // Once a weapon is displayed, it shouldn't be displayed in future random cycles. 
    function submitButton() {

        const health = document.querySelectorAll(".health");
        const inputValue = document.getElementById("weaponText").value;
        if (inputValue.toUpperCase() == shuffled_weapons[0].name.toUpperCase()) {
            console.log("correct");
            shuffled_weapons.shift();
            console.log(shuffled_weapons);
            tallyScore(score + 1);
            score++;
            displayGame();
        }
        else {
            shuffled_weapons.shift();
            displayGame();
            health[0].remove();
        }

        stopGameAfterNoHealth(health);

    }

    function tallyScore(score) {
        let scoreHTML = document.querySelector("#score");
        scoreHTML.innerHTML = `Score: ${score}`;
    }

    function stopGameAfterNoHealth(health) {
        if (health.length == 1) {
            console.log("Game over");
        }
    }

});