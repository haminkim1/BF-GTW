window.addEventListener("load", function () {
    document.getElementById("playButton").onclick = function () {
        location.href = "./GamePage.html";
    };
    document.getElementById("login").onclick = function () {
        location.href = "./login.html";
    };
    document.getElementById("register").onclick = function () {
        location.href = "./register.html";
    };

    let gunImageDisplay = document.querySelector("#gunImageDisplay");

    // Displaying weapon images on the front page in random order. 
    var shuffled_weapons = shuffle(weapons);
    for (i = 0; i < shuffled_weapons.length; i++) {
        gunImageDisplay.innerHTML += `<img src="./guns/${shuffled_weapons[i].name}.png">`;
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
});