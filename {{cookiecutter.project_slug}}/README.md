# {{ cookiecutter.project_name }}

[![Python Version: 3.7](https://badgen.net/badge/python/3.7/blue)](https://docs.python.org/3.7/) [![Code Style: Black](https://badgen.net/badge/code%20style/black/black)](https://github.com/ambv/black)

{%- if cookiecutter.use_travis|lower == 'y' -%}
&nbsp;[![Build Status](https://badgen.net/badge/travis/passing/green)](https://travis-ci.com/)&nbsp;[![codecov](https://badgen.net/badge/coverage/100%25/green)](https://codecov.io/)
<!-- TODO: You should change codecov, travis badges to valid URL-->
{%- endif %}

## Getting Started

<!-- TODO: Describe how to prepare to use this project -->

### Installation

```sh
$ make
$ ./bin/install_hooks.sh
```

## Test

```sh
$ make check
$ make test
```

## Requirements

<!-- TODO: Describe stack of this project -->

* [Pipenv](https://github.com/pypa/pipenv) - Dependency management tool

## Related Documents

<!-- TODO: Insert related documents here-->

## License

<!-- TODO: If you want, set license information here-->
