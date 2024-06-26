document.addEventListener('DOMContentLoaded', () => {
    const carousels = document.querySelectorAll('.carousel');

    carousels.forEach(carousel => {
        const items = carousel.querySelectorAll('.carousel-item');
        let currentItem = 0;

        const showItem = (index) => {
            items.forEach((item, i) => {
                item.style.display = (i === index) ? 'block' : 'none';
            });
        };

        const updateCounter = (index) => {
            const counter = carousel.querySelector('.image-counter');
            counter.textContent = `${index + 1}/${items.length}`;
        };

        showItem(currentItem);
        updateCounter(currentItem);

        const nextButton = carousel.querySelector('.carousel-next');
        const prevButton = carousel.querySelector('.carousel-prev');

        nextButton.addEventListener('click', () => {
            currentItem = (currentItem + 1) % items.length;
            showItem(currentItem);
            updateCounter(currentItem);
        });

        prevButton.addEventListener('click', () => {
            currentItem = (currentItem - 1 + items.length) % items.length;
            showItem(currentItem);
            updateCounter(currentItem);
        });
    });
});
