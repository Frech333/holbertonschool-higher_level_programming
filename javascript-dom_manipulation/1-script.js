const header = document.querySelector('header');
const redHeader = document.querySelector('#red_header');

redHeader.addEventListener('click', () => {
  if (header.classList.contains('green')) {
    header.classList.remove('green');
    header.classList.add('red');
  }
});
