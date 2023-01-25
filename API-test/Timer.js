window.addEventListener("load", function () {

    // Variables for timer functions
    let timer = null;
    let timerMinutes = null;
    let seconds = 60;
    let minutes = 9;
 
    // Start countdown of 10 minutes when the start button is clicked. 
    document.querySelector("#btnStartTimer").addEventListener("click", startTimer);
    document.querySelector("#btnStopTimer").addEventListener("click", stopTimer);

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

});