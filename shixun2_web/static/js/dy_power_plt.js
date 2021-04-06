
function dy_power_plt() {

var myChart = echarts.init(document.getElementById('main'));


var time = []
var pwra = []
var pwrp = []

$.get('/api/power').done(function (response) {


        for (var i = 0;  i< response.power.data.length; i++) {
           time[i]= response.power.data[i][0]
           pwra[i]= response.power.data[i][1]
           pwrp[i]= response.power.data[i][2]


        }
 myChart.setOption({
    title: {
        text: '电量图'
    },
    tooltip: {
        trigger: 'axis',
        axisPointer: {
            type: 'cross',
            label: {
                backgroundColor: '#6a7985'
            }
        }
    },
    legend: {
        data: ['实发电量', '理论电量']
    },
    toolbox: {
        feature: {
            saveAsImage: {}
        }
    },
    grid: {
        left: '3%',
        right: '4%',
        bottom: '3%',
        containLabel: true
    },
    xAxis: [
        {
            type: 'category',
            boundaryGap: false,
            data: time,
            axisLabel: {
                            show: true,
                            textStyle: {
                                color: '#fff'
                            }
                        }
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
        {
            name: '实发电量',
            type: 'line',
            stack: '总量',
            areaStyle: {},
            data: pwra
        },

        {
            name: '理论电量',
            type: 'line',
            stack: '总量',
            label: {
                normal: {
                    show: true,
                    position: 'top'
                }
            },
            areaStyle: {},
            data: pwrp
        }
    ]
});



});


//   myChart.setOption(option);

 };
