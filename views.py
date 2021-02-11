from my_framework.render import render


# my page_controller
class IndexView:
    def __call__(self, request):
        print(request)
        return '200 OK', render('index.html')


class AboutView:
    def __call__(self, request):
        print(request)
        return '200 OK', render('about.html')
