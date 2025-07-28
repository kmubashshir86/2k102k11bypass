// Dark mode toggle
const toggleButton = document.createElement('button');
toggleButton.textContent = 'Toggle Dark Mode';
toggleButton.style.position = 'fixed';
toggleButton.style.top = '10px';
toggleButton.style.right = '10px';
toggleButton.style.padding = '10px';
toggleButton.style.backgroundColor = '#1e88e5';
toggleButton.style.color = 'white';
toggleButton.style.border = 'none';
toggleButton.style.borderRadius = '5px';
toggleButton.style.cursor = 'pointer';
document.body.appendChild(toggleButton);

toggleButton.addEventListener('click', () => {
    document.body.classList.toggle('dark-mode');
});

// Apply dark mode styles
const style = document.createElement('style');
style.textContent = `
    .dark-mode {
        background-color: #121212;
        color: #e0e0e0;
    }
    .dark-mode header {
        background-color: #1565c0;
    }
    .dark-mode article {
        background-color: #1e1e1e;
    }
    .dark-mode footer {
        background-color: #424242;
    }
`;
document.head.appendChild(style);
