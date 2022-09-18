window.addEventListener("load", function () {

    document.querySelector("#submit").addEventListener("click", submitButton);
    let score = 0;

    // Press the submit button by pressing the "Enter" button
    const inputWeaponText = document.getElementById("weaponText");

    inputWeaponText.addEventListener("keypress", function (event) {
        if (event.key === "Enter") {
            event.preventDefault();
            document.getElementById("submit").click();
        }
    });

    // Require an unshuffled order of the weapons as a new array.
    var unshuffledWeapons = [...weapons];
    // Displaying weapon images on the front page in random order. 
    var shuffled_weapons = shuffle(weapons);



    // This event listener will search if the first letters of the weapons names match with the letters of the input typed. 
    // Get value of input
    // Convert value of input into array
    // Compare first index of input array vs weapons name array. (Need to think about which loop to use)
    // If first index match, print "match".
    // If second and etc match, print "match". 
    // Next would be to somehow add all the matching weapon names below the weapon input. Once that name is clicked, it'll copy and paste to the input area. 
    // Once the name is clicked, it will hide the auto complete name div again. 
    inputWeaponText.addEventListener("input", function () {
        const weaponAutoCompleteList = document.querySelector("#weaponAutoCompleteList");
        const valueOfInput = document.getElementById("weaponText").value;
        const arrayOfInput = Array.of(...valueOfInput)

        const y = Object.values(unshuffledWeapons);
        const x = unshuffledWeapons.every((unshuffledWeapons) => {
            return unshuffledWeapons.name.charAt(arrayOfInput.length - 1).toUpperCase() == valueOfInput.toUpperCase()
        });
        console.log (x)
        https://www.youtube.com/playlist?list=PLDlWc9AfQBfZGZXFb_1tcRKwtCavR7AfT


        console.log(valueOfInput)
        if (arrayOfInput.length == 0) {
            weaponAutoCompleteList.innerHTML = "";
        }
        else {
            for (let i in unshuffledWeapons) {
                if (valueOfInput.toUpperCase() == unshuffledWeapons[i].name.charAt(arrayOfInput.length - 1).toUpperCase() && x === false) {
                    weaponAutoCompleteList.innerHTML += `
                    <div class="hiddenLists">
                        <span><strong id="hiddenWords">${unshuffledWeapons[i].name}</strong></span>
                    </div>`;

                }
            }
        }
 
    })





    displayGame();



    // Loading a random weapon image. 
    function displayGame() {
        let weaponImage = document.querySelector("#weaponImage");
        weaponImage.innerHTML = `<img src="./guns/${shuffled_weapons[0].name}.png" id="weaponImageDisplay">`;
        document.getElementById("weaponText").value = "";
    }


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