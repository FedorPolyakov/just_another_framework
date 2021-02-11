from my_framework.render import render


class PageNotFound:
    def __call__(self, request):
        print(request)
        return '404 WRONG PAGE', '<h1>404 PAGE =(<h1>'


class MyFramework:
    def __init__(self, routes: dict, front_controllers: list):
        self.routes = routes
        self.front_controllers = front_controllers

    def __call__(self, environ, start_response):
        print('framework works')
        path = environ['PATH_INFO']
        print(path)
        if path in self.routes:
            view = self.routes[path]
        else:
            path_ = path+'/'
            if path_ in self.routes:
                view = self.routes[path_]
            else:
                view = PageNotFound()
        request = {}
        for front in self.front_controllers:
            front(request)
        code, body = view(request)
        # print(code)
        # print(body)
        start_response(code, [('Content-Type', 'text/html')])
        return [body.encode('utf-8')]


# application = MyFramework(routes, front_controllers)


