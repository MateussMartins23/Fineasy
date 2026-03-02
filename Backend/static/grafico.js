// Detectar tema atual
const currentTheme = document.documentElement.getAttribute('data-theme') || 'dark';
const legendColor = currentTheme === 'light' ? '#000000' : '#FFFFFF';

const ctx = document.getElementById('graficoDespesas');

new Chart(ctx, {
    type: 'pie',
    data: {
        labels: ['Alimentação', 'Transporte', 'Lazer', 'Outros'],
        datasets: [{
            data: [450, 200, 150, 100],
            backgroundColor: [
                '#59df00',
                '#020068',
                '#710486',
                '#ffee00'
            ],
            borderWidth: 0
        }]
    },
    options: {
        responsive: true,
        plugins: {
            legend: {
                position: 'bottom',
                labels: {
                    color: legendColor
                }
            }
        }
    }
});