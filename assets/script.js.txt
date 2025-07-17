// static/script.js
// Prevent right-click on media elements
document.addEventListener('contextmenu', (e) => {
  const isMedia = ['img', 'image', 'video', 'svg', 'picture'].some(
    tagName => tagName.localeCompare(e.target.tagName, undefined, { sensitivity: 'base' }) === 0
  );
  if (isMedia) e.preventDefault();
});

// Hamburger Menu Toggle
document.querySelector('.hamburger').addEventListener('click', () => {
  document.querySelector('.nav-menu').classList.toggle('active');
});