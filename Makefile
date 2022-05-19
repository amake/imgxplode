SHELL := /bin/bash
env := .env

.PHONY: all
all: test

.PHONY: test
test: ## Run tests
test: clean | $(env)
	$(env)/bin/python imgxplode.py test.png
	@(( $$(find . -name 'test-*.png' | wc -l) == 3 )) && echo ok

$(env):
	virtualenv $(@)
	$(@)/bin/pip install pillow

.PHONY: clean
clean: ## Remove some things
	rm -rf test-*.png

.PHONY: clobber
clobber: ## Remove all the things
	rm -rf $(env)

.PHONY: help
help: ## Show this help text
	$(info usage: make [target])
	$(info )
	$(info Available targets:)
	@awk -F ':.*?## *' '/^[^\t].+?:.*?##/ \
         {printf "  %-24s %s\n", $$1, $$2}' $(MAKEFILE_LIST)
