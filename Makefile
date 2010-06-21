prereqs:
	sudo port install py26-virtualenv

dev:
	virtualenv-2.6 --no-site-packages .
	virtualenv-2.6 --relocatable .
	bin/python setup.py develop

test:
	bin/python setup.py test