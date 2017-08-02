install:
	python -m virtualenv --python python2.7 .
	. bin/activate && pip install -r requirements-dev.txt
	. bin/activate && python setup.py develop