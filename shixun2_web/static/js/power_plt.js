

function power() {

 var myChart = echarts.init(document.getElementById('power_main'));

var time = []
var pwra = []
var pwrp = []

$.get('/api/power_plt').done(function (response) {


        for (var i = 0;  i< response.plt.data.length; i++) {
           time[i]= response.plt.data[i][0]
           pwra[i]= response.plt.data[i][1]
           pwrp[i]= response.plt.data[i][2]


        }
        console.log(pwrp)

var colors = ['#5793f3', '#d14a61', '#675bba'];
myChart.setOption({
    color: colors,
    title: {
        text: '功率曲线',
        textStyle:{ //设置主标题风格
            color:'#fff'

            }
    },
    tooltip: {
        trigger: 'none',
        axisPointer: {
            type: 'cross'
        }
    },
    legend: {
        data:['实际功率', '理论功率']
    },
    grid: {
        top: 70,
        bottom: 50
    },
    xAxis: [
        {
            type: 'category',
            axisTick: {
                alignWithLabel: true
            },
            axisLine: {
                onZero: false,
                lineStyle: {
                    color: '#000'
                }
            },
            axisPointer: {
                label: {
                    formatter: function (params) {
                        return '理论功率 ' + params.value
                            + (params.seriesData.length ? '：' + params.seriesData[0].data : '');
                    }
                }
            },
            data: time
        },
        {
            type: 'category',
            axisTick: {
                alignWithLabel: true
            },
            axisLine: {
                onZero: false,
                lineStyle: {
                    color: '#000'
                }
            },
            axisPointer: {
                label: {
                    formatter: function (params) {
                        return '实际功率  ' + params.value
                            + (params.seriesData.length ? '：' + params.seriesData[0].data : '');
                    }
                }
            },
            data: time
        }
    ],
    yAxis: [
        {
            type: 'value',
            axisLabel: {
                            show: true,
                            textStyle: {
                                color: '#fff'
                            }
                        }

        }
    ],
    series: [
        {   symbol: "none",
            name: '实际功率',
            type: 'line',
            xAxisIndex: 1,
            smooth: true,
            data: pwra
        },
        {   symbol: "none",
            name: '理论功率',
            type: 'line',
            smooth: true,
            data: pwrp
        }
    ]
});





});


 };
