# Makefile para construir el curriculum académico PDF desde YAML.
#
# Juan Martin Loyola <https://jmloyola.github.io/> and 
# Brandon Amos <http://bamos.github.io> and
# Ellis Michael <http://ellismichael.com>

TEMPLATES=$(shell find plantillas -type f)

RESULT_DIR=resultado
TEX=$(RESULT_DIR)/cv.tex
PDF=$(RESULT_DIR)/cv.pdf
YAML_FILE = cv.yaml

.PHONY: all viewpdf clean

all: $(PDF)

$(RESULT_DIR):
	mkdir -p $(RESULT_DIR)

$(TEX): $(RESULT_DIR) $(TEMPLATES) $(YAML_FILE) generate_cv.py
	python generate_cv.py $(YAML_FILE)

$(PDF): $(TEX)
	latexmk -pdf -cd- -jobname=$(RESULT_DIR)/cv $(RESULT_DIR)/cv
	latexmk -c -cd $(RESULT_DIR)/cv

viewpdf: $(PDF)
	atril $(PDF)

clean:
	rm -rf $(RESULT_DIR)/*
