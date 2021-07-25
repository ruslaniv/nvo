import os
import aiohttp_jinja2
from aiohttp import web
from dotenv import load_dotenv

from utils.parser import parse_response
from workers.database import write_request_to_db
from workers.file import write_request_to_file

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


class FilePostView(web.View):
    async def post(self):
        req = await self.request.json()
        resp = await write_request_to_file(req)
        _ = parse_response(resp)
        return web.json_response(_["messages"], status=_["status"]["status_code"])


class DatabasePostView(web.View):
    async def post(self):
        req = await self.request.json()
        response = await write_request_to_db(req)
        _ = parse_response(response)
        return web.json_response(_["messages"], status=_["status_code"])