import os
from dataclasses import dataclass
from typing import Optional


@dataclass(frozen=True)
class HTTPConfiguration:
    host: str
    port: int


@dataclass(frozen=True)
class SentryConfiguration:
    dsn: Optional[str]


@dataclass(frozen=True)
class Configuration:
    debug: bool
    environment: Optional[str]
    before_graceful_termination: int
    http: HTTPConfiguration
    sentry: SentryConfiguration


def init_config(d: dict = None) -> Configuration:
    d = d or os.environ
    return Configuration(
        d.get('{{ cookiecutter.package_name|upper }}_DEBUG', str(False)).upper() == str(True).upper(),
        d.get('{{ cookiecutter.package_name|upper }}_ENVIRONMENT'),
        int(d.get('{{ cookiecutter.package_name|upper }}_BEFORE_GRACEFUL_TERMINATION', 10)),
        HTTPConfiguration(
            d.get('{{ cookiecutter.package_name|upper }}_HTTP_HOST', '0.0.0.0'),
            int(d.get('{{ cookiecutter.package_name|upper }}_HTTP_PORT', 8000)),
        ),
        SentryConfiguration(d.get('{{ cookiecutter.package_name|upper }}_SENTRY_DSN')),
    )
