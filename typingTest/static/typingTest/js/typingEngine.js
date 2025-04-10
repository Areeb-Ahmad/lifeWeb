class TypingEngine {
    constructor(texts, timeLimit = 60) {
        this.texts = texts;
        this.timeLimit = timeLimit;
        this.timer = timeLimit;
        this.currentText = "";
        this.currentPosition = 0;
        this.correctChars = 0;
        this.totalTyped = 0;
        this.isTyping = false;
        this.interval = null;
    }

    init() {
        this.resetTest();
        this.displayText();
    }

    resetTest() {
        clearInterval(this.interval);
        this.currentText = this.texts[Math.floor(Math.random() * this.texts.length)];
        this.currentPosition = 0;
        this.correctChars = 0;
        this.totalTyped = 0;
        this.timer = this.timeLimit;
        this.isTyping = false;
    }

    displayText() {
        const textDisplay = document.getElementById('text-display');
        textDisplay.innerHTML = this.currentText.split('').map(char => 
            `<span class="untyped">${char}</span>`
        ).join('');
    }

    startTimer() {
        this.interval = setInterval(() => {
            this.timer--;
            document.getElementById('timer').textContent = this.timer;
            
            if (this.timer <= 0) {
                this.endTest();
            }
        }, 1000);
    }

    handleInput(inputChar) {
        if (!this.isTyping) {
            this.isTyping = true;
            this.startTimer();
        }

        const spans = document.querySelectorAll('#text-display span');
        const currentChar = this.currentText[this.currentPosition];

        // Update character styling
        if (this.currentPosition > 0) {
            spans[this.currentPosition - 1].classList.remove('current');
        }

        if (inputChar === currentChar) {
            spans[this.currentPosition].className = 'correct';
            this.correctChars++;
        } else {
            spans[this.currentPosition].className = 'incorrect';
        }

        spans[this.currentPosition].classList.add('current');
        this.currentPosition++;
        this.totalTyped++;

        // Update stats
        this.updateStats();

        // Check if test completed
        if (this.currentPosition === this.currentText.length) {
            this.endTest();
        }
    }

    updateStats() {
        const minutes = (this.timeLimit - this.timer) / 60;
        const wpm = Math.round((this.correctChars / 5) / minutes);
        const accuracy = Math.round((this.correctChars / this.totalTyped) * 100);
        
        document.getElementById('wpm').textContent = `${wpm} WPM`;
        document.getElementById('accuracy').textContent = `${accuracy}%`;
    }

    endTest() {
        clearInterval(this.interval);
        document.getElementById('user-input').disabled = true;
    }
}