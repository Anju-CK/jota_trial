document.getElementById('brand').addEventListener('click', function(event) {
    event.preventDefault();
    this.classList.remove('no-underline');
    document.getElementById('domain').classList.add('no-underline');
    document.getElementById('billing').classList.add('no-underline');
    document.getElementById('management').classList.add('no-underline');
});

document.getElementById('domain').addEventListener('click', function(event) {
    event.preventDefault();
    this.classList.remove('no-underline');
    document.getElementById('brand').classList.add('no-underline');
    document.getElementById('billing').classList.add('no-underline');
    document.getElementById('management').classList.add('no-underline');
});

document.getElementById('management').addEventListener('click', function(event) {
    event.preventDefault();
    this.classList.remove('no-underline');
    document.getElementById('billing').classList.add('no-underline');
    document.getElementById('domain').classList.add('no-underline');
    document.getElementById('brand').classList.add('no-underline');
});

document.getElementById('billing').addEventListener('click', function(event) {
    event.preventDefault();
    this.classList.remove('no-underline');
    document.getElementById('management').classList.add('no-underline');
    document.getElementById('domain').classList.add('no-underline');
    document.getElementById('brand').classList.add('no-underline');
});