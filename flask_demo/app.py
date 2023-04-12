# 从flask这个包中导入Flask类
from flask import Flask, request, render_template
from datetime import datetime

# 使用Flask类创建一个app对象
# __name__:代表当前app.py这个模块
# 1.以后出现bug，它可以帮助我们快速定位
# 2.对于寻找模板文件，有一个相对路径
# 暂时不理解也没关系，固定这么写就行
app = Flask(__name__)


# 当作过滤器的函数
# value就是使用过滤器的时候,|前面的值
# format1就是自己定义的格式,不写也行
# datetime的一个方法,叫strftime,按照format1的格式转换成字符串
def datetime_formate(value, format1="%Y年-%m月-%d日 %H:%M"):
    return value.strftime(format1)


# 如何当作过滤器
# 使用app自带的函数add_template_filter(过滤函数,过滤器的名字(模板文件中直接放在|后使用,类似内置过滤器length这样))
app.add_template_filter(datetime_formate, "dformat")


class User:
    def __init__(self, username, email):
        self.username = username
        self.email = email

# 创建一个路由和视图函数的映射
# https://www.baidu.com,根路由/根路径
# /home/user/xx
# 装饰器，根路由
# http://127.0.0.1:5000
# @app.route('/')
# def hello_world():
#     return 'Hello world！'
#
# # url: http[80]/https[443]://www.qq.com:443/path
# # url与视图：准确地讲是path与视图
# # 定义无参URL
# # http://127.0.0.1:5000/profile
# @app.route('/profile')
# def profile():
#     return "我是个人中心！"
#
#
# @app.route('/blog/list')
# def blog_list():
#     return "我是博客列表！"
#
#
# # 定义有参URL：将参数固定到了path中
# # http://127.0.0.1:5000/blog/hazel_blog
# # @app.route('/blog/int: <blog_id>')
# @app.route('/blog/<blog_id>')
# def blog_detail(blog_id):
#     return "您访问的博客是：%s" % blog_id
#
#
# # /book/list：会给我返回第一页的数据
# # /book/list?page=2，获取第二页的数据
# # http://127.0.0.1:5000/book/list?page=2
# @app.route('/book/list')
# def book_list():
#     # arguments:参数
#     # request.args:类字典类型
#     page = request.args.get("page", default=1, type=int)
#     return f"您获取的是第{page}页的图书列表！"
#
# 1.debug模式：自动加载修改后的代码，浏览器上直接看到新代码
# 1.1 开启debug模式后，只要修改代码后保存，就会自动重新加载，不需要手动重启项目
# 1.2 如果开发的时候，出现bug，如果开启了debug模式，在浏览器上可以直接看到出错信息
#
# 2.修改host：
# 主要的作用：就是让其他电脑能访问到我电脑上的flask项目
#
# 3.修改port端口号：
# 主要的作用，如果5000端口被其他程序占用了，那么可以通过修改port来监听新的端口号


# jinja2模板渲染:render_template自动到文件夹templates下面找到指定的文件名进行渲染，比如index.html
@app.route('/')
def hello_world():
    # 如果user信息是一个类User
    user = User(username="用户名:hairong", email="邮箱:xx.qq.cm")
    # 如果user信息不是类,只是个普通的字典
    person = {
        "username": "张三",
        "email": "zhangsan@qq.com"
    }
    return render_template("index.html", user=user, person=person)


# jinja2模板渲染:变量访问，带参数进html文件，blog_id是url里自己输入的
@app.route("/blog/<blog_id>")
def blog_detail(blog_id):
    return render_template("blog_detail.html", blog_id=blog_id, username="hair")


# jinja2过滤器使用:jinja2文件里,可以直接写变量进行渲染,但有些变量需要先经过一些处理,然后再进行渲染. 也就是说要先把这些变量扔给一个函数,这个函数处理完成之后再进行渲染.这个操作就叫做过滤器. 用管道操作符 | 来实现.
@app.route("/filter")
def filter_demo():
    user = User(username="用户名:hairong", email="邮箱:xx.qq.cm")
    mytime = datetime.now()
    return render_template("filter.html", user=user, mytime=mytime)


# jinja2控制语句：if/else/for关键字
@app.route("/control")
def control_statement():
    age = 19
    books = [{
        "name": "三国演义",
        "author": "罗贯中"
    }, {
        "name": "水浒传",
        "author": "施耐庵"
    }]
    return render_template("control.html", age=age, books=books)


# jinja2模板继承：用extends，block关键字
@app.route("/child1")
def child1():
    return render_template("child1.html")


@app.route("/child2")
def child2():
    return render_template("child2.html")


# jinja2静态文件加载:css,JS,图片，用url_for关键字
@app.route("/static")
def static_demo():
    return render_template("static.html")


if __name__ == '__main__':
    # app.run(host='0.0.0.0', port=8000, debug=True)
    app.run(debug=True)
