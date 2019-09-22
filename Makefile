DIRECTORIES := shmarray

all:

format:
	autoflake -r -i $(DIRECTORIES)
	isort -rc $(DIRECTORIES)
	black $(DIRECTORIES)

style-check:
	black --diff --check $(DIRECTORIES)
	flake8 --ignore E501,E203,F401,W503,W504 --radon-max-cc 13 $(DIRECTORIES)
	# mypy $(DIRECTORIES)


wheel:
	python3 setup.py sdist bdist_wheel

