from datetime import datetime

from db import db_conn
from db.model import Message
from utils.serializer import serialize
from utils.timestamp import convert_timestamp


async def write_request_to_db(data):
    message = Message()
    message.transport = data['transport']
    message.target = data['target']
    message.message = data['message']
    if "created_date" not in data:
        message.created_date = datetime.now().timestamp()
    else:
        message.created_date = convert_timestamp(data['created_date'], "timestamp")
    try:
        async with db_conn.get_async_sa_session() as session:
            session.add(message)
            await session.commit()
        response = serialize(message.__dict__)
        del response["_sa_instance_state"]
        return {"status": "created", "status_code": 201, "response": response}
    except Exception as e:
        return {"status": "failed", "error_message": str(e), "status_code": 500}

