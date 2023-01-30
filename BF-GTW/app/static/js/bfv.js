window.addEventListener("load", function () {

    // changing class of body tag in layout.html whenever bfv.html loads. 
    // the function loads devastation.webp instead of having a black background. 
    const background = document.querySelector(".background")
    background.classList.add("bfv-main")
    background.classList.remove("background")
})



