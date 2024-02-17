from typing import Any
from io import BytesIO

from jinja2 import Environment, FileSystemLoader
from weasyprint import HTML

from app.services.jinja2.templates import templates_dir
from app.services.bucket import bucket_service
from app.assets.logos import logos_dir


def format_as_money(number):
    rounded_number = round(number)
    
    str_number = str(rounded_number)
    parts = []
    while str_number:
        parts.append(str_number[-3:])
        str_number = str_number[:-3]

    formatted_money = "$" + ",".join(reversed(parts))
    return formatted_money



def generate_pdf(sale: dict[str, Any]) -> str:
    env = Environment(loader=FileSystemLoader(templates_dir))
    env.add_extension("jinja2.ext.i18n")
    env.filters["format"] = format_as_money
    template = env.get_template("factura.html.j2")
    render = template.render(sale)

    pdf = HTML(string=render, base_url=logos_dir).write_pdf()
    file = BytesIO()
    file.write(pdf)
    file.seek(0)

    response = bucket_service.post(file)
    return response["file_path"]["path"]
