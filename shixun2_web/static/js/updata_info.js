 

 function updata_info() {
//

$.get('/api/info').done(function (response) {
	
	 var str = " <thead><tr><th scope='col'>时间</th><th scope='col'>功率</th><th scope='col'>风速</th><th scope='col'>偏向角</th></tr></thead><tbody>";//把数据组装起来
                        for (var i = 0;  i< response.info.data.length; i++) {
                            str += "<tr><td>" + response.info.data[i][0] +
                                "</td><td>" + response.info.data[i][1] +
                                "</td><td>" + response.info.data[i][2] +
                                "</td><td>" + response.info.data[i][3] +
                                "</td></tr><tbody>";
                        }
                        $("#updata_info").html(str);//把拼好的样式填到指定的位置，一个Ajax的表格刷新功能就完成了
           
            });

    };