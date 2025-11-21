import time
import scrapy
from ..models.province_config import AllProvincesConfig
from ..items import ProcurementItem
from ..utils.requests_utils import JsonRequest
from ..core.logger import setup_scrapy_logging


setup_scrapy_logging()

class GuangxiSpider(scrapy.Spider):
    name = "guangxi"

    def __init__(self, cfg=None, **kwargs):
        super().__init__(**kwargs)
        # ✅ 类型安全 + 提示
        self.cfg = cfg  # 从 from_crawler 传入 官方建议不直接在__init__中调用setting

    @classmethod
    def from_crawler(cls, crawler, *args, **kwargs):
        # 从 crawler 获取 settings
        raw = crawler.settings.get("PROVINCE_CONFIG", {})
        try:
            cfg = AllProvincesConfig(**raw).guang_xi
        except Exception as e:
            raise ValueError(f"配置解析失败: {e}")

        # 创建 spider 实例，并传入 cfg
        spider = cls(cfg=cfg, **kwargs)
        spider._set_crawler(crawler)  # 关键！绑定 crawler（包含 settings、stats 等）
        return spider

    def start_requests(self):
        # 动态生成 check 请求参数
        check_param = {
            **self.cfg.check.static_param,
            "pageNo": 1,
            "_t": int(time.time() * 1000),
        }

        if self.cfg.check.method == "post":
            yield JsonRequest(
                url=self.cfg.check.url,
                data=check_param,
                callback=self.parse_page_count
            )

    def parse_page_count(self, response):
        # 假设返回总页数 total_pages
        # total_pages = response.json().get("result").get("data").get("total", 1)
        total_pages = 1

        for page in range(1, total_pages + 1):
            param = {
                **self.cfg.check.static_param,
                "pageNo": page,
                "_t": int(time.time() * 1000),
            }
            yield JsonRequest(
                url=self.cfg.check.url,
                data=param,
                callback=self.parse_ids
            )

    def parse_ids(self, response):
        items = response.json().get("result").get("data").get("data")
        for item in items:
            article_id = item["articleId"]
            detail_param = {
                **self.cfg.detail.static_param,
                "articleId": article_id,
                "timestamp": int(time.time()),
            }

            url = self.cfg.detail.url
            if self.cfg.detail.method == "get":
                from urllib.parse import urlencode
                url = f"{url}?{urlencode(detail_param)}"

            yield scrapy.Request(
                url=url,
                method=self.cfg.detail.method.upper(),
                callback=self.parse_detail,
                meta={"item": item},
            )

    def parse_detail(self, response):
        item = ProcurementItem()
        title = response.json().get("result").get("data").get("title")
        item['title'] = title

