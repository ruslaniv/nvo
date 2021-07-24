import os
import aiohttp_jinja2
from aiohttp import web
from dotenv import load_dotenv

load_dotenv()
user = os.environ.get("POSTGRES_USER")


class HomePageView(web.View):
    @aiohttp_jinja2.template('home.jinja2')
    async def get(self) -> dict:
        return {"user": user}


class WebPostView(web.View):
    async def post(self):
        req = await self.request.json()
        return web.json_response(req)
