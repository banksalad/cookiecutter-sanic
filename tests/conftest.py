import pytest


@pytest.fixture
def context():
    def builder(travis='y'):
        return {
            'project_name': 'Rainist',
            'project_slug': 'rainist',
            'package_name': 'cookie',
            'use_travis': travis,
        }

    return builder
