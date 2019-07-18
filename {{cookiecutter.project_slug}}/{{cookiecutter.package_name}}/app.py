from sanic import Sanic, response
from sentry_sdk import init as init_sentry
from sentry_sdk.integrations.sanic import SanicIntegration

from . import __version__, view
from .config import Configuration


def create_app(config: Configuration):
    app = Sanic(__name__)

    # Configure Sentry
    init_sentry(
        dsn=config.sentry.dsn,
        environment=config.environment,
        release=__version__,
        integrations=[SanicIntegration()],
    )

    @app.listener('before_server_start')
    async def init(app_, loop):
        pass

    @app.listener('after_server_stop')
    async def close(app_, loop):
        pass

    @app.route('/')
    async def index(_):
        return response.text(
            f'{{ cookiecutter.project_name }} ({__version__})'
        )

    app.blueprint(view.app)

    return app
