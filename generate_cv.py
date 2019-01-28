"""Generates LaTeX copies of my cv from a YAML file."""

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

# TODO: remove loc tag or variable from templates

def generate(yaml_contents, document_type, language, hide_personal_info):
    # TODO: si hide_personal_info == True quitar informacion personal (direccion, telefono, etc.)
    templates_dir = f'templates/{language}'
    env = Environment(loader=FileSystemLoader(templates_dir),
                  block_start_string='~{', block_end_string='}~',
                  variable_start_string='~{{', variable_end_string='}}~')
    body = ""
    section_template = f'{document_type}-section.tmpl.tex'
    # generate sections 1 by 1
    for section in yaml_contents['order']:
        contents = yaml_contents[section[0]]
        name = section[1].title()
        body += env.get_template(section_template).render(
          name = name.upper(),
          contents = contents
        )
    # generate the TeX wrapper and fill it with generated sections
    result = open(f'result/{language}/{document_type}.tex', 'w')
    document_template = f'{document_type}.tmpl.tex'
    result.write(env.get_template(document_template).render(
        name = yaml_contents['name'].upper(),
        email = yaml_contents['email'],
        body = body,
        today = date.today().strftime("%B %d, %Y")
    ))
    result.close()


def main():
    # Parse the command line arguments
    parser = argparse.ArgumentParser(description='Generates a LaTeX cv from data in a YAML file.')
    parser.add_argument('yaml', metavar='YAML_FILE', nargs='?', default='cv.yaml',
                        help='The YAML file that contain the resume/cv '
                        'details, in order of increasing precedence')
    parser.add_argument('--document_type', choices=['professional', 'academic', 'unsl'],
                        help='type of the generated cv')
    parser.add_argument('--language', choices=['english', 'spanish'],
                        help='language of the generated cv')
    parser.add_argument('--hide_personal_info', action='store_true',
                        help='does not include personal information in the generated cv')
    # TODO: armar distintos templates para los distintos tipos de cv.
    args = parser.parse_args()

    # read data yaml file
    with open(args.yaml, 'r') as f:
        yaml_contents = yaml.load(f)

    generate(yaml_contents, args.document_type, args.language, args.hide_personal_info)


if __name__ == "__main__":
    main()