# lambda-python

a boilerplate with codebuild buildspec.yml for building deployable lambda package using the python runtime

## Installation

Use the package manager [pipenv](https://pipenv.pypa.io/en/latest/) to install for development.

```bash
pipenv install -d
# this install Pipfile deps and dev-deps
```

## Testing

```bash
pipenv run pytest
# or just 'pytest' if virtualenv is active
```
