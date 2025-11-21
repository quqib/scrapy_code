# debug_guangxi.py
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from procurement.spiders.guangxi import GuangxiSpider  # ⚠️ 替换成你的真实模块路径！

if __name__ == "__main__":
    # 获取 settings.py 中的配置
    settings = get_project_settings()

    # 创建爬虫进程（单线程，适合调试）
    process = CrawlerProcess(settings)

    # 添加你的爬虫
    process.crawl(GuangxiSpider)

    # 启动（会阻塞直到爬虫结束）
    process.start()