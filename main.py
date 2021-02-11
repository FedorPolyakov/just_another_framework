from my_framework.just_another_framework import MyFramework
import views

routes = {
    '/': views.IndexView(),
    '/about/': views.AboutView(),
}


class FirstFront:
    def __call__(self, request):
        print(request)
        request['first'] = 'first'
        return request


front_controllers = [FirstFront()]


application = MyFramework(routes, front_controllers)
