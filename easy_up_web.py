import tornado.ioloop 
import tornado.web
from tornado.options import define,options
import tornado.httpserver
"""这些包是用来网页循环消息接收访问和返回数据数据的头文件
"""
define("port",type=int,default=8081,help="运行这个地址和端口号") #定义端口号

class IndexHeadle(tornado.web.RequestHandler):
    def get(self):   #服务器得到请求 返回初始界面
        self.render("前端.html")
    def post(self): 
        file_metas = self.request.files["sc_fwq"] #获得网页上上传的数据
        for meta in file_metas:
            file_name = meta["filename"] #获取文件名
            with open("./file/"+file_name,"wb") as w:
                w.write(meta["body"])  #把文件内容写到其他文件里
                self.write(meta["filename"]+"上传成功\n")

urls = [(r"/",IndexHeadle),]  #路由映射 html文件里打开路径 映射到python代码里


def main():
  """网页显示和接收返回数据
  """
    tornado.options.parse_command_line()
    app = tornado.web.Application(urls)
    app.listen(options.port)
    tornado.ioloop.IOLoop.current().start()

if __name__ =="__main__":
    main()
