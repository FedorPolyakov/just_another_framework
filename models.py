from patterns.prototype import PrototypeMixin


class User:
    pass


class Coach(User):
    pass


class Student(User):
    pass


class UserFactory:
    users_type = {
        'coach': Coach,
        'student': Student
    }

    @classmethod
    def create(cls, user_type_):
        return cls.users_type[user_type_]()


class Category:
    auto_id = 0

    def __init__(self, name, category):
        self.id = Category.auto_id
        Category.auto_id += 1
        self.name = name
        self.category = category
        self.training_courses = []

    def course_count(self):
        len_course = len(self.training_courses)
        if self.category:
            len_course += self.category.course_count()
        return len_course


class TrainingCourse(PrototypeMixin):

    def __init__(self, name, category):
        self.name = name
        self.category = category
        self.category.training_courses.append(self)


# курс дистанционных занятий
class DistanceCourse(TrainingCourse):
    pass


# курс очных занятий
class LiveCourse(TrainingCourse):
    pass


class CourseFactory:
    course_type = {
        'distance': DistanceCourse,
        'live': LiveCourse
    }

    @classmethod
    def create(cls, course_type_, name, category):
        return cls.course_type[course_type_](name, category)


class SiteInterface:
    def __init__(self):
        self.coaches = []
        self.students = []
        self.training_courses = []
        self.categories = []

    @staticmethod
    def create_user(type_):
        return UserFactory.create(type_)

    @staticmethod
    def create_category(name, category=None):
        return Category(name, category)

    def find_category_by_id(self, id):
        for item in self.categories:
            print(f'find_category_by_id - item - {item.id}')
            if item.id == id:
                return item
        raise Exception(f'There are not category with id = {id}')

    @staticmethod
    def create_training_course(type_, name, category_):
        return CourseFactory.create(type_, name, category_)

    def get_course(self, name) -> TrainingCourse:
        for item in self.training_courses:
            print(f'item - {item.name}')
            if item.name == name:
                return item
        return None
