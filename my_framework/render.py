from jinja2 import Template
import os

#
def render(template_name, folders='templates', **kwargs):
    """
    :param template_name: имя шаблона
    :param kwargs: параметры для передачи в шаблон
    :return:
    """
    path = os.path.join(folders, template_name)
    with open(path, encoding='utf-8') as file:
        template = Template(file.read())
    return template.render(**kwargs)


# class Render:
#     def __init__(self, template_name):
#         self.template_name = template_name
#         self.folder = 'templates'
#
#     def __call__(self, *args, **kwargs):
#         path = os.path.join(self.folder, self.template_name)
#         with open(path, encoding='utf-8') as file:
#             template = Template(file.read())
#         return template.render(**kwargs)
