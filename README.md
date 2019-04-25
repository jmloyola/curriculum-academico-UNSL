Generador de Currículum Académico para la Universidad Nacional de San Luis
============================
Este repositorio contiene el código fuente que yo uso para generar automáticamente mi currículum académico para la Universidad Nacional de San Luis (Argentina). El archivo final en formato `pdf` se genera desde un archivo en formato `yaml` con todos los datos necesarios.

Los campos válidos para completar el currículum académico son los que se encuentran en el artículo 35 de la ordenanza del consejo superior [OCS-1-15/97](http://digesto.unsl.edu.ar/docs/200606/20060626091521_18824.pdf).

## Requerimientos
* Python (>=3.6),
* MikTeX o cualquier otro procesador de LaTeX (se supone que los paquetes LaTeX están ahí o que MikTeX los instala al vuelo durante la compilación por primera vez),
* Jinja2.

## Cómo usarlo

Edita el archivo `cv.yaml` con tu información (lee las pautas en el encabezado), luego ejecuta el comando `make` en la consola. Esto generará un currículum académico en la carpeta `resultado`.

## Licencia

Este trabajo se distribuye bajo la licencia MIT con partes con derechos de autor de [Aleksandr Mattal](https://github.com/QuteBits/resume_42), [Brandon Amos](https://github.com/bamos/cv) y [Ellis Michael](https://github.com/emichael/resume). Sus porciones también se distribuyen bajo la licencia MIT (`LICENSE-qutebits.mit`, `LICENSE-bamos.mit` y `LICENSE-emichael.mit`).

## Agradecimientos

Este proyecto se basa en el trabajo realizado por [Aleksandr Mattal](https://github.com/QuteBits/resume_42).

## Contribuciones

Todo el contenido de este repositorio es abierto, esto quiere decir que cualquier persona interesada puede contribuir al mismo. Todas las contribuciones serán bien recibidas incluyendo:

- Correcciones ortográficas
- Correcciones en el código Python, incluidas mejoras de estilo

La forma de contribuir es vía GitHub, es decir los cambios deberán ser hechos en forma de pull requests y los problemas / bugs deberán reportarse como Issues.