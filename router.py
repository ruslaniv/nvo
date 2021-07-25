from aiohttp.web_app import Application
from views.home import HomePageView, WebPostView, FilePostView

URL_PREFIX = "/api/v1"


def set_routes(app: Application):
    app.router.add_get('', HomePageView)
    app.router.add_post(f'{URL_PREFIX}/post/web', WebPostView, name='web')
    app.router.add_post(f'{URL_PREFIX}/post/file', FilePostView, name='file')


