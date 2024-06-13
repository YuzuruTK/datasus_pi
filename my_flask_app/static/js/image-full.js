
// custom.js

document.addEventListener('DOMContentLoaded', () => {
    const modal = document.getElementById('image-modal');
    const modalImage = document.getElementById('modal-image');
    const imageThumbnails = document.querySelectorAll('.image-thumbnail');
    const modalCloseButton = document.querySelector('.modal-close');
    const modalNextButton = document.querySelector('.modal-next');
    const modalPrevButton = document.querySelector('.modal-prev');

    let currentImageIndex;

    imageThumbnails.forEach((thumbnail, index) => {
        thumbnail.addEventListener('click', () => {
            modal.classList.add('is-active');
            modalImage.src = thumbnail.src;
            currentImageIndex = index;
        });
    });

    modalCloseButton.addEventListener('click', () => {
        modal.classList.remove('is-active');
    });

    modalNextButton.addEventListener('click', () => {
        currentImageIndex = (currentImageIndex + 1) % imageThumbnails.length;
        modalImage.src = imageThumbnails[currentImageIndex].src;
    });

    modalPrevButton.addEventListener('click', () => {
        currentImageIndex = (currentImageIndex - 1 + imageThumbnails.length) % imageThumbnails.length;
        modalImage.src = imageThumbnails[currentImageIndex].src;
    });

    document.querySelector('.modal-background').addEventListener('click', () => {
        modal.classList.remove('is-active');
    });
});
