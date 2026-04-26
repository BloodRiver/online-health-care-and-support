document.addEventListener('DOMContentLoaded', function() {
    const donationsCtx = document.getElementById('monthlyDonationsChart').getContext('2d');
    const bloodGroupCtx = document.getElementById('bloodGroupChart').getContext('2d');
    const bloodGroupBarCtx = document.getElementById('bloodGroupBarChart').getContext('2d');

    const COLORS = ['#0088FE', '#00C49F', '#FFBB28', '#FF8042', '#8884d8'];

    new Chart(donationsCtx, {
        type: 'line',
        data: {
            labels: donationLabels,
            datasets: [{
                label: 'Donations',
                data: donationData,
                borderColor: '#dc2626',
                borderWidth: 2,
                tension: 0.4,
                pointRadius: 3,
                fill: false
            }]
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            plugins: {
                legend: { position: 'top' },
                tooltip: { enabled: true }
            },
            scales: {
                y: {
                    beginAtZero: true,
                    ticks: {
                        stepSize: 50
                    },
                    grid: {
                        display: true,
                        borderDash: [5, 5],
                        color: 'rgba(0, 0, 0, 0.1)'
                    }
                },
                x: {
                    grid:
                    {
                        display: true,
                        borderDash: [5, 5],
                        color: 'rgba(0, 0, 0, 0.1)'
                    }
                }
            }
        }
    });

    new Chart(bloodGroupCtx, {
        type: 'pie',
        data: {
            labels: bloodGroupLabels,
            datasets: [{
                data: bloodGroupDataCounts,
                backgroundColor: COLORS,
                borderWidth: 1
            }]
        },
        plugins: [ChartDataLabels], // Enables the percentage labels
        options: {
            responsive: true,
            maintainAspectRatio: false,
            plugins: {
                legend: { position: 'top' },
                datalabels: {
                    color: '#fff',
                    formatter: (value, ctx) => {
                        let sum = ctx.chart.data.datasets[0].data.reduce((a, b) => a + b, 0);
                        let percentage = (value * 100 / sum).toFixed(0) + "%";
                        return ctx.chart.data.labels[ctx.dataIndex] + ": " + percentage;
                    },
                    font: { weight: 'bold' }
                }
            }
        }
    });

    new Chart(bloodGroupBarCtx, {
        type: 'bar',
        data: {
            labels: blood_group_labels,
            datasets: [{
                label: 'Blood Group Distribution',
                data: blood_group_stat_counts,
                backgroundColor: '#dc2626', // Matching your "fill" color
                borderWidth: 0
            }]
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            scales: {
                y: {
                    beginAtZero: true,
                    grid: {
                        display: true,
                        borderDash: [3, 3] // Replicates strokeDasharray="3 3"
                    },
                    ticks: {
                        stepSize: 80
                    }
                },
                x: {
                    grid: {
                        display: true,
                        borderDash: [3, 3] // Replicates strokeDasharray="3 3"
                    }
                }
            },
            plugins: {
                legend: { display: true }, // Equivalent to <Legend />
                tooltip: { enabled: true } // Equivalent to <Tooltip />
            }
        }
    });
});