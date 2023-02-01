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

})



