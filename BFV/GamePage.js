window.addEventListener("load", function () {


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

    function timer(){
        
    }

    // This function should randomly display an image and prompt the user to guess. 
    // Once a weapon is displayed, it shouldn't be displayed in future random cycles. 
    function game() {
        
    }
});