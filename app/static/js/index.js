function startTyping() {
    const textElement = document.getElementById('typed-text');
    const text = textElement.innerHTML;

    textElement.innerHTML = ''; // Clear the text

    // Set up a function to add the hourglass element after typing
    function addHourglass() {
        const hourglassIcon = document.createElement('i');
        hourglassIcon.className = 'fa-solid fa-hourglass-end';
        hourglassIcon.style.marginLeft = '.35rem'; 
        textElement.appendChild(hourglassIcon);
    }

    for (let i = 0; i < text.length; i++) {
        setTimeout(function () {
            textElement.innerHTML += text.charAt(i);
            if (i === text.length - 1) {
                addHourglass(); // Call the function to add the hourglass icon after typing is complete
            }
        }, 50 * i); // Typing speed: 100ms delay for each character
    }
}

window.onload = function () {
    startTyping();
};
