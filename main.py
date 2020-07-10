# .travis.yml
config = """
language: python
python:
  #Python versions
  - '2.7'
  - '3.7'
  # PyPy versions
  - 'pypy'
  - 'pypy3'
# command to install dependencies
install:
  - pip install -r requirements.txt
# command to run tests
script: "pytest"
"""
