def parse_response(data):
    _ = {"messages": {"status": data["status"]}, "status_code": data["status_code"]}
    if "error_message" in data:
        _["messages"]["response"] = data["error_message"]
    else:
        _["messages"]["response"] = data["response"]
    return _
