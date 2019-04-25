"""Generador de Currículum Académico para la Universidad Nacional de San Luis en formato PDF a partir de archivo YAML"""

__author__ = [
    'Juan Martin Loyola <https://jmloyola.github.io>'
    'Aleksandr Mattal <https://github.com/qutebits>'
    'Brandon Amos <http://bamos.github.io>',
    'Ellis Michael <http://ellismichael.com>',
]

import argparse
import yaml
from datetime import date
from jinja2 import Environment, FileSystemLoader

def generate(yaml_contents):
    templates_dir = 'plantillas'
    env = Environment(loader=FileSystemLoader(templates_dir),
                  block_start_string='~{', block_end_string='}~',
                  variable_start_string='~{{', variable_end_string='}}~')
    body = ""
    section_template = 'cv-section.tmpl.tex'
    # generate sections 1 by 1
    for section in yaml_contents['secciones_a_incluir']:
        contents = yaml_contents[section[0]]
        name = section[1].title()
        body += env.get_template(section_template).render(
          name = name.upper(),
          contents = contents
        )
    # generate the TeX wrapper and fill it with generated sections
    result = open('resultado/cv.tex', 'w')
    document_template = 'cv.tmpl.tex'
    result.write(env.get_template(document_template).render(
        body = body,
        today = date.today().strftime("%B %d, %Y")
    ))
    result.close()


def main():
    # Parse the command line arguments
    parser = argparse.ArgumentParser(description='Generates a LaTeX cv from data in a YAML file.')
    parser.add_argument('yaml', metavar='YAML_FILE', nargs='?', default='cv.yaml',
                        help='The YAML file that contain the cv '
                        'details, in order of increasing precedence')
    args = parser.parse_args()

    # read data yaml file
    with open(args.yaml, 'r') as f:
        yaml_contents = yaml.load(f)

    generate(yaml_contents)


if __name__ == "__main__":
    main()