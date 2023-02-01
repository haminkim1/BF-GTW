window.addEventListener("load", function () {

    // changing class within body tag in layout.html whenever bfv.html loads. 
    // the function loads devastation.webp instead of having a black background. 
    const background = document.querySelector(".background");
    background.classList.remove("background");
    
    const parentDiv = document.querySelector(".parentDiv");
    parentDiv.classList.add("bfv-main")

    const changeToShadowClass = document.querySelector(".changeToShadowClass");
    changeToShadowClass.className = '';
    changeToShadowClass.classList.add("shadow")

    let input = document.querySelector('input');
    input.addEventListener('input', async function() {
        let response = await fetch('/bfv?name=' + input.value);
        let weapons = await response.json();
        // After fetching API data, display those names in a list below the input box 
        // let html = '';
        // for (let i in weapons) {
        //     let name = weapons[i];
        //     html += '<li>' + name + '</li>';
        // }
        // document.querySelector('.test').innerHTML += html;
        console.log(weapons)
    });
})



