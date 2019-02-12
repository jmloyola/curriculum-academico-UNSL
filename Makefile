# Makefile to build PDF and Markdown cv from YAML.
#
# Juan Martin Loyola <https://jmloyola.github.io/> and 
# Brandon Amos <http://bamos.github.io> and
# Ellis Michael <http://ellismichael.com>

TEMPLATES=$(shell find templates -type f)

LANGUAGE=spanish
TYPE=unsl
PARENT_RESULT_DIR=result
RESULT_DIR=$(PARENT_RESULT_DIR)/$(LANGUAGE)
TEX=$(RESULT_DIR)/$(TYPE).tex
PDF=$(RESULT_DIR)/$(TYPE).pdf
YAML_FILE = cv.yaml

.PHONY: all viewpdf clean

all: $(PDF)

$(RESULT_DIR):
	mkdir -p $(RESULT_DIR)

$(TEX): $(RESULT_DIR) $(TEMPLATES) $(YAML_FILE) generate_cv.py
	python generate_cv.py $(YAML_FILE) --document_type $(TYPE) --language $(LANGUAGE)

$(PDF): $(TEX)
	latexmk -pdf -cd- -jobname=$(RESULT_DIR)/$(TYPE) $(RESULT_DIR)/$(TYPE)
	latexmk -c -cd $(RESULT_DIR)/$(TYPE)

viewpdf: $(PDF)
	evince $(PDF)

clean:
	rm -rf $(PARENT_RESULT_DIR)/*