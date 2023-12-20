document.getElementById('plans-link').addEventListener('click', function(event) {
    event.preventDefault();
    this.classList.remove('no-underline');
    document.getElementById('contact-link').classList.add('no-underline');
    window.location.href = this.getAttribute('href');
});

document.getElementById('contact-link').addEventListener('click', function(event) {
    event.preventDefault();
    this.classList.remove('no-underline');
    document.getElementById('plans-link').classList.add('no-underline');
    window.location.href = this.getAttribute('href');
});




