from my_framework.render import render
from wsgiref.util import setup_testing_defaults
import quopri


class PageNotFound:
    def __call__(self, request):
        # print(request)
        return '404 WRONG PAGE', '<h1>404 PAGE =(<h1>'


class MyFramework:

    def change_bytes2str(self, data):
        data_b = bytes(data.replace('%', '=').replace("+", " "), 'UTF-8')
        data_str = quopri.decodestring(data_b)
        return data_str.decode('utf-8')

    def parse_input_data(self, data: str):
        rez = {}
        if data:
            parameters = data.split('&')
            for param in parameters:
                key, value = param.split('=')
                rez[key] = self.change_bytes2str(value)
        return rez

    def get_wsgi_input_data(self, environ) -> bytes:
        data_content_length = environ.get('CONTENT_LENGTH')
        content_length = int(data_content_length) if data_content_length else 0
        data = environ['wsgi.input'].read(content_length) if content_length > 0 else b''
        return data

    def parse_wsgi_input_data(self, data: bytes) -> dict:
        rez = {}
        if data:
            data_str = data.decode(encoding='utf-8')
            rez = self.parse_input_data(data_str)
        return rez

    def __init__(self, routes: dict, front_controllers: list):
        self.routes = routes
        self.front_controllers = front_controllers

    def __call__(self, environ, start_response):
        setup_testing_defaults(environ)

        # print(environ)
        path = environ['PATH_INFO']
        # print(f'PATH_INFO - {path}')
        query = environ['QUERY_STRING']
        method = environ['REQUEST_METHOD']
        request_params = self.parse_input_data(query)

        data = self.get_wsgi_input_data(environ)
        data = self.parse_wsgi_input_data(data)

        if path in self.routes:
            pass
        elif f'{path}/' in self.routes:
            path = f'{path}/'
        request = {}
        if path in self.routes:
            view = self.routes[path]
            request['method'] = method
            request['data'] = data
            request['request_params'] = request_params
            # print(request)
            for front in self.front_controllers:
                front(request)
            code, body = view(request)
        else:
            view = PageNotFound()
            code, body = view(request)
        # print(f'code - {code}')
        if code == '222 OK':
            start_response(code, [('Content-Type', 'text/css')])
        else:
            start_response(code, [('Content-Type', 'text/html')])
        return [body.encode('utf-8')]



