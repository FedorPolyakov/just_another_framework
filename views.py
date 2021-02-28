from my_framework.render import render
from logger import Logger
from models import SiteInterface
from my_framework.just_another_framework import MyFramework


site = SiteInterface()
log = Logger('views')


class CSSView:
    def __call__(self, request):
        return '222 OK', render('style.css', template_folder='./static/')


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


class CourseListView:
    def __call__(self, request):
        log.log('List of training courses')
        print(f'List of training courses - {site.training_courses}')
        return '200 OK', render('course_list.html', objects_list=site.training_courses)


class CreateCourseView:
    def __call__(self, request):
        if request['method'] == 'POST':
            data = request['data']
            name = data['name']
            category_id = data.get('category_id')
            category = None
            if category_id:
                category = site.find_category_by_id(int(category_id))
                course = site.create_training_course('live', name, category)
                site.training_courses.append(course)
            return '200 OK', render('create_course.html')
        else:
            return '200 OK', render('create_course.html', categories=site.categories)


class CreateCategoryView:
    def __call__(self, request):
        if request['method'] == 'POST':
            data = request['data']
            name = data['name']
            category_id = data.get('category_id')
            print(category_id)
            category = None
            if category_id:
                category = site.find_category_by_id(int(category_id))
            new_category = site.create_category(name, category)
            site.categories.append(new_category)
            return '200 OK', render('create_category.html')
        else:
            return '200 OK', render('create_category.html', categories=site.categories)


class CopyCourseView:
    def __call__(self, request):
        params = request['request_params']
        name = params['name']
        old_course = site.get_course(name)
        if old_course:
            copy_name = f'copy_{name}'
            copy_course = old_course.clone()
            copy_course.name = copy_name
            site.training_courses.append(copy_course)

        return '200 OK', render('course_list.html', objects_list=site.training_courses)


class CategoryListView:
    def __call__(self, request):
        log.log('List of categories')
        print(f'List of categories - {site.training_courses}')

        return '200 OK', render('category_list.html', objects_list=site.categories)
