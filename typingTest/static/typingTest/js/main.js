document.addEventListener('DOMContentLoaded', () => {
    const texts = [
        "The quick brown fox jumps over the lazy dog",
        "Programming is the art of telling another human what one wants the computer to do",
        "To be or not to be, that is the question",
        "The only way to learn a new programming language is by writing programs in it"
    ];

    const engine = new TypingEngine(texts);
    engine.init();

    const userInput = document.getElementById('user-input');
    const restartBtn = document.getElementById('restart-btn');

    userInput.addEventListener('input', (e) => {
        engine.handleInput(e.target.value.slice(-1));
        e.target.value = "";
    });

    restartBtn.addEventListener('click', () => {
        engine.init();
        userInput.disabled = false;
        userInput.focus();
    });

    // Focus input on page load
    userInput.focus();
});