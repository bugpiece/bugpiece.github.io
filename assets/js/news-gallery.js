document.querySelectorAll('[data-news-gallery]').forEach(function (gallery) {
  var photos = Array.from(gallery.querySelectorAll('.news-photo'));
  var indicators = gallery.querySelector('.news-gallery__indicators');
  if (photos.length < 2 || !indicators) return;

  var buttons = Array.from(indicators.querySelectorAll('button'));
  var status = gallery.querySelector('[data-photo-status]');
  var previous = gallery.querySelector('[data-photo-previous]');
  var next = gallery.querySelector('[data-photo-next]');
  var current = 0;

  function showPhoto(index, announce) {
    current = (index + photos.length) % photos.length;
    photos.forEach(function (photo, photoIndex) {
      photo.hidden = photoIndex !== current;
    });
    buttons.forEach(function (button, buttonIndex) {
      if (buttonIndex === current) {
        button.setAttribute('aria-current', 'true');
      } else {
        button.removeAttribute('aria-current');
      }
    });
    if (announce) status.textContent = buttons[current].getAttribute('aria-label');
  }

  buttons.forEach(function (button, index) {
    button.addEventListener('click', function () { showPhoto(index, true); });
  });
  previous.addEventListener('click', function () { showPhoto(current - 1, true); });
  next.addEventListener('click', function () { showPhoto(current + 1, true); });

  showPhoto(0, false);
  indicators.hidden = false;
  previous.hidden = false;
  next.hidden = false;
});
