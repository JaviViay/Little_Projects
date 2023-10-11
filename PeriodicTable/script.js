const elements = document.querySelectorAll('.element');

        elements.forEach(element => {
            element.addEventListener('mouseenter', () => {
                const tooltip = element.querySelector('.tooltip');
                tooltip.style.display = 'block';
            });

            element.addEventListener('mouseleave', () => {
                const tooltip = element.querySelector('.tooltip');
                tooltip.style.display = 'none';
            });
        });