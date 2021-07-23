from aiohttp.web_app import Application

from views.home import HomePageView


def set_routes(app: Application):
    app.router.add_get('', HomePageView)

