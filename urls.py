import views

routes = {
    # '/': views.IndexView,
    # '/about/': views.AboutView(),
    # '/contact/': views.ContactView(),
    # '/static/style.css/': views.CSSView(),
    # '/create_course/': views.CreateCourseView(),
    # '/create_category/': views.CreateCategoryView(),
    # '/course_list/': views.CourseListView(),
    # '/category_list/': views.CategoryListView(),
    # '/copy_course/': views.CopyCourseView()
}

routes.update(views.routes)