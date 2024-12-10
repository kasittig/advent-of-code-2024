from jinja2 import Environment, PackageLoader, select_autoescape

from core.utils import get_default_solution_filename, get_default_test_filename

env = Environment(loader=PackageLoader("core"), autoescape=select_autoescape())


def generate_daily_template(day: str) -> None:
    code_template = env.get_template("daily_template.jinja")
    stub = code_template.render(day=day)
    with open(get_default_solution_filename(day), "w") as code_file:
        code_file.write(stub)

    test_template = env.get_template("daily_test_template.jinja")
    test_stub = test_template.render(day=day)
    with open(get_default_test_filename(day), "w") as test_file:
        test_file.write(test_stub)
