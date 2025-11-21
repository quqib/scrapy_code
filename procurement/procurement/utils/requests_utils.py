import json
from scrapy import Request

def JsonRequest(url, data, callback, **kwargs):
    """发送 JSON POST 请求的便捷函数"""
    return Request(
        url=url,
        method="POST",
        headers={"Content-Type": "application/json; charset=UTF-8"},
        body=json.dumps(data, ensure_ascii=False),
        callback=callback,
        **kwargs
    )