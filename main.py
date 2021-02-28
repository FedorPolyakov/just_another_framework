from my_framework.just_another_framework import MyFramework
from wsgiref.simple_server import make_server
import views

routes = {
    '/': views.IndexView(),
    '/about/': views.AboutView(),
    '/contact/': views.ContactView(),
    '/static/style.css/': views.CSSView(),
    '/create_course/': views.CreateCourseView(),
    '/create_category/': views.CreateCategoryView(),
    '/course_list/': views.CourseListView(),
    '/category_list/': views.CategoryListView(),
    '/copy_course/': views.CopyCourseView()
}


class FirstFront:
    def __call__(self, request):
        # print(request)
        request['first'] = 'FirstFront'
        return request


front_controllers = [FirstFront()]


application = MyFramework(routes, front_controllers)

with make_server('', 8000, application) as httpd:
    print("Serving on port 8000...")
    httpd.serve_forever()


