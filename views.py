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


class ContactView:
    def __call__(self, request):
        print(request)
        if request['method'] == 'POST':
            data = request['data']
            title = data['title']
            text = data['text']
            email = data['email']
            print(f'You have email from - {email} '
                  f'with title - {title} '
                  f'with text - {text}')
        return '200 OK', render('contact.html')
