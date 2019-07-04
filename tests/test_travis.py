import pytest


def test_travis_total_lines(cookies, context):
    """
    We expect .travis.yml has below content
    ```
    1 sudo: required
    2
    3 language: python
    4
    5 install:
    6   - make
    ```
    """
    ctx = context()
    result = cookies.bake(extra_context=ctx)

    makefile = result.project.join('.travis.yml')
    lines = makefile.readlines(cr=False)

    expected = 32
    assert len(lines) == expected


def test_travis_total_section(cookies, context):
    ctx = context()
    result = cookies.bake(extra_context=ctx)

    makefile = result.project.join('.travis.yml')
    content = makefile.read()
    sections = content.strip().split('\n\n')

    expected = 10
    assert len(sections) == expected
