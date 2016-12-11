# FLask WEB 开发读书笔记

### 2016年12月06日 前四章知识总结
* 视图函数可以返回三个参数, 响应内容, HTTP状态码, 首部字典
* 视图函数也可以返回一个响应对象(Response), 在有特殊需求的时候可以选择返回它,如,写cookie.

* Flask 有两种上下文全局变量:
  程序上下文,分别是current_app和g, 当前激活程序的程序实例和用于临时存储的全局变量每次请求后都会进行重设.
  请求上下文, request和session

* Flask 在分发请求之前推送这些上下文, 请求处理完成之后将他们删除.

* 除了使用app.route装饰器注册路由之外, 还可以使用app.add_url_rule()方法生成映射.

* app.url_map可以查看先用的路由映射.

* 除了使用Flask-Bootstrap的基类之外, 还可以自己定义基类.

* Flash函数的模板也可以定义在自己定义的基类里.

* 可以通过app.errorhandler(error=404)装饰器注册自定义的错误界面

* url_for(endpoint,args,_external), _external设为True, 函数将会返回绝对链接.

* Flask-script 可以让项目支持命令行参数, 默认包含 runserver 和 runshell

