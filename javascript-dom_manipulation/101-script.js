const hello = document.querySelector('#hello');
const languageCode = document.querySelector('#language_code');
const btnTranslate = document.querySelector('#btn_translate');

btnTranslate.addEventListener('click', () => {
  const url = `https://hellosalut.stefanbohacek.dev/?lang=${languageCode.value}`;
  fetch(url)
    .then(response => response.json())
    .then(data => {
      hello.textContent = data.hello;
    });
});
