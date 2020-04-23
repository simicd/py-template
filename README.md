# Python Package Template
## Intro
This repo stores a template for Python packages and includes
- Simple folder structure with test folder
- Files with dependencies (requirements.txt)
- Installation instructions (setup.py) which generates a distributable Python package with `python setup.py bdist_wheel --universal` (might require `pip install wheel` beforehand)

## Documentation with Sphinx
- Create module structure as .rst file (required when there are new .py modules): `sphinx-apidoc -o docs/source/ pytemplate pytemplate/tests/* --force --separate --no-headings`. Options:
    - `-o <target> <package> <exclude>` define where to write the documentation source files
    - `--force` overwrite old files
    - `--separate` create a file for each module
    - `--no-headings` use module-level docstrings instead of default titles (module name)
- Create website based on .rst files in source folder: `sphinx-build -b html docs/source docs/build`

Requires: `sphinx_rtd_theme`, `sphinx_autodoc_typehints`

## Running unit tests and code coverage
`pytest --doctest-modules --junitxml=junit/test-results.xml --cov=pytemplate --cov-report=xml --cov-branch --ignore main.py`

Requires: `pytest`, `pytest-cov`