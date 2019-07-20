from typing import List, Iterator

import pytest


@pytest.mark.parametrize(
    'requirements', ['requirements.txt', 'requirements-dev.txt']
)
def test_requirements_include_specifiers(cookies, context, requirements):
    """
    We expect each package has `==` specifier
    ```
    1 black==19.3b0
    2 mypy==0.701
    ```
    """
    ctx = context()
    result = cookies.bake(extra_context=ctx)

    packages = result.project.join(requirements)
    content = packages.read()
    lines = content.strip().split('\n')

    assert all('==' in l for l in lines)


@pytest.mark.parametrize('packages', ['[packages]', '[dev-packages]'])
def test_pipfile_include_specifiers(cookies, context, packages):
    """
    We expect each package has `==` specifier
    ```
    1 [dev-packages]
    2 isort = "==4.3.20"
    3 black = "==19.3b0"
    4
    5 [packages]
    6 sanic = "==19.6.0"
    ```
    """
    ctx = context()
    result = cookies.bake(extra_context=ctx)

    pipfile = result.project.join('Pipfile')
    content = pipfile.read()
    sections = content.strip().split('\n\n')
    lines = filter(
        is_pipfile_requirement, split_section_to_lines(sections, packages)
    )

    assert all('==' in l for l in lines)


def split_section_to_lines(sections: List[str], title: str) -> Iterator[str]:
    for s in sections:
        if title in s:
            yield from s.split('\n')


def is_pipfile_requirement(line: str) -> bool:
    """
    >>> is_pipfile_requirement('isort = "==4.3.20"')
    True
    >>> is_pipfile_requirement('[dev-packages]')
    False
    """
    return len(line.split(' ')) == 3 and '=' in line
