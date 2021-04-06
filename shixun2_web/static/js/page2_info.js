 

 function updata_ap() {
//
$.get('/api/page2_1').done(function (response) {

	 var str = " <thead><tr><th scope='col'>时间</th><th scope='col'>预测功率</th><th scope='col'>实际功率</th>";
                        for (var i = 0;  i< response.page2_1.data.length; i++) {
                            str += "<tr><td>" + response.page2_1.data[i][0] +
                                "</td><td>" + response.page2_1.data[i][1] +
                                "</td><td>" + response.page2_1.data[i][2] +
                                "</td></tr><tbody>";
                        }
                        $("#page2_1").html(str);//把拼好的样式填到指定的位置，一个Ajax的表格刷新功能就完成了

            });

    };


