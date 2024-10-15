// Select all progress containers
const progressContainers = document.querySelectorAll('.progress-container');

// Iterate over each container
progressContainers.forEach(container => {
    const progressBar = container.querySelector('.progress-bar');
    const slider = container.querySelector('input[type="range"]');

    // Update progress bar based on slider value
    slider.addEventListener('input', (event) => {
        const value = event.target.value;
        progressBar.style.width = value + '%';
        progressBar.setAttribute('aria-valuenow', value);
        progressBar.textContent = value + '%';
    });
});