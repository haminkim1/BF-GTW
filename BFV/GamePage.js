window.addEventListener("load", function () {

    // Variables for timer functions
    let timer = null;
    let seconds = 60;
    let minutes = "0" + 9;
 
    // Start countdown of 10 minutes when the start button is clicked. 
    document.querySelector("#btnStartTimer").addEventListener("click", startTimer);
   // document.querySelector("#btnStopTimer").addEventListener("click", stopTimer);

   // Function executes when start button is clicked. 
    function startTimer(){
        if (timer == null) {
            document.querySelector("#timer_face").innerHTML = "10:00"; // removed timer = from the start of the line.
            

            timer = setInterval(updateSeconds, 1000); // Every seconds, the timer drops by 1 second. 
            timer = setInterval(updateMinutes, 60000); // Every minutes, the timer drops by 1 minute. 
        }
    }

    // setInterval every second within the startTimer function
    function updateSeconds() {
        seconds --;
        
        // if seconds or minutes have 1 significant figure, add a 0 at the beginning. so 1:1 would be 01:01.
        if (seconds < 10) {
            document.querySelector("#timer_face").innerHTML = minutes + ":" + "0" + seconds;
        }
        else {
            document.querySelector("#timer_face").innerHTML = minutes + ":" + seconds;
        }
        
        if (seconds == 0) {
            seconds = 60;
        }
    }

    // setInterval every minute within the startTimer function
    function updateMinutes() {
        minutes --;
    }


    stopGame();

    function stopGame() {
        if (minutes == 0 && seconds == 0) {
            console.log(gameover);
            clearInterval(timer);
        }
    }








    let weaponImage = document.querySelector("#weaponImage");

    // Displaying weapon images on the front page in random order. 
    var shuffled_weapons = shuffle(weapons);
    for (i = 0; i < 1; i++) {
        weaponImage.innerHTML = `<img src="./guns/${shuffled_weapons[i].name}.png">`;
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
    function game() {
        
    }
});