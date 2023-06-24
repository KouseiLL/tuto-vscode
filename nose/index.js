const toggle = document.getElementById('darkModeToggle');
const body = document.body;
const toggleText = document.getElementById('toggleText');

toggle.addEventListener('change', function () {
  body.classList.toggle('dark');
  if (body.classList.contains('dark')) {
    toggleText.textContent = 'ON';
  } else {
    toggleText.textContent = 'OFF';
  }
});

