document.addEventListener('DOMContentLoaded', function () {
    var swiper = new Swiper('.swiper-container', {
        slidesPerView: 1,
        spaceBetween: 30,
        navigation: {
            nextEl: '.swiper-button-next',
            prevEl: '.swiper-button-prev',
        },
        pagination: {
            el: '.swiper-pagination',
            clickable: true,
        },
        loop: true, // Enable infinite loop
        autoplay: {
            delay: 3000, // Adjust the delay between slides in milliseconds
            disableOnInteraction: false,
        },
    });

    const serviceCards = document.querySelectorAll('.service-card');

    serviceCards.forEach(card => {
        card.addEventListener('click', () => {
            const serviceId = card.id;
            showServiceDetails(serviceId);
        });
    });

    function showServiceDetails(service) {
        // Hide all service details initially
        const serviceDetails = document.querySelectorAll('.service-details');
        serviceDetails.forEach(detail => detail.style.display = 'none');

        // Show the selected service details
        const selectedServiceDetail = document.getElementById(service + '-details');
        if (selectedServiceDetail) {
            selectedServiceDetail.style.display = 'block';
        }
    }
});
