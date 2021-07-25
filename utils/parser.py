def parse_response(data):
    _ = {"messages": {}, "status": {}}
    _["messages"] = {"status": data["status"]}
    if "message" in data:
        _["messages"] = {"message": data["message"]}
    _["status"] = {"status_code": data["status_code"]}
    return _
