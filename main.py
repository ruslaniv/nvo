import aiohttp_jinja2
import jinja2
from aiohttp import web
from aiohttp.web import run_app
from aiohttp.web_app import Application

from db import db_conn
from router import set_routes


def main():
    configure(dev_mode=True)
    app = create_app()
    run_app(app)


def configure(dev_mode: bool):
    configure_db(dev_mode)


def configure_db(dev_mode: bool):
    db_conn.do_global_init()


def create_app() -> Application:
    app = web.Application()
    set_routes(app)
    aiohttp_jinja2.setup(app, loader=jinja2.FileSystemLoader('templates'))
    return app


if __name__ == '__main__':
    main()
else:
    configure(dev_mode=False)
