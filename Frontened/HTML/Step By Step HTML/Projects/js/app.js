// Smooth Scrolling for Navigation Links
document.querySelectorAll('ul li a').forEach(link => {
    link.addEventListener('click', function(e) {
        e.preventDefault();
        const target = document.querySelector(this.getAttribute('href'));
        if (target) {
            target.scrollIntoView({ behavior: 'smooth' });
        }
    });
});

// Change Header Style on Scroll
window.addEventListener('scroll', function () {
    const header = document.querySelector('header');
    if (window.scrollY > 50) {
        header.style.background = '#ff4e50';
        header.style.padding = '15px';
    } else {
        header.style.background = 'linear-gradient(45deg, #ff4e50, #fc913a)';
        header.style.padding = '20px';
    }
});

// Input Focus Animation
const searchBox = document.querySelector('input');
searchBox.addEventListener('focus', () => {
    searchBox.style.width = '350px';
    searchBox.style.transition = '0.3s';
});
searchBox.addEventListener('blur', () => {
    searchBox.style.width = '300px';
});
