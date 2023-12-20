document.addEventListener("DOMContentLoaded", function() {
    var dropdown = document.getElementById('dropdown');
    var menu = document.getElementById('menu');
    var chevron = dropdown.querySelector('i');

    dropdown.addEventListener('click', function() {
        if (menu.style.display === 'block') {
            menu.style.display = 'none';
            chevron.classList.remove('fa-chevron-up');
            chevron.classList.add('fa-chevron-down');
        } else {
            menu.style.display = 'block';
            chevron.classList.remove('fa-chevron-down');
            chevron.classList.add('fa-chevron-up');
        }
    });
});