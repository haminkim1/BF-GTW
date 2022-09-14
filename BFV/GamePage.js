window.addEventListener("load", function () {

    // Variables for timer functions
    let timer = null;
    let timerMinutes = null;
    let seconds = 60;
    let minutes = 9;
 
    // Start countdown of 10 minutes when the start button is clicked. 
    document.querySelector("#btnStartTimer").addEventListener("click", startTimer);
    document.querySelector("#btnStopTimer").addEventListener("click", stopTimer);
    document.querySelector("#submit").addEventListener("click", submitButton);

    // Press the submit button by pressing the "Enter" button
    const inputWeaponText = document.getElementById("weaponText");

    inputWeaponText.addEventListener("keypress", function(event) {
        if (event.key === "Enter") {
            event.preventDefault();
            document.getElementById("submit").click();
        }
    });

    stopGame();

    let weaponImage = document.querySelector("#weaponImage");

    // Displaying weapon images on the front page in random order. 
    var shuffled_weapons = shuffle(weapons);
   
        weaponImage.innerHTML = `<img src="./guns/${shuffled_weapons[0].name}.png" id="weaponImageDisplay">`;
    

    
    // Function executes when start button is clicked. 
    function startTimer(){
        if (timer == null && timerMinutes == null) {
            document.querySelector("#timer_face").innerHTML = "10:00"; // removed timer = from the start of the line.
            
            timer = setInterval(updateSeconds, 1000); // Every second, the timer drops by 1 second. 
            timerMinutes = setInterval(updateMinutes, 60000); // Every minute, the timer drops by 1 minute. 
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
        
        if (seconds == 0) {
            seconds = 60;
        }
    }

    // setInterval every minute within the startTimer function
    function updateMinutes() {
        minutes --;
    }

    function stopGame() {
        if (minutes == 0 && seconds == 0) {
            console.log(gameover);
            clearInterval(timer);
            clearInterval(timerMinutes);
        }
    }

    function stopTimer() {
        clearInterval(timer);
        clearInterval(timerMinutes);
        minutes = 0;
        seconds = 0;
        document.querySelector("#timer_face").innerHTML = "0" + minutes + ":" + "0" + seconds;
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
        const inputValue = document.getElementById("weaponText").value;
        if (inputValue.toUpperCase() == shuffled_weapons[0].name.toUpperCase()) {
            console.log("correct");
            shuffled_weapons.shift();
            console.log(shuffled_weapons);
        }
        else {
            console.log("incorrect");
        }
    }

});