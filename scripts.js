// Dark mode toggle
const toggleButton = document.createElement('button');
toggleButton.id = 'dark-mode-toggle';
toggleButton.textContent = 'Toggle Dark Mode';
toggleButton.setAttribute('aria-label', 'Toggle dark mode'); // Accessibility

// Insert button inside header for better positioning
const header = document.querySelector('header');
header.appendChild(toggleButton);

toggleButton.addEventListener('click', () => {
    document.body.classList.toggle('dark-mode');
});
