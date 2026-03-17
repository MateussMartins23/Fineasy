// Detectar tema atual
const currentTheme = document.documentElement.getAttribute('data-theme') || 'dark';
const legendColor = currentTheme === 'light' ? '#000000' : '#FFFFFF';

const ctx = document.getElementById('graficoDespesas');
let=fetch('/dados')
.then(res => res.json())
.then(data => {
    console.log(data);
});
new Chart(ctx, {
    type: 'pie',
    data: {
        labels: ['Entrada', 'Investimento', 'Saida', 'Saldo_Final'],
        datasets: [{
            data: data,
            backgroundColor: [
                '#59df00',
                '#020068',
                '#860411',
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