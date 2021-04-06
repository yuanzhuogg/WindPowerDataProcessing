
import pandas as pd
import pymysql



# //page1 的左侧数据
times_p = 1
times_f = 13


# //page2 右下的数据
times_p2 = 1
times_f2 = 6

# //page2 动态功率的数据
times_p3 = 1
times_f3 = 30


# 发电量累加
power_p = 1
power_f = 7

class get_info(object):

    # 开始读取左侧数据
    def start(self):
        global times_p
        global times_f
        # 1.连接到mysql数据库
        conn = pymysql.connect(host='localhost', user='root', password='123456', db='shixun_info', charset='utf8')
        # localhost连接本地数据库 user 用户名 password 密码 db数据库名称 charset 数据库编码格式

        # 2.创建游标对象
        cursor = conn.cursor()  # cursor当前的程序到数据之间连接管道

        # 3.组装sql语句 需要查询的MySQL语句
        sql = "select * from info  where id >={} and id<={}".format(times_p,times_f)
        # sql = "select * from info  where id >=1 and id<=15"


        times_p = times_f
        times_f += 13;
        # 4.执行sql语句
        cursor.execute(sql)

        # 5.处理结果集
        all = cursor.fetchall()

        data=[]
        # 逐条输出获取到的数据类型及数据
        for each in all:
            # print(type(each), list(each))
            data.append(list(each[1:]))


        # 6.关闭所有的连接
        # 关闭游标
        cursor.close()
        # 关闭数据库
        conn.close()

        return data


# <------------------------------------------------------------------>

    # //获取发电量
    def get_power(self):
        global power_p
        global power_f
        # 1.连接到mysql数据库
        conn = pymysql.connect(host='localhost', user='root', password='123456', db='shixun_info', charset='utf8')
        # localhost连接本地数据库 user 用户名 password 密码 db数据库名称 charset 数据库编码格式

        # 2.创建游标对象
        cursor = conn.cursor()  # cursor当前的程序到数据之间连接管道

        # 3.组装sql语句 需要查询的MySQL语句
        sql = "select * from power  where id >={} and id<={}".format(power_p, power_f)
        # sql = "select * from info  where id >=1 and id<=15"

        power_p += 1
        power_f += 1;
        # 4.执行sql语句
        cursor.execute(sql)

        # 5.处理结果集
        all = cursor.fetchall()

        data = []
        # 逐条输出获取到的数据类型及数据
        for each in all:
            # print(type(each), list(each))
            data.append(list(each[1:]))

        # 6.关闭所有的连接
        # 关闭游标
        cursor.close()
        # 关闭数据库
        conn.close()

        return data
        # //获取发电量


# //获取发电量曲线
    def power_lot(self):

        # 1.连接到mysql数据库
        conn = pymysql.connect(host='localhost', user='root', password='123456', db='shixun_info', charset='utf8')
        # localhost连接本地数据库 user 用户名 password 密码 db数据库名称 charset 数据库编码格式

        # 2.创建游标对象
        cursor = conn.cursor()  # cursor当前的程序到数据之间连接管道

        # 3.组装sql语句 需要查询的MySQL语句
        sql = "select * from power_2  "

        # 4.执行sql语句
        cursor.execute(sql)

        # 5.处理结果集
        all = cursor.fetchall()

        data = []
        # 逐条输出获取到的数据类型及数据
        for each in all:
            # print(type(each), list(each))
            data.append(list(each))

        # 6.关闭所有的连接
        # 关闭游标
        cursor.close()
        # 关闭数据库
        conn.close()

        return data


# //第二个页面数据
    def get_page2_data(self):
        global times_p2
        global times_f2
        # 1.连接到mysql数据库
        conn = pymysql.connect(host='localhost', user='root', password='123456', db='shixun_info', charset='utf8')
        # localhost连接本地数据库 user 用户名 password 密码 db数据库名称 charset 数据库编码格式

        # 2.创建游标对象
        cursor = conn.cursor()  # cursor当前的程序到数据之间连接管道

        # 3.组装sql语句 需要查询的MySQL语句
        sql = "select * from info  where id >={} and id<={}".format(times_p2, times_f2)
        # sql = "select * from info  where id >=1 and id<=15"

        times_p2  = times_f2
        times_f2 += 6
        # 4.执行sql语句
        cursor.execute(sql)

        # 5.处理结果集
        all = cursor.fetchall()

        data = []
        # 逐条输出获取到的数据类型及数据
        for each in all:
            # print(type(each), list(each))
            data.append(list(each[1:]))

        # 6.关闭所有的连接
        # 关闭游标
        cursor.close()
        # 关闭数据库
        conn.close()

        return data
        # //获取发电量

# //第二个页面发电率的数据
    def dy_power_plt(self):
        global times_p3
        global times_f3
        # 1.连接到mysql数据库
        conn = pymysql.connect(host='localhost', user='root', password='123456', db='shixun_info', charset='utf8')
        # localhost连接本地数据库 user 用户名 password 密码 db数据库名称 charset 数据库编码格式

        # 2.创建游标对象
        cursor = conn.cursor()  # cursor当前的程序到数据之间连接管道

        # 3.组装sql语句 需要查询的MySQL语句
        sql = "select * from dy_power_plt  where id >={} and id<{}".format(times_p3, times_f3)
        # sql = "select * from info  where id >=1 and id<=15"

        times_p3  = times_f3
        times_f3 += 30
        # 4.执行sql语句
        cursor.execute(sql)

        # 5.处理结果集
        all = cursor.fetchall()

        data = []
        # 逐条输出获取到的数据类型及数据
        for each in all:
            # print(type(each), list(each))
            data.append(list(each[1:]))

        # 6.关闭所有的连接
        # 关闭游标
        cursor.close()
        # 关闭数据库
        conn.close()

        return data
        # //获取发电量

    def page2(self):
        # 1.连接到mysql数据库
        conn = pymysql.connect(host='localhost', user='root', password='123456', db='shixun_info', charset='utf8')
        # localhost连接本地数据库 user 用户名 password 密码 db数据库名称 charset 数据库编码格式

        # 2.创建游标对象
        cursor = conn.cursor()  # cursor当前的程序到数据之间连接管道

        # 3.组装sql语句 需要查询的MySQL语句
        sql = 'select * from page2 '

        # 4.执行sql语句
        cursor.execute(sql)

        # 5.处理结果集
        all = cursor.fetchall()

        data = []
        # 逐条输出获取到的数据类型及数据
        for each in all:
            # print(type(each), list(each))
            data.append(list(each))

        # 6.关闭所有的连接
        # 关闭游标
        cursor.close()
        # 关闭数据库
        conn.close()

        return data

    def page2_1(self):
        global times_p;
        global times_f;
        # 1.连接到mysql数据库
        conn = pymysql.connect(host='localhost', user='root', password='123456', db='shixun_info', charset='utf8')
        # localhost连接本地数据库 user 用户名 password 密码 db数据库名称 charset 数据库编码格式

        # 2.创建游标对象
        cursor = conn.cursor()  # cursor当前的程序到数据之间连接管道

        # 3.组装sql语句 需要查询的MySQL语句
        sql = 'select * from page2  where id >={} and id <{} '.format(times_p, times_f)

        times_p += 1
        times_f += 1

        # 4.执行sql语句
        cursor.execute(sql)

        # 5.处理结果集
        all = cursor.fetchall()

        data = []
        # 逐条输出获取到的数据类型及数据
        for each in all:
            # print(type(each), list(each))
            data.append(list(each[1:]))

        # 6.关闭所有的连接
        # 关闭游标
        cursor.close()
        # 关闭数据库
        conn.close()

        return data




