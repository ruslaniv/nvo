from datetime import datetime

import sqlalchemy.orm


def serialize(data):
    results = {}
    if isinstance(data, dict):
        _={}
        for k, v in data.items():
            if isinstance(v, sqlalchemy.orm.state.InstanceState):
                v = '_'
            if isinstance(v, sqlalchemy.orm.collections.InstrumentedList):
                v = serialize(v)
            if isinstance(v, datetime):
                v = serialize(v)
            results[k] = v
    elif isinstance(data, list):
        _ = []
        for record in data:
            _.append(serialize(record.__dict__))
        return _
    elif isinstance(data, datetime):
        return data.isoformat()
    return results