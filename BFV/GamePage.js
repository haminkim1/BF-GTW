window.addEventListener("load", function () {

    // Variables for timer functions
    let timer = null;
    let timerMinutes = null;
    let seconds = 10;
    let minutes = 1;
 
    // Start countdown of 10 minutes when the start button is clicked. 
    document.querySelector("#btnStartTimer").addEventListener("click", startTimer);
    document.querySelector("#btnStopTimer").addEventListener("click", stopTimer);

    // Function executes when start button is clicked. 
    function startTimer(){
        if (timer == null && timerMinutes == null) {
            document.querySelector("#timer_face").innerHTML = "10:00"; // removed timer = from the start of the line.
            
            timer = setInterval(updateSeconds, 1000); // Every second, the timer drops by 1 second. 
            timerMinutes = setInterval(updateMinutes, 2000); // Every minute, the timer drops by 1 minute. 
        }
    }

    // setInterval every second within the startTimer function
    function updateSeconds() {
        seconds --;
        
        // if seconds or minutes have 1 significant figure, add a 0 at the beginning. so 1:1 would be 01:01.
        if (seconds < 10) {
            document.querySelector("#timer_face").innerHTML = "0" + minutes + ":" + "0" + seconds;
        }
        else {
            document.querySelector("#timer_face").innerHTML = "0" + minutes + ":" + seconds;
        }
        
        if (minutes != 0 && seconds == 0) {
            seconds = 60;
        }

        stopSecondsTimer();
    }

    // setInterval every minute within the startTimer function
    function updateMinutes() {
        minutes --;
        stopMinutesTimer();
    }

    function stopTimer() {
        clearInterval(timer);
        clearInterval(timerMinutes);
        minutes = 0;
        seconds = 0;
        document.querySelector("#timer_face").innerHTML = "0" + minutes + ":" + "0" + seconds;
    }

    // Above are the timer related codes
    // Below are the game related codes

    document.querySelector("#submit").addEventListener("click", submitButton);
    let score = 0;

    // Press the submit button by pressing the "Enter" button
    const inputWeaponText = document.getElementById("weaponText");

    inputWeaponText.addEventListener("keypress", function(event) {
        if (event.key === "Enter") {
            event.preventDefault();
            document.getElementById("submit").click();
        }
    });

    // Displaying weapon images on the front page in random order. 
    var shuffled_weapons = shuffle(weapons);


    displayGame();
    
    function displayGame() {
        let weaponImage = document.querySelector("#weaponImage");  
        weaponImage.innerHTML = `<img src="./guns/${shuffled_weapons[0].name}.png" id="weaponImageDisplay">`;
        document.getElementById("weaponText").value = "";
    }


    function stopSecondsTimer() {
        if (minutes == 0 && seconds == 0) {
            clearInterval(timer);
            console.log("seconds stopped");
        }
    }

    function stopMinutesTimer() {
        if (minutes == 0) {
            clearInterval(timerMinutes);
            console.log("Game Over");
        }
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
            tallyScore(score+1);
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