ROOT    := $(PWD)
PYTHON   = $(shell test -x bin/python && echo bin/python || echo `which python`)
SETUP    = $(PYTHON) setup.py
NAME    := $(shell $(SETUP) --name)

.PHONY: $(NAME).egg-info

prereqs:
	sudo port install py26-virtualenv

dev:
	virtualenv-2.6 --no-site-packages .
	virtualenv-2.6 --relocatable .
	bin/python setup.py develop

tags: TAGS.gz

TAGS.gz: TAGS
	gzip -f $^

TAGS: $(SOURCES)
	ctags -eR lib $(NAME) > $@

test:
	bin/python setup.py test

clean:
	rm -f TAGS* $(shell find . -type f -name \*.pyc)
