function redirect() {
    window.location = "https://github.com/ARKseal/ARKseal.github.io";
}

function startTimer(duration, display) {
    var timer = duration, seconds;
    setInterval(function () {
        seconds = parseInt(timer % 60, 10);

        display.textContent = seconds;

        if (--timer < 0) {
            timer = duration;
        }
        if (seconds == 0) {
            redirect()
        }
    }, 1000);
}

window.onload = function () {
    var timer = document.getElementById('time');
    startTimer(4, timer);
};