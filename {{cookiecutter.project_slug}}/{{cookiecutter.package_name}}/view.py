from sanic.blueprints import Blueprint

app = Blueprint(  # pylint: disable=invalid-name
    'v1', version=1, strict_slashes=True
)
