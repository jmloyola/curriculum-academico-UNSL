# Makefile to build PDF and Markdown cv from YAML.
#
# Juan Martin Loyola <https://jmloyola.github.io/> and 
# Brandon Amos <http://bamos.github.io> and
# Ellis Michael <http://ellismichael.com>

TEMPLATES=$(shell find templates -type f)

RESULT_DIR=result
TEX=$(RESULT_DIR)/cv.tex
PDF=$(RESULT_DIR)/cv.pdf
YAML_FILES = cv.yaml

.PHONY: all public viewpdf clean

all: $(PDF)

$(RESULT_DIR):
	mkdir -p $(RESULT_DIR)

public: $(RESULT_DIR) $(TEMPLATES) $(YAML_FILES) generate_cv.py
	python generate_cv.py cv.yaml

$(TEX): $(TEMPLATES) $(YAML_FILES) generate_cv.py
	python generate_cv.py $(YAML_FILES)

$(PDF): $(TEX)
	latexmk -pdf -cd- -jobname=$(RESULT_DIR)/cv $(RESULT_DIR)/cv
	latexmk -c -cd $(RESULT_DIR)/cv

viewpdf: $(PDF)
	gnome-open $(PDF)

clean:
	rm -rf $(RESULT_DIR)/cv*