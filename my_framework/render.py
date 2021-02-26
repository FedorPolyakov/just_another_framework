from jinja2 import Template, FileSystemLoader
from jinja2.environment import Environment
import os

#
def render(template_name, template_folder='templates', **kwargs):
    """
    :param template_name: имя шаблона
    :param template_folder: имя папки с шаблонами
    :param kwargs: параметры для передачи в шаблон
    :return:
    """
    print(f'template_folder - {template_folder}')
    env = Environment()
    env.loader = FileSystemLoader(template_folder)
    template = env.get_template(template_name)
    return template.render(**kwargs)

    # path = os.path.join(folders, template_name)
    # with open(path, encoding='utf-8') as file:
    #     template = Template(file.read())
