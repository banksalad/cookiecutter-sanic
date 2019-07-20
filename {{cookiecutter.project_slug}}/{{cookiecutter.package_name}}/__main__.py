from .app import create_app
from .config import init_config


def main():
    config = init_config()
    app = create_app(config)
    app.go_fast(
        host=config.http.host, port=config.http.port, debug=config.debug
    )


main()
