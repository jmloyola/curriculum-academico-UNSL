"""Generates LaTeX copies of my cv from a YAML file."""

__author__ = [
    'Juan Martin Loyola <https://jmloyola.github.io>'
    'Aleksandr Mattal <https://github.com/qutebits>'
    'Brandon Amos <http://bamos.github.io>',
    'Ellis Michael <http://ellismichael.com>',
]

import yaml
from datetime import date
from jinja2 import Environment, FileSystemLoader

# read data yaml file
yaml_contents = yaml.load(open("cv.yaml", 'r'))

env = Environment(loader=FileSystemLoader("templates"),
                  block_start_string='~{', block_end_string='}~',
                  variable_start_string='~{{', variable_end_string='}}~')

# TODO: remove loc tag or variable from templates

def generate():
    body = ""
    # generate sections 1 by 1
    for section in yaml_contents['order']:
        contents = yaml_contents[section[0]]
        name = section[1].title()
        body += env.get_template("resume-section.tmpl.tex").render(
          name = name.upper(),
          contents = contents
        )
    # generate the TeX wrapper and fill it with generated sections
    result = open("result/cv.tex", 'w')
    result.write(env.get_template("resume.tmpl.tex").render(
    name = yaml_contents['name'].upper(),
    email = yaml_contents['email'],
    body = body
    ))
    result.close()

generate()