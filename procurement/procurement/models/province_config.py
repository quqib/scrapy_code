"""
文件目的配置提示词：
    比方说在setting中定义的字段，调用时没有提示，使用pydantic这个库来解决这个问题
"""

from typing import Dict, Any, Literal
from pydantic import BaseModel


class RequestConfig(BaseModel):
    url: str
    method: Literal["get", "post"]
    static_param: Dict[str, Any]


class ProvinceConfigModel(BaseModel):
    check: RequestConfig
    detail: RequestConfig


class AllProvincesConfig(BaseModel):
    guang_xi: ProvinceConfigModel
    # jiang_su: ProvinceConfigModel  # 后续扩展