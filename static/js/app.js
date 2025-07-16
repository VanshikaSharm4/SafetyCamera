const nextButton = document.querySelector('.next-btn');
const video = document.querySelector('.hero-video');

const movieList = ['videos/hero-1.mp4', 'videos/hero-2.mp4', 'videos/hero-3.mp4'];

let index = 0;

nextButton.addEventListener('click', function () {
  index += 1;

  if (index >= movieList.length) {
    index = 0;
  }

  video.src = movieList[index];
  video.play(); // Optional: to auto-play on change
});

// Feature Slider Logic
(function() {
  const track = document.querySelector('.feature-slider-track');
  const slides = Array.from(document.querySelectorAll('.feature-slide'));
  const leftArrow = document.querySelector('.feature-slider-arrow.left');
  const rightArrow = document.querySelector('.feature-slider-arrow.right');
  const dots = Array.from(document.querySelectorAll('.feature-slider-dots .dot'));
  let currentIndex = 0;
  const totalSlides = slides.length;

  function updateSlider(index) {
    // Loop around
    if (index < 0) index = totalSlides - 1;
    if (index >= totalSlides) index = 0;
    currentIndex = index;
    // Move track
    track.style.transform = `translateX(-${index * 100}%)`;
    // Update dots
    dots.forEach((dot, i) => {
      dot.classList.toggle('active', i === index);
    });
  }

  leftArrow.addEventListener('click', () => {
    updateSlider(currentIndex - 1);
  });
  rightArrow.addEventListener('click', () => {
    updateSlider(currentIndex + 1);
  });
  dots.forEach((dot, i) => {
    dot.addEventListener('click', () => updateSlider(i));
  });

  // Optional: swipe support for mobile
  let startX = null;
  track.addEventListener('touchstart', (e) => {
    startX = e.touches[0].clientX;
  });
  track.addEventListener('touchend', (e) => {
    if (startX === null) return;
    const endX = e.changedTouches[0].clientX;
    if (endX - startX > 50) updateSlider(currentIndex - 1);
    else if (startX - endX > 50) updateSlider(currentIndex + 1);
    startX = null;
  });

  // Initialize
  updateSlider(0);
})();


