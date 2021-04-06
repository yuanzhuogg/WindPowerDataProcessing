import tornado.ioloop
import tornado.web
import sys, asyncio
import os
from controller  import  index,updata
#
# if sys.platform == 'win32':
# 	asyncio.set_event_loop_policy(\
# 	asyncio.WindowsSelectorEventLoopPolicy())


def make_app():

    # 获取当前路径
    _dir_ = os.getcwd()
    #配置静态资源访问路径
    setting={

        "template_path":_dir_ + "/template",
        "static_path":_dir_ + "/static"
    }
   #
    return tornado.web.Application([
        (r"/", index.MainHandler),
        (r"/stop", index.stop),
        (r"/zhendong", index.zhendong),
        (r"/api/info", updata.updata_info),
        (r"/api/page2_info", updata.get_page_data),
        (r"/api/power", updata.get_power),
        (r"/api/power_plt", updata.power_plt_data),
        (r"/api/dy_power_plt", updata.dy_power_data),
        (r"/power", index.power_lot),
        (r"/duifeng", index.duifeng),
        (r"/index_page", index.index_page),
        (r"/api/page2", updata.page2),
        (r"/api/page2_1", updata.page2_1)




    # **setting文件加入
    ],**setting)

if __name__ == "__main__":
    app = make_app()
    app.listen(8088)
    tornado.ioloop.IOLoop.current().start()