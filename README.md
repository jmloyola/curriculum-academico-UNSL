YAML to PDF Resume Generator
============================
This repo contains the source I use to automatically generate my curriculum vitae and resume as PDF from YAML input.

## Requirements:
* Python (I tested it on Python 3.6.4),
* MikTeX or any other LaTeX processor (LaTeX packages are assumed to be there or to be installed on-the-fly by MikTeX during compiling for the first time),
* Jinja2.

## Usage:

Edit the file `cv.yaml` with your information (read the guidelines in the header), then run this command in the console: `python generate_cv.py && cd result && pdflatex cv.tex && pdflatex cv.tex`. We compile the TeX file twice so that the page numbering would be correct (TeX doesn't know how many pages you compile during the first run).

## License:

This work is distributed under the MIT license with portions copyrighted by [Aleksandr Mattal](https://github.com/QuteBits/resume_42), [Brandon Amos](https://github.com/bamos/cv) and [Ellis Michael](https://github.com/emichael/resume). Their portions are also distributed under the MIT license (`LICENSE-qutebits.mit`, `LICENSE-bamos.mit` and `LICENSE-emichael.mit`).

## Acknowledgements:

This project is based in the work done by [Aleksandr Mattal](https://github.com/QuteBits/resume_42).
