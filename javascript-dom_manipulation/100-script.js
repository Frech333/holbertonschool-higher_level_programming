const addItem = document.querySelector('#add_item');
const removeItem = document.querySelector('#remove_item');
const clearList = document.querySelector('#clear_list');
const myList = document.querySelector('.my_list');

addItem.addEventListener('click', () => {
  const newLi = document.createElement('li');
  newLi.textContent = 'Item';
  myList.appendChild(newLi);
});

removeItem.addEventListener('click', () => {
  const lastLi = myList.querySelector('li:last-child');
  if (lastLi) {
    myList.removeChild(lastLi);
  }
});

clearList.addEventListener('click', () => {
  myList.innerHTML = '';
});
