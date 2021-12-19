// function navButton() {
//     document.getElementById("point-relais").style.position = "relative";
//     document.getElementById("point-relais").style.top = "89px";


// }



document.querySelectorAll(".smooth-scroll").onClick(function (e) {
    let currentItem = e.target.text;
    console.log(currentItem);
    $("html, body").animate(
        {
            scrollTop:
                $($(this).attr("href")).offset().top -
                (currentItem == "Skills" ? 100 : 100)
        },
        "fast"
    );
    return false;
});