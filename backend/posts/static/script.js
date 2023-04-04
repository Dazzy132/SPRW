window.addEventListener('load', function () {
  let postField = document.getElementById('id_post');
  let form = postField.closest('form');

  if (form && postField.value) {
    postField.disabled = true;
    let infoSpan = document.createElement('div');
    infoSpan.style.color = 'red'
    infoSpan.textContent = 'Нельзя изменить пост у комментария';
    postField.parentNode.insertBefore(infoSpan, postField.nextSibling);
  }
});