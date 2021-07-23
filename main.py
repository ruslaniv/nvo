import aiohttp_jinja2
import jinja2
from aiohttp import web
from aiohttp.web import run_app
from aiohttp.web_app import Application
from router import set_routes


def create_app() -> Application:
    app = web.Application()
    set_routes(app)
    aiohttp_jinja2.setup(app, loader=jinja2.FileSystemLoader('templates'))
    return app


def main():
    app = create_app()
    run_app(app)


if __name__ == '__main__':
    main()
