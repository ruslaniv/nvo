from datetime import datetime
from typing import Union


def convert_timestamp(date: Union[datetime, datetime.timestamp], to: str) -> Union[datetime, datetime.timestamp]:
    if to == 'datetime':
        datetime_object = datetime.fromtimestamp(date)
        return datetime_object
    elif to == 'timestamp':
        timestamp = datetime.timestamp(datetime.fromisoformat(date))
        return timestamp
