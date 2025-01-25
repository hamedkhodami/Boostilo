    function drawCenterText(chart) {
        var width = chart.width,
            height = chart.height,
            ctx = chart.ctx;
        ctx.restore();
        var centerX = width / 2;
        var centerY = height / 2;
        var innerRadius = (chart.chartArea.left + chart.chartArea.right) / 2 * 0.35;
    
        ctx.beginPath();
        ctx.arc(centerX, centerY, innerRadius + width * 0.05, 0, 2 * Math.PI);
        ctx.fillStyle = 'white';
        ctx.fill();
        ctx.closePath();
    
        var fontSize = window.innerWidth <= 768 ? 20 : 25;
        ctx.font = fontSize + "px sans-serif";
        ctx.textBaseline = "middle";
        var textLines = ["Content", "Marketing", "Cycle"];
        var lineHeight = fontSize * 1.2;
        textLines.forEach(function(text, index) {
            var textX = Math.round((width - ctx.measureText(text).width) / 2);
            var textY = centerY - (lineHeight * (textLines.length - 1) / 2) + (index * lineHeight);
            ctx.fillStyle = "#4e2984";
            ctx.fillText(text, textX, textY);
        });
        ctx.save();
    }
    
    var ctx = document.getElementById('myChart').getContext('2d');
    var myChart = new Chart(ctx, {
        type: 'doughnut',
        data: {
            labels: [
                'RESERCH AND PLANNING ',
                'IDEATION',
                'CONTENT CREATION',
                'PUBLISHING',
                'MARKETING AND BRANDING',
            ],
            datasets: [{
                label: 'Marketing stages',
                data: [20, 20, 20, 20, 20],
                backgroundColor: [
                    '#6b38b4',
                    '#6b38b4',
                    '#6b38b4',
                    '#6b38b4',
                    '#6b38b4'
                ],
                borderColor: [
                    '#6b38b4',
                    '#6b38b4',
                    '#6b38b4',
                    '#6b38b4',
                    '#6b38b4'
                ],
                borderWidth: 1,
                spacing: 20
            }]
        },
        options: {
            cutout: '50%',
            responsive: true,
            plugins: {
                legend: {
                    display: false 
                },
                tooltip: {
                    enabled: true
                },
                datalabels: {
                    color: '#fff',
                    font: {
                        size: window.innerWidth > 768 ? 18 : 11, // فونت را برای عرض بزرگتر از 768 پیکسل به 25 پیکسل تنظیم می‌کنیم 
                        weight: '700'
                    },
                    
                    align: 'center',  
                    anchor: 'center',  
                    formatter: function(value, context) {
                        var labels = context.chart.data.labels[context.dataIndex].split(' ');
                        return (context.dataIndex + 1) + '\n' + labels.join('\n');
                    },
                    padding: 0,
                    textAlign: 'center'
                }
            }
        },
        plugins: [{
            beforeDraw: drawCenterText
        }, ChartDataLabels]
    });
