/* frontend/script.js */

// Collapsible Left Menu
document.getElementById('toggleMenu').addEventListener('click', function() {
    const leftMenu = document.getElementById('leftMenu');
    leftMenu.classList.toggle('collapsed');
});

// Responsive Shrinkage Function
function adjustPageWidth() {
    const width = window.innerWidth;
    let shrinkPercentage = 1; // Default (100%)

    if (width >= 992 && width <= 1600) {
        shrinkPercentage = 0.9; // 90%
    } else if (width >= 700 && width <= 767) {
        shrinkPercentage = 0.8; // 80%
    } else if (width >= 600 && width < 700) {
        shrinkPercentage = 0.75; // 75%
    } else if (width <= 600) {
        shrinkPercentage = 0.5; // 50%
    }

    const container = document.querySelector('.container');
    container.style.transform = `scale(${shrinkPercentage})`;
    container.style.transformOrigin = 'top left';
}

// Event Listeners for Responsive Shrinkage
window.addEventListener('resize', adjustPageWidth);
window.addEventListener('load', adjustPageWidth);
