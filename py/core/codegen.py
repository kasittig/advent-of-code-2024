from jinja2 import Environment, PackageLoader, select_autoescape
import os

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

    generate_imports()


def generate_imports() -> None:
    import_template = env.get_template("init_template.jinja")
    days = get_days()
    import_contents = import_template.render(days=days)
    with open("solutions/__init__.py", "w") as import_file:
        import_file.write(import_contents)


def get_days() -> list[str]:
    days: list[str] = []
    for i in range(25):
        if os.path.exists(get_default_solution_filename(str(i))):
            days.append(str(i))
    return days
