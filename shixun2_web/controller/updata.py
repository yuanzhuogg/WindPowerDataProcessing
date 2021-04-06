
import tornado.web
from server import fo


# //实时更新数据
class updata_info(tornado.web.RequestHandler):
    def get(self):

        results = fo.start()

        result=dict()

        result['info']=dict(data=results)

        self.finish(result)


# //获取发电量
class get_power(tornado.web.RequestHandler):
    def get(self):

        results = fo.get_power()

        result=dict()

        result['power']=dict(data=results)

        self.finish(result)

# //获取功率曲线图像
class power_plt_data(tornado.web.RequestHandler):
    def get(self):

        results = fo.power_lot()

        result=dict()

        result['plt']=dict(data=results)

        self.finish(result)


# //获取第二个页面的data数据
class get_page_data(tornado.web.RequestHandler):
    def get(self):

        results = fo.get_page2_data()

        result=dict()

        result['info']=dict(data=results)

        self.finish(result)


# //获取动态功率曲线图像
class dy_power_data(tornado.web.RequestHandler):
    def get(self):

        results = fo.dy_power_plt()

        result=dict()

        result['dy_plt']=dict(data=results)

        self.finish(result)


class page2(tornado.web.RequestHandler):
    def get(self):

        results = fo.page2()

        result=dict()

        result['page2']=dict(data=results)

        self.finish(result)


class page2_1(tornado.web.RequestHandler):
    def get(self):

        results = fo.page2_1()

        result=dict()

        result['page2_1']=dict(data=results)

        self.finish(result)