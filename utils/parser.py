from datetime import datetime
from typing import Union


def parse_response(data: dict[str, Union[str, int, datetime]]) -> dict[str, Union[dict[str, Union[str, float, int]], int]]:
    _ = {"messages": {"status": data["status"]}, "status_code": data["status_code"]}
    if "error_message" in data:
        _["messages"]["response"] = data["error_message"]
    else:
        _["messages"]["response"] = data["response"]
    return _
