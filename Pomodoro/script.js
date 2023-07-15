const startButton = document.getElementById('start-button');
const stopButton = document.getElementById('stop-button');
const resetButton = document.getElementById('reset-button');
const clock = document.getElementById('clock');

let timer;
let time = 1500; // 25 minutes

function startTimer() {
    timer = setInterval(updateTimer, 1000);
    startButton.disabled = true;
}

function stopTimer() {
    clearInterval(timer);
    startButton.disabled = false;
}

function resetTimer() {
    stopTimer();
    time = 1500;
    updateClock();
}

function updateTimer() {
    if (time > 0) {
        time--;
        updateClock();
    } else {
        stopTimer();
    }
}

function updateClock() {
    const minutes = Math.floor(time / 60);
    const seconds = time % 60;
    clock.textContent = `${formatTime(minutes)}:${formatTime(seconds)}`;
}

function formatTime(time) {
    return time < 10 ? `0${time}` : time;
}

startButton.addEventListener('click', startTimer);
stopButton.addEventListener('click', stopTimer);
resetButton.addEventListener('click', resetTimer);