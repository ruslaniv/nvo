import aiohttp_jinja2
from aiohttp import web


class HomePageView(web.View):
    @aiohttp_jinja2.template('home.jinja2')
    async def get(self) -> dict:
        return {"user": "Ruslan"}
