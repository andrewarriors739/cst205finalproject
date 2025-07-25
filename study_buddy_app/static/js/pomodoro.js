let timeLeft = 1500; // 25 minutes in seconds
let timer;

// Confetti function
function launchConfetti() {
    const count = 2000,
      defaults = {
        origin: { y: 0.7 },
      };

    function fire(particleRatio, opts) {
      confetti(
        Object.assign({}, defaults, opts, {
          particleCount: Math.floor(count * particleRatio),
        })
      );
    }

    fire(0.25, {
      spread: 26,
      startVelocity: 55,
    });

    fire(0.2, {
      spread: 60,
    });

    fire(0.35, {
      spread: 100,
      decay: 0.91,
      scalar: 0.8,
    });

    fire(0.1, {
      spread: 120,
      startVelocity: 25,
      decay: 0.92,
      scalar: 1.2,
    });

    fire(0.1, {
      spread: 120,
      startVelocity: 45,
    });
}

function startTimer() {
    document.getElementById("tickSound").play();
    
    clearInterval(timer);
    timer = setInterval(function() {
        if (timeLeft > 0) {
            timeLeft--;
            const minutes = Math.floor(timeLeft / 60);
            const seconds = timeLeft % 60;
            document.getElementById("timer").innerText = minutes + ":" + seconds.toString().padStart(2, '0');
        } else {
            clearInterval(timer);
            document.getElementById("completeSound").play();
            launchConfetti();
            alert("Time's up!");

            resetTimer();
        }
    }, 1000);
}

function resetTimer() {
    document.getElementById("tickSound").play();
    
    clearInterval(timer);
    timeLeft = 1500;
    document.getElementById("timer").innerText = "25:00";
}
