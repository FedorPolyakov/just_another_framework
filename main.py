from my_framework.just_another_framework import MyFramework
from wsgiref.simple_server import make_server
from urls import routes


class FirstFront:
    def __call__(self, request):
        request['first'] = 'FirstFront'
        return request


front_controllers = [FirstFront()]
application = MyFramework(routes, front_controllers)
with make_server('', 8000, application) as httpd:
    print("Serving on port 8000...")
    httpd.serve_forever()
