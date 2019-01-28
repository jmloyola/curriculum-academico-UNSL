YAML to PDF Resume Generator
============================
This repo contains the source I use to automatically generate my curriculum vitae and resume as PDF from YAML input.

## Requirements:
* Python (>=3.6),
* MikTeX or any other LaTeX processor (LaTeX packages are assumed to be there or to be installed on-the-fly by MikTeX during compiling for the first time),
* Jinja2.

## Usage:

Edit the file `cv.yaml` with your information (read the guidelines in the header), then run this command in the console: `make LANGUAGE=$desired_language TYPE=$desired_type`.

You will have to replace:
- `$desired_language` with _english_ or _spanish_, and
- `$desired_type` with _academic_, _professional_ or _unsl_.

This will generate a cv suited for the `$desired_type` and `$desired_language` you indicated.

## License:

This work is distributed under the MIT license with portions copyrighted by [Aleksandr Mattal](https://github.com/QuteBits/resume_42), [Brandon Amos](https://github.com/bamos/cv) and [Ellis Michael](https://github.com/emichael/resume). Their portions are also distributed under the MIT license (`LICENSE-qutebits.mit`, `LICENSE-bamos.mit` and `LICENSE-emichael.mit`).

## Acknowledgements:

This project is based in the work done by [Aleksandr Mattal](https://github.com/QuteBits/resume_42).
