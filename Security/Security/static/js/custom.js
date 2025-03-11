// get current year
(function () {
    var year = new Date().getFullYear();
    document.querySelector("#currentYear").innerHTML = year;
})();

document.addEventListener("DOMContentLoaded", function () {
    $('#teamCarousel').carousel({
        interval: 4000, // Matches the example's speed (4 seconds)
        pause: "hover",
        wrap: true
    });
});
