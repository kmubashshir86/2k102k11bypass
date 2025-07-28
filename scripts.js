// Dark mode toggle
const toggleButton = document.createElement('button');
toggleButton.id = 'dark-mode-toggle';
toggleButton.textContent = 'Toggle Dark Mode';
document.body.appendChild(toggleButton);

toggleButton.addEventListener('click', () => {
    document.body.classList.toggle('dark-mode');
});
