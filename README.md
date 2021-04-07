# WindPowerDataProcessing
 风力发电非常环保，且风能蕴量巨大，因此日益受到世界各国的重视。但是对于实际采集 到的测风数据及功率数据都存在各种各样的问题，需要有准确的实测数据来分析风电特征及发电规律 而且从风场收集到的数据中通常包含异常数据点，造成计算机进行数据筛选和排序的速度比较慢，因此 需要可靠有效的风电数据处理方法来筛选合理有效的数据以进行风电功率预测建模。
 
 
文件说明：

  文件（shixun2_web） 为python web项目，进行数据可视化；文件（数据处理代码） 为原始数据的处理代码；文件（shixun_info.sql）为已清洗好的数据

运行环境：
   数据清洗环境：  python 3.7 + pandas 0.24.1 + jupyter 1.0.0 + notebook 5.7.4 + pymysql 0.9.3；开发工具eclipse
   
   python web 项目运行环境：python 3.7 + tornado 6.0.2 ；开发工具pycharm
   
   
运行流程：
    进入app.py 文件  启动main 方法 ，浏览器访问地址 http://localhost:8088/index_page
  
 
