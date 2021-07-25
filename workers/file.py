from os.path import join
from typing import Union

import aiofiles, aiofiles.os
from datetime import datetime
import json
from pathlib import Path

from utils.timestamp import convert_timestamp


async def write_request_to_file(data: dict[str, Union[str, datetime]]) -> dict[str, Union[str, int], dict[str, Union[str, int, float]]]:
    if "created_date" not in data:
        data["created_date"] = datetime.now().timestamp()
    else:
        data["created_date"] = convert_timestamp(data['created_date'], "timestamp")
    directory = join(Path(__file__).parent.parent, 'logs')
    filename = datetime.now().strftime("%Y-%m-%d")
    try:
        await aiofiles.os.stat('/')
    except FileNotFoundError:
        # ToDo Maybe subclass all error messages?
        # ToDo Maybe break out to separate funcitons?
        return {"status": "failed", "error_message": "The file system is missing. Make sure the file system is mounted", "status_code": 500}
    try:
        await aiofiles.os.stat(directory)  # aiofiles does not implement any other method to check if a directory exists
    except:
        await aiofiles.os.mkdir(directory)
    try:
        await aiofiles.os.stat(f'logs/{filename}_log.txt')
        mode = 'a'
    except:
        mode = 'w'
    try:
        async with aiofiles.open(f'logs/{filename}_log.txt', mode=mode) as f:
            await f.write(json.dumps(data) + '\n')
        return {"status": "created", "status_code": 201, "response": data}
    except Exception as e:
        return {"status": "failed", "error_message": str(e), "status_code": 500}