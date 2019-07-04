import pytest


def test_makefile_total_lines(cookies, context):
    """
    We expect Makefile has below content
    ```
    1 check:
    2     isort
    3     black
    4
    5 format:
    6     isort
    7     black
    ```
    """
    ctx = context()
    result = cookies.bake(extra_context=ctx)

    makefile = result.project.join('Makefile')
    lines = makefile.readlines(cr=False)

    expected = 30
    assert len(lines) == expected


def test_makefile_total_section(cookies, context):
    ctx = context()
    result = cookies.bake(extra_context=ctx)

    makefile = result.project.join('Makefile')
    content = makefile.read()
    sections = content.strip().split('\n\n')

    expected = 8
    assert len(sections) == expected


def test_makefile_phony(cookies, context):
    ctx = context()
    result = cookies.bake(extra_context=ctx)

    makefile = result.project.join('Makefile')
    lines = makefile.readlines()
    phony = lines[0]

    expected = 8
    assert len(phony.split(' ')) == expected
